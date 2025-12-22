'''
the length based spliter allows you to split the text on the bases of number
of characters given in the argument if you given character = 100 then it will just split 
a chunk after 100 charector
'''

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("pdf.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
    separator= " "
)

result = splitter.split_documents(docs)

print(result[0].page_content)