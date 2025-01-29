import logging
from fastapi import FastAPI, Request
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from pydantic import BaseModel

# Set up logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

groq_api_key = "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"
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# 1. Create Prompt Template
system_template = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser = StrOutputParser()

# Create Chain
chain = prompt_template | model | parser

# Pydantic model for the input data
class ChainInput(BaseModel):
    language: str
    text: str

# App Definition
app = FastAPI(title="Langchain Server",
              version="1.0",
              description="A simple API server using Langchain runnable interfaces")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chain/invoke")
async def invoke_chain(input_data: ChainInput):
    logging.debug(f"Received data: {input_data}")
    
    # Convert the input data to a dictionary and pass it to the chain
    result = chain.invoke(input_data.dict())
    return result

# Error handling
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"An error occurred: {str(exc)}"},
    )

if __name__ == "__main__":
    import uvicorn
    logging.debug("Starting Uvicorn server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
