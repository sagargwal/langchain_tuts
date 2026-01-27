import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

# Load env
load_dotenv(dotenv_path="C:/Users/makerofdreams/Desktop/langchain_models/.env")

st.set_page_config(page_title="YouTube Transcript Q&A", layout="centered")
st.title("📺 YouTube Transcript Q&A Bot")

# ---------- Functions ----------
def get_transcript(video_id: str) -> str:
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.fetch(video_id, languages=["en"])
        transcript = " ".join(chunk.text for chunk in transcript_list)
        return transcript
    except TranscriptsDisabled:
        return "no caption available"
    except Exception as e:
        return f"error: {str(e)}"


def splitter(transcript: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    chunks = splitter.create_documents([transcript])
    return chunks


def build_faiss_vectorstore(chunks):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store


def context(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# ---------- Session State ----------
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "llm_chain" not in st.session_state:
    st.session_state.llm_chain = None


# ---------- UI ----------
video_id = st.text_input("Enter YouTube Video ID", placeholder="e.g. QeVlSZGl6Hs")

if st.button("Build Knowledge Base"):
    if not video_id:
        st.warning("Please enter a YouTube video ID.")
    else:
        with st.spinner("Fetching transcript & building vector store..."):
            transcript = get_transcript(video_id)

            if transcript.startswith("no caption") or transcript.startswith("error"):
                st.error(transcript)
            else:
                chunks = splitter(transcript)
                vector_store = build_faiss_vectorstore(chunks)
                retriever = vector_store.as_retriever(
                    search_type="similarity", search_kwargs={"k": 4}
                )

                llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

                prompt = PromptTemplate(
                    template="""
You are a helpful assistant.
Answer ONLY from the provided transcript context.
If the context is insufficient, just say you don't know.

{context}
Question: {question}
""",
                    input_variables=["context", "question"],
                )

                parallel_chain = RunnableParallel(
                    {
                        "context": retriever | RunnableLambda(context),
                        "question": RunnablePassthrough(),
                    }
                )

                parser = StrOutputParser()
                llm_chain = parallel_chain | prompt | llm | parser

                st.session_state.vector_store = vector_store
                st.session_state.llm_chain = llm_chain

                st.success("Vector store built successfully! You can now ask questions.")


# ---------- Chat Section ----------
if st.session_state.llm_chain is not None:
    st.subheader("💬 Ask Questions")

    user_question = st.text_input("Your question")

    if st.button("Ask"):
        if not user_question:
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                answer = st.session_state.llm_chain.invoke(user_question)
                st.markdown("**AI:**")
                st.write(answer)
