'''
pypdf is a loader of langchain that allows user to direct load pdf 
it converts content of a pdf into document object
'''


from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("pdf.pdf")

docs = loader.load()

# print(docs[0].page_content)
print(docs[0].metadata["keywords"])