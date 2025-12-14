'''
ruunable parallel is runable premetive that allows multiple runnable to execute in parellel,

each runnable runs on the same input and processes it independently,prducing a dictionary of outputs
'''
# creating an example

'''
linkdin post and tweet generater - user will give a topic and generater will genrate a tweet and a linkdin post of that topic 
'''

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model =ChatOpenAI()

prompt1 = PromptTemplate(
    template= "generate a linkdin post for the {topic}",
    input_variables= ["topic"]
)

prompt2 = PromptTemplate(
    template= "generate a tweet for the {topic}",
    input_variables= ["topic"]
)

parser = StrOutputParser()

parellel_chain = RunnableParallel({
    "linkedin" : RunnableSequence(prompt1,model,parser),
    "tweet" : RunnableSequence(prompt2, model, parser)}
)
result = parellel_chain.invoke({"topic":"about a project in AI using coputer vision"})


print(result)
print(result["tweet"])
# print(result["linkedin"])