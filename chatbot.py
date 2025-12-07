from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

# while True:
#     user_input = input("you: ")
#     if user_input == "exit":
#         break
#     result = model.invoke(user_input)
#     print("AI: ",result.content)

#the above code creates a simple chatbot that doesnot have a memory or chat history
# so if you talk with context of previous message it wont understand  

# in the follwing chat bot thier is a chatbot which remembers the context and gives a chat history
# chat_history = []

# while True:
#     user_input = input("you: ")
#     chat_history.append(user_input)
#     if user_input == "exit":
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print("AI: ",result.content)
# print(chat_history)

# although this is pretty good but the chat history doesnt give idea about who wrote what meaning 
# what was users input and what was AI's reply

# langchain messages
# in messages.py
# lets create a chat bot that has history with annotation or human,ai or system
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
chat_history = [#creating a system message in chat history and will append human message and ai message in this
    SystemMessage(content = "you are mahatma gandhi and reply with his wisdom")
]

while True:#so that keep asking your response
    user_input = input("you: ")# user input is taken here
    chat_history.append(HumanMessage(content = user_input)) # append in chat hostory so now chat history has system mesage and user message
    if user_input == "exit":
        break#if user want to break from from chatbot
    result = model.invoke(chat_history)#use model with system message and user message
    chat_history.append(AIMessage(content = result.content))# now just to maintain history and use it for next mesage with same context keeping system,ai,human message in same place 
    print("AI: ",result.content)
print(chat_history)# after breaking the while loop showing history

