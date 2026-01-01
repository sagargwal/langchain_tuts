'''thier are model which can give structured output like openai, 
claude etc but most of the hugging face can not so to get structure output from them we need to have 
parser'''

'''output parser help convert raw llm output into structured formats like json ,csv pydantic model
and more, they ensure consistency validation, and ease ofthe use in application'''

'''four kinds are the common ones
1. str output parser
2. json outpt paser 
3. structured output parser
4. pydantic output parser
and more but these are most common ones'''
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm = llm)

# template for detailed report
template1 = PromptTemplate(
    template = "write a detailed report about {topic}",
    input_variables= ["topic"]
)

# template for 5 line summary
template2 = PromptTemplate(
    template="summerise the following text in five line /n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({"topic":"many ways to kill someone"})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({"text":result1})
result2 = model.invoke(prompt2)

print(result2.content)