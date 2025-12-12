# user will give text (a detailed text) , we will generate notes with this doc and create a quiz
"we will do this parellely "
"we will use one model to generate notes and other to generate notes simultaneously"
"and then we will merge the model"
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)

model2 = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template= "generate a simple and short notes from the following text \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template = "Genrate 5 short question and anwsers from the following \n {text}",
    input_variables= ["text"]
)

prompt3 = PromptTemplate(
    template = "merge the provided notes and quizes into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variable =["notes","quiz"]
)

parser = StrOutputParser()

parellel_chain = RunnableParallel({
    "notes" : prompt1 | model1| parser,
    "quiz" : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain  = parellel_chain | merge_chain

text  = '''
Runnable ¶
Bases: ABC, Generic[Input, Output]

A unit of work that can be invoked, batched, streamed, transformed and composed.

Key Methods¶
invoke/ainvoke: Transforms a single input into an output.
batch/abatch: Efficiently transforms multiple inputs into outputs.
stream/astream: Streams output from a single input as it's produced.
astream_log: Streams output and selected intermediate results from an input.
Built-in optimizations:

Batch: By default, batch runs invoke() in parallel using a thread pool executor. Override to optimize batching.

Async: Methods with 'a' suffix are asynchronous. By default, they execute the sync counterpart using asyncio's thread pool. Override for native async.

All methods accept an optional config argument, which can be used to configure execution, add tags and metadata for tracing and debugging etc.

Runnables expose schematic information about their input, output and config via the input_schema property, the output_schema property and config_schema method.

Composition¶
Runnable objects can be composed together to create chains in a declarative way.

Any chain constructed this way will automatically have sync, async, batch, and streaming support.

The main composition primitives are RunnableSequence and RunnableParallel.

RunnableSequence invokes a series of runnables sequentially, with one Runnable's output serving as the next's input. Construct using the | operator or by passing a list of runnables to RunnableSequence.

RunnableParallel invokes runnables concurrently, providing the same input to each. Construct it using a dict literal within a sequence or by passing a dict to RunnableParallel.

For example,


from langchain_core.runnables import RunnableLambda

# A RunnableSequence constructed using the `|` operator
sequence = RunnableLambda(lambda x: x + 1) | RunnableLambda(lambda x: x * 2)
sequence.invoke(1)  # 4
sequence.batch([1, 2, 3])  # [4, 6, 8]


# A sequence that contains a RunnableParallel constructed using a dict literal
sequence = RunnableLambda(lambda x: x + 1) | {
    "mul_2": RunnableLambda(lambda x: x * 2),
    "mul_5": RunnableLambda(lambda x: x * 5),
}
sequence.invoke(1)  # {'mul_2': 4, 'mul_5': 10}
Standard Methods¶
All Runnables expose additional methods that can be used to modify their behavior (e.g., add a retry policy, add lifecycle listeners, make them configurable, etc.).

These methods will work on any Runnable, including Runnable chains constructed by composing other Runnables. See the individual methods for details.

For example,


from langchain_core.runnables import RunnableLambda

import random

def add_one(x: int) -> int:
    return x + 1


def buggy_double(y: int) -> int:
    """Buggy code that will fail 70% of the time"""
    if random.random() > 0.3:
        print('This code failed, and will probably be retried!')  # noqa: T201
        raise ValueError('Triggered buggy code')
    return y * 2

sequence = (
    RunnableLambda(add_one) |
    RunnableLambda(buggy_double).with_retry( # Retry on failure
        stop_after_attempt=10,
        wait_exponential_jitter=False
    )
)

print(sequence.input_schema.model_json_schema()) # Show inferred input schema
print(sequence.output_schema.model_json_schema()) # Show inferred output schema
print(sequence.invoke(2)) # invoke the sequence (note the retry above!!)
Debugging and tracing¶
As the chains get longer, it can be useful to be able to see intermediate results to debug and trace the chain.

You can set the global debug flag to True to enable debug output for all chains:


from langchain_core.globals import set_debug

set_debug(True)
Alternatively, you can pass existing or custom callbacks to any given chain:


from langchain_core.tracers import ConsoleCallbackHandler

chain.invoke(..., config={"callbacks": [ConsoleCallbackHandler()]})
'''

result = chain.invoke({"text":text})

print(result)

chain.get_graph().print_ascii()