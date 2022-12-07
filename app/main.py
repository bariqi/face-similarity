from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, Form
from pydantic import BaseModel
import face_service as face
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import sys
from starlette.requests import Request

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'])

class compare(BaseModel):
    photo1: str
    photo2: str

@app.get("/")
def read_root():
    return {"Welcome in Zoho face-similarity system"}

@app.post("/verify")
async def create_item(item: compare):
    face_photo1 = face.detectandrecog('base64',item.photo1).detect_and_extract_embed()
    face_photo2 = face.detectandrecog('base64',item.photo2).detect_and_extract_embed()

    result = face.comparison(face_photo1, face_photo2)
    return JSONResponse(content=result)