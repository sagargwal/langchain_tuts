'''
lang_chain_passthrough just give the inut as output but in some cases it can be helpful

in this example user want the joke and the joke explaination as an output (not just the joke explaination)
'''
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough
# from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables= ["topic"]
)

parser = StrOutputParser()

joke_gen_chain = prompt1 | model | parser
# result1 = joke_gen_chain.invoke({"topic":"tree"})

prompt2 = PromptTemplate(
    template = "write the explaination of this {joke}",
    input_variables= ["joke"]
)

joke_explainer_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "joke_explainer" : RunnableSequence(prompt2, model, parser)
})


final_chain = RunnableSequence(joke_gen_chain,joke_explainer_chain)

print(final_chain.invoke({"topic":"cricket"}))