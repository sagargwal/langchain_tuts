'''
runnable = A Runnable in LangChain is a standardized, executable unit that takes an input, performs a computation, and produces an output, and can be composed with other Runnables.
two types 
1. task specific runnable

these are core langchain components that have been converted into runnables so they can be used in pipelines 
do task specific operations like llm calls prompting retrival 
example -  chat openai 
prmopttemplate = formats prompts dynamically
retriever - retrieves relevent documents 
2. runnable primitive
these are fundamental  building blocks for structuring execution logic in ai workflows
help in  interation of differnt runnables
eg 
runnable sequence - runs steps in order
runnable parrellel - runs multiple steps simultaneusly
'''

# runnable sequence

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
# from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables= ["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({"topic":"tree"})

print(result)