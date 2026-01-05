'''
Runnable_lambda using this we can convert any function into runnable meaning they can be integrated into a chain and will have a invoke method in them
'''

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

def word_count(arr):
    return len(arr.split())

model = ChatOpenAI()

prompt = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables= ["topic"]
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parellel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "word_count" : RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain,parellel_chain)

result = final_chain.invoke({"topic":"AI"})

print(result)

