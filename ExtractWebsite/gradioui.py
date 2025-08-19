import gradio as gr
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

# 1️⃣ Load your local NDIS knowledge base text
TXT_FILE = "privacy.txt"
if not os.path.exists(TXT_FILE):
    raise FileNotFoundError(f"{TXT_FILE} not found. Place your NDIS text file in the same folder.")

with open(TXT_FILE, "r", encoding="utf-8") as f:
    ndis_text = f.read()

# 2️⃣ Split the text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
docs = text_splitter.create_documents([ndis_text])

# 3️⃣ Create embeddings and local vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# Optional: save the vector store for future use
vectorstore.save_local("ndis_vectorstore")

# 4️⃣ Build retrieval-based QA chain
# This ensures the model only uses your TXT knowledge base
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o-mini", temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k":5})
)

# 5️⃣ Define chatbot response function
def ndis_chatbot(query):
    """
    Answers questions using only the local TXT knowledge base.
    """
    return qa.run(query)

# 6️⃣ Gradio UI
iface = gr.Interface(
    fn=ndis_chatbot,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything about NDIS..."),
    outputs="text",
    title="NDIS Knowledge Chatbot (Local TXT)",
    description="This chatbot only uses the local NDIS knowledge base text file. It does NOT access the internet."
)

# 7️⃣ Launch the web app
iface.launch(share=True)
