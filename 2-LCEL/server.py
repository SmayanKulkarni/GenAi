import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] =os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] =os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langserve import add_routes
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI

model = OllamaLLM(model = "llama3")

embeddings = (
    OllamaEmbeddings(model = "llama3")
)
messages = [
    SystemMessage(content="Translate the following from english to German, just provide the translation, nothing else"),
    HumanMessage(content="Hello, how are you?")
]
parser =StrOutputParser()
from langchain_core.prompts import  ChatPromptTemplate    
system_template =   "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ('system' , system_template), 
    ('user', '{text}')
])
chain = prompt_template | model | parser
app = FastAPI(title = "Langchain Server",
              version  = "1.0",
              description="A simple API server using langchain runnable interfaces.")

add_routes(
    app,
    chain,
    path ="/chain"
)
if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
