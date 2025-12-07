'''this json output parser help LLM to give output in json format'''
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser



load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template= "Give me the name, age and city of the fictional person /n {format_instruction}",
    input_variables=[],
    partial_variables= {"format_instruction":parser.get_format_instructions()}
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# the three lines can be used in a chain easily
chain = template | model | parser

result = chain.invoke({})#here it is mandatory to put a dict be it empty

print(result)