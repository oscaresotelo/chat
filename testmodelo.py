# import os
# import requests 
# token = "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"
# os.environ["HUGGINFACEHUB_API_TOKEN"] = token

# # url = "https://raw.githubusercontent.com/hwchase17/langchain/master/docs/modules/state_of_the_union.txt"
# # res = "evangelio.txt"
# # with open("evangelio.txt", "w") as f:
# #   f.write(res.text)

# from langchain.document_loaders import TextLoader
# loader = TextLoader('la_biblioteca_de_babel.txt')
# documents = loader.load()

# import textwrap

# def wrap_text_preserve_newlines(text, width=110):
#     # Split the input text into lines based on newline characters
#     lines = text.split('\n')

#     # Wrap each line individually
#     wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

#     # Join the wrapped lines back together using newline characters
#     wrapped_text = '\n'.join(wrapped_lines)

#     return wrapped_text

# # Text Splitter
# from langchain.text_splitter import CharacterTextSplitter
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)

# from langchain.embeddings import HuggingFaceEmbeddings

# embeddings = HuggingFaceEmbeddings()


# from langchain.vectorstores import FAISS

# db = FAISS.from_documents(docs, embeddings)

# query = "desde donde se ven los pisos superiores"
# docs = db.similarity_search(query)


# from langchain.chains.question_answering import load_qa_chain
# from langchain import HuggingFaceHub

# llm = HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":0, "max_length":512})

# chain = load_qa_chain(llm, chain_type="stuff")
# query = "What did the president say about the Supreme Court"
# docs = db.similarity_search(query)
# chain.run(input_documents=docs, question=query)

# query = "desde donde se ven los pisos superiores?"
# docs = db.similarity_search(query)
# chain.run(input_documents=docs, question=query)
# print(wrap_text_preserve_newlines(str(docs[0].page_content)))
import os
import requests 
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
import textwrap

# Set Hugging Face API token
token = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = token

# Load text from local file
loader = TextLoader('state_of_the_union.txt')
documents = loader.load()

# Split text into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Generate embeddings for text chunks
embeddings = HuggingFaceEmbeddings()

# Create vector store for text chunks
db = FAISS.from_documents(docs, embeddings)



# Define function to wrap text while preserving newlines
def wrap_text_preserve_newlines(text, width=50):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text
query = "which was Our goal ?"
docs = db.similarity_search(query)
print(wrap_text_preserve_newlines(str(docs[0].page_content)))
# Perform similarity search and run question answering chain for two different queries
# llm=HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":0, "max_length":512})
# chain = load_qa_chain(llm, chain_type="stuff")
# query1 = "What did the president say about economy?"
# docs1 = db.similarity_search(query1)
# chain.run(input_documents=docs1, question=query1)
# print(wrap_text_preserve_newlines(str(docs1[0].page_content)))

# query2 = "Desde donde se ven los pisos superiores?"
# docs2 = db.similarity_search(query2)
# chain.run(input_documents=docs2, question=query2)

# Print the content of the first document returned by the similarity search, wrapped to fit within 110 characters per line
