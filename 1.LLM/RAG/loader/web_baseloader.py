from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

url = "https://www.nbcnews.com/world/australia/bondi-beach-shooting-suspect-charged-59-offenses-terrorism-murder-rcna249641"

loader = WebBaseLoader(url)

doc = loader.load() #this is the main doc

prompt = PromptTemplate(
    template= "answer {question} based upon {text}",
    input_variables= ["question","text"]
)

chain = prompt | model | parser

print(chain.invoke({"question":"what is socially wrong in this","text":doc}))