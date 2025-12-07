# here we make a chatbot where user can in the go set the systempromt as per it need what for some questions you need an ai expert but for some case you need cricket expert so we will have dynamic system prompt
from langchain_core.prompts import ChatPromptTemplate
chat_template = ChatPromptTemplate([
    ("system", "you are a {domain} expert"),
    ("human", "exaplain me the {topic}")
])

prompt = chat_template.invoke({"domain":"cricket","topic":"Dusra"})

print(prompt)