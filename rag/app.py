import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_text_splitters import NLTKTextSplitter




st.header('RAG SYSTEM ON "Content behind" paper')
loader=PyPDFLoader("pdf.pdf")

pages=loader.load_and_split()

page="".join([p.page_content for p in pages] )

f=open('.geminiai_api_key_1.txt')
key=f.read()
genai.configure(api_key=key)

text_splitter = NLTKTextSplitter(chunk_size=568, chunk_overlap=100)
chunks=text_splitter.split_documents(pages)

embedding_model= GoogleGenerativeAIEmbeddings(google_api_key=key,model='models/embeding-001')
db=Chroma.from_documents(chunks,embedding_model,persist_directory="./chroma_db_")
db.persist()
db_connection=Chroma(persist_directory="./chroma_db_",embedding_function=embedding_model)
retriver=db_connection.as_retrivever(search_kwargs={"k":5})
model=genai.GenerativeModel('gemini-1.5-pro-latest')

chat=model.start_chat(history=[])

user_input_1=st.text_input("Enter your question....")

user_input = page + user_input_1

response = chat.send_message(user_input)

if st.button("Answer"):
    st.subhedder("user query.....")
    st.write(user_input_1)
    st.subheader("Systems Response")
    st.write(response.text)