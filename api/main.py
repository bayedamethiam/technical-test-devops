import json
import logging
import os
import uuid

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pymongo import MongoClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Secret Message API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],  # Allows all methods
    allow_headers=["Content-Type"],  # Allows all headers
)

# Connect to mongoDB
mongo_url = os.environ.get("MONGO_URL")
mongo_database = os.environ.get("MONGO_DATABASE")

client: MongoClient = MongoClient(mongo_url)
db = client.get_database(mongo_database)  # type: ignore
collection = db.get_collection("messages")
logger.info(
    f"Connected to MongoDB at {mongo_url} with database {mongo_database}"
    )


class MessageBody(BaseModel):
    message: str


class Message(BaseModel):
    message: str
    identifier: str


@app.post("/message")
async def create_message(message: MessageBody):
    """
    Create a new message
    """
    to_insert = Message(message=message.message, identifier=str(uuid.uuid4()))

    collection.insert_one(to_insert.model_dump())
    return to_insert


@app.get("/message/{query}")
async def get_message(query: str):
    q = json.loads(query)
    message = collection.find_one(q)
    if message is None:
        logger.warning(f"Message not found: {q}")
        return JSONResponse(
            content={"message": "Message not found"}, status_code=404
        )
    logger.info(f"Found message: {message}. Deleting...")
    collection.delete_one(q)
    return MessageBody(message=message["message"])  # type: ignore


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
