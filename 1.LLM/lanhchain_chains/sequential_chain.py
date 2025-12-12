from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template= "give me a dtailed report of 200 words for {topic}",
    input_variables= ["topic"]
)

prompt2 = PromptTemplate(
    template = "generate a 5 pointer summary from the following text \n {text}",
    input_variables= ["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()
chain = prompt | model | parser | prompt2 | model | parser

result = chain.invoke({"topic":"google gsoc 2026"})

# print(result)

chain.get_graph().print_ascii()