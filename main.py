from transformers import pipeline
import os,shutil
import cv2
import uvicorn
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile,Response, status, HTTPException,Form

model_checkpoint = "rashid996958/Machine_translation_5-10_epochs"
translator = pipeline("translation", model=model_checkpoint)

app = FastAPI()

@app.get("/")
def read_root():
    return {"STATUS": "API WORKING"}

@app.post("/translate",status_code=status.HTTP_200_OK)
async def translate(response: Response, input_text: str = Form("How are you ?")):  
    response = {"hindi":translator(input_text)[0]['translation_text']}
    return response
