'''
RunnableBranch - is the control flow component that allows you to conditionally route input data 
to different chains or runnables based on custom logics 

it is langchain's if/else
'''

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableBranch, RunnablePassthrough
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

report_gen_chain = prompt1 | model | parser 

branch_gen_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt1 | model | parser),
    
     RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_gen_chain)

print(final_chain.invoke({"topic": "russian vs ukraine"}))