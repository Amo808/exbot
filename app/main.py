from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.api import router

app = FastAPI(title="MCP Server")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the MCP Server!"}

app.include_router(router)