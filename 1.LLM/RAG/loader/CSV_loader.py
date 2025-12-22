'''
helps you load a csv 
'''
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
loader = CSVLoader("train_and_test2.csv")

data = loader.load()
data_10 = data[:10]
# print(data[0].page_content)

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

# url = "https://www.nbcnews.com/world/australia/bondi-beach-shooting-suspect-charged-59-offenses-terrorism-murder-rcna249641"

# loader = WebBaseLoader(url)

# doc = loader.load() #this is the main doc

prompt = PromptTemplate(
    template= "answer {question} based upon {data}",
    input_variables= ["question","data"]
)

chain = prompt | model | parser

print(chain.invoke({"question":"what is the mean of each column","data":data_10}))
