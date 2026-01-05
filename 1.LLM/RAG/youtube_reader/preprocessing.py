from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI,ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch,RunnableLambda,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


load_dotenv(dotenv_path="C:/Users/makerofdreams/Desktop/langchain_models/.env")


def get_transcript(id):
  try:
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.fetch(id,languages=["en"])
    transcript = " ".join(chunk.text for chunk in transcript_list)
    return transcript
  except TranscriptsDisabled:
    return "no caption available"

def splitter(transcript):
  splitter = RecursiveCharacterTextSplitter(
      chunk_size = 500,
      chunk_overlap = 50
  )
  chunks = splitter.create_documents([transcript])
  return chunks


def build_faiss_vectorstore(chunks):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

def context(docs):
  return "\n\n".join(doc.page_content for doc in docs)
#  creting the runnable

chain1 = (RunnableLambda(get_transcript) | RunnableLambda(splitter) | RunnableLambda(build_faiss_vectorstore))


# example key "QeVlSZGl6Hs"
id = str(input("id: "))
vector_store = chain1.invoke(id)

# print(vector_store.index_to_docstore_id)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(context),
    'question': RunnablePassthrough()
})

parser = StrOutputParser()

llm_chain = parallel_chain | prompt | llm | parser  

# answer = llm_chain.invoke("please summerise")

chat_history = []

# while True:
#   user_input = input("you: ")
#   chat_history.append(HumanMessage(content = user_input))
#   if user_input == "exit":
#     break
#   result = llm_chain.invoke(chat_history)
#   chat_history.append(AIMessage(content=result))
#   print("AI: ",result)

while True:
    user_input = input("you: ")
    if user_input == "exit":
        break

    result = llm_chain.invoke(user_input)
    print("AI:", result)