# in this pericular application we are creating a solution that on the basis of user's sentiment gives a 
# tells if it is a neg feedback or a positive feedback

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

'''
for geting the sentiment 
requirements 
1. need a model to take input and assess the sentiment
2. need a prompt that tells the model to classify the sentiment 
3. need a parser that can instruct the prompt to ask the sentiment in positive or negetive and also to verify if model is gving output in positive or negetive
'''

class Feedback(BaseModel):
    sentiment: Literal["positive","negetive"] = Field(description="Give the sentement of the feedback")

parser2 = PydanticOutputParser(pydantic_object= Feedback)

prompt1 = PromptTemplate(
    template = "classify the sentiment of the following phone's feedback text into positive or negetive \n {feedback} \n {format_instruction}",
    input_variables= ["feedback"],
    partial_variables= {"format_instruction":parser2.get_format_instructions()}
)

classifier = prompt1 | model | parser2
# result = chain.invoke({"feedback":"i think it was ok not bad not good"})
# print(result.sentiment)
# print(prompt1.format(feedback="i think it was ok not bad not good"))

prompt2 = PromptTemplate(
    template = "write an appropriate respose to this positive feedback, make sure to read the feedback and give feedback specific answer \n {feedback}",
    input_variables= ["feedback"]
)

prompt3 = PromptTemplate(
    template = "write an appropriate respose to this negetive feedback, make sure to read the feedback and give feedback specific response \n {feedback}",
    input_variables= ["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt2 | model |parser),
    (lambda x:x.sentiment == "negetive", prompt3 | model |parser),
    RunnableLambda(lambda x: "could not find the sentiment")
)

chain = classifier | branch_chain
 
print(chain.invoke({"feedback":'''I’ve been using this phone for about two months, and overall, it has been an experience. The display is really impressive — the colors are vibrant, and the 120Hz refresh rate makes everything feel smooth. Watching videos and scrolling through apps feels great. The camera performance is also solid in good lighting, especially the main sensor, which captures sharp photos with natural colors. I really liked the portrait mode too; the edge detection is much better than my previous phone.

However, the performance has been disappointing. The processor struggles when I try playing heavier games or keep too many apps running in the background. There is noticeable lag, especially when switching between apps or opening the camera quickly. The battery life is also just average; with moderate use, I barely get through the day. It drains faster when gaming or using navigation.

One thing that really frustrated me is the heating issue. Even basic tasks like clicking pictures or using Instagram for a while cause the device to warm up more than expected. I’m not sure if it’s a software problem, but it definitely affects the experience.

On the positive side, the build quality feels premium, and the speakers are surprisingly loud and clear. The UI is clean, although there are still a few bloatware apps that I had to uninstall.

Overall, it’s a decent phone for camera and display lovers, but the processor and heating issues make it hard to recommend for heavy users. I hope future software updates fix some of these performance problems.'''}))
# print(
#     prompt2.format(
#         feedback="i think the phone was ok not bad not good but the camera is good, hated the processor"
#     )
# )
