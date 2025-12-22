'''
directory loader = it is a document loader that lets you load multiple document from a folder

'''

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path = '.',# . because the pdfs are in same folder as the code
    glob= '*.pdf', # thier are many glob for differnt kinds of docs 
    loader_cls= PyPDFLoader # cause all are pdf 
)

docs = loader.load() # can also use lazy_loader if thier are lot of files
# lazy loader do not load all document first and then do operations 
# print(docs[100].page_content)

'''
note - You cannot use one
loader_cls for multiple file types; instead,
create separate DirectoryLoaders per file type and
merge the results.

docs = (DirectoryLoader(".", "*.pdf", PyPDFLoader).load()
      + DirectoryLoader(".", "*.txt", TextLoader).load())
'''

'''

loader vs lazy_loader

Loader (load) loads all documents at once into memory, so it is simple to use but can be memory-heavy for large datasets.

LazyLoader (lazy_load) loads documents one by one (as a generator), making it memory-efficient for large or many files.

Working style: load() returns a list of Document objects, while lazy_load() returns an iterator you loop over.

Use case: use Loader for small datasets / quick tests, and LazyLoader for large corpora or production RAG pipelines.
'''