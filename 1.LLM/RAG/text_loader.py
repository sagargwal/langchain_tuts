'''
TextLoader is a simple and commonly used document loader in LangChain that reads plain text(.txt)
files and convert them into Langchain Document object

Use Case 
1. ideal for using chatlogs, scrapped test, transcript, code snippits, or any plain text data
into a langchain pipeline

limitation

works only with txt.files
'''
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

loader = TextLoader("wind.txt", encoding = "utf-8")

docs = loader.load() # here the txt has beeen converted into a document object or standard format

prompt = PromptTemplate(
    template = "give the refferences used by the poet in this {poem}",
    input_variables= ["poem"]
)

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({"poem":docs[0].page_content}))
