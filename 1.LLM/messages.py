# langchain has three types of messages
# system_message, human_message, AI_message

'''
System Message: Sets the behavior, role, and rules for the AI assistant.
Human Message: The user’s input or query that the AI needs to respond to.
AI Message: The assistant’s response generated based on the system and human messages.
'''
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="you are a professional basketball player answer with your expertise"),
    HumanMessage(content = "why does india have bad basketball")
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)