'''
semantic text splitter works by first splitting lines and then using an 
embedding model, it tries to find the cosine similarity between two sentences 
and on the bases of a perticular threshold it find that the similarity is not 
good enough
'''

from  langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)
'''
here the breakpoint thershold is standard deviation meaning the evaluation on
how different one line is from another so that it should be put as next line will be decided 
if the similarity score of that line is 1 standard deviation away from all previous lines
'''
sample = '''The afternoon felt slow and deliberate, as if the air itself had decided to linger, and while the kettle was heating on the stove the idea of learning a new language briefly crossed the mind before being replaced by a sudden concern about how migratory birds navigate across oceans without landmarks, which is strange because the original plan had been to organize a desk that was cluttered with old notebooks and receipts from grocery stores that no longer exist.

There is something comforting about routines, like walking the same route every morning, although halfway through that thought it becomes impossible not to think about how cloud computing relies on massive data centers that consume enormous amounts of electricity, which then leads to questions about sustainable architecture and why certain ancient buildings remain cooler than modern ones even without air conditioning.

Books often serve as quiet companions, but while remembering the smell of old paper and dust, the mind unexpectedly jumps to the mechanics of bicycle gears and how a small change in chain tension can dramatically alter speed, which feels unrelated until one realizes that efficiency is a shared theme across both reading habits and mechanical systems.

Conversations sometimes drift without warning, starting with weekend plans and smoothly sliding into debates about whether artificial intelligence can truly be creative, only to end with a recollection of childhood summers spent waiting for monsoon rains that never arrived on time, leaving behind a sense of anticipation that felt larger than the season itself.

Time moves forward regardless of intention, and even as one reflects on personal goals, thoughts veer sharply toward the economics of street food pricing and how vendors balance cost, taste, and demand, before returning abruptly to the difficulty of maintaining long-term focus in an environment filled with constant notifications.

Silence can be peaceful, yet during moments of stillness the brain often fills the gap by recalling fragments of unrelated knowledge, such as the way muscles store memory after repeated practice or why certain songs become popular despite having simple melodies, and these jumps rarely announce themselves with any clear transition.'''

docs = splitter.create_documents([sample])

print(docs[0])