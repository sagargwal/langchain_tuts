'''### **Structured Output**

* Data follows a fixed format like JSON, tables, or key-value pairs.
* Easy for machines to parse, validate, and use in automation or APIs.
* Used when the model must interact with tools, databases, or workflows.

### **Unstructured Output**

* Free-form text like paragraphs, explanations, or natural conversation.
* Designed for humans, not strict machine parsing.
* Used in chat responses, storytelling, and open-ended communication.
'''
# in this file we study with_structured data, that work as extracting specific information from natural text 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Literal, Optional
from pydantic import BaseModel,Field
load_dotenv()

model = ChatOpenAI()
# this is a simple use of typedict 
'''class Review(TypedDict):
    summary : Annotated[str,"give a one line summary of 10 words"]
    sentiment : Annotated[str,"analysis and give if it is a [like] or [dislike]"]

structured_review = model.with_structured_output(Review)
result = structured_review.invoke("I really like this coffee cup! The design is simple and classy, and it feels great in the hand. I just wish it was a little bigger, but overall, I’m happy with it.")

print(result)'''
#{'summary': 'Coffee cup with simple and classy design, feels great in the hand, wished it was bigger, overall happy.', 'sentiment': 'like'}

class Review(BaseModel):
    key_themes : list[str] = Field(description= "write all key themes from the review in a list")
    summary : list[str] = Field(description="give a summary in 20 words")

    sentiment :Literal["like","dislike"] = Field(description = "analysis and give if it is a [like] or [dislike]")
    pros : list[str] = Field(description = "write what the customer likes about the product")
    cons : list[str] = Field(description = "write what customer dislikes about the product")
    reason : str = Field(description = "write why poople are disgusted about this product and dont want to even see it")
    name : Optional[str] = Field(description = "what is the name of the reviewer")
structured_review = model.with_structured_output(Review)
result = structured_review.invoke('''I’ve been using the Poco X4 long enough now to get a proper feel for it, and technically speaking, it’s a pretty capable mid-range device, though with some clear compromises.

The Snapdragon processor holds up well for general multitasking and even gaming to an extent — titles like COD Mobile and BGMI run smoothly on medium to high settings without major throttling in the first 20–30 minutes. After longer sessions, you notice slight thermal buildup, and performance dips a bit, but nothing dramatic. RAM management is decent; background apps don’t reload aggressively unless you really push it.

The display is definitely one of its highlights — the AMOLED panel with the high refresh rate feels smooth and responsive, especially during scrolling, animations, and UI navigation. Color reproduction is fairly accurate, and HDR content looks good, though maximum brightness could’ve been higher for better outdoor visibility.

The camera system is where things get interesting. In good lighting conditions, the main sensor produces sharp, contrast-rich images with decent dynamic range. The processing leans a bit towards boosting saturation and sharpness, which some users may like. Portrait separation is generally clean, though edge detection occasionally misses fine hair lines. In low light, however, the sensor and ISP struggle — noise reduction gets aggressive, softening details, and exposure sometimes fluctuates. Night mode helps, but it’s slower and still can’t fully compensate for the hardware limitations. Video stabilization works fine for casual use, but it’s not flagship-level.

Battery life is reliable — a full day on moderate use is realistic thanks to the efficient chipset and large battery. The charging speed is a big plus; it goes from almost empty to usable levels very quickly, so downtime feels minimal.

Software is probably the most inconsistent part. btw i am Sagar,MIUI has improved, but there’s occasional stutter in animations, a few preinstalled apps you’ll never use, and notification handling can be unpredictable at times. Nothing catastrophic, just mildly annoying if you care about polish.

Overall, the Poco X4 is technically well-balanced for its category: solid performance, great display, fast charging, and a camera that performs well only under the right conditions. It’s a good fit for people who want specs and performance per rupee, but if you care more about refined software or consistent camera performance, you’ll feel the compromises.''')

print(result)

