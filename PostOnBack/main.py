from contextlib import asynccontextmanager
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func

from models import User, init_db, async_session
import my_requests as rq

from datetime import datetime, timedelta
from passlib.context import CryptContext

from fastapi import FastAPI, UploadFile, File, Form, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
import os
import uuid
import joblib
import cv2
import numpy as np
import re
import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import tempfile
from model import analyze as an
import pandas as pd


UPLOAD_DIR = tempfile.mkdtemp(prefix="post_analysis_")
os.makedirs(UPLOAD_DIR, exist_ok=True)
vectorizer = TfidfVectorizer(max_features=1000)

# Load your pre-trained model

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print('Bot is ready')
    yield   

app = FastAPI(title = "PostON", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/register", response_model=rq.UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: rq.UserCreate):
    # Check if user already exists
    async with async_session() as session:
        db_user = await session.scalar(select(User).where(User.email == user.email))
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already registered"
            )
        print('OAOAOAOAOAOO')
        # Validate password
        try:
            rq.validate_password(user.password)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        
        # Hash password
        hashed_password = pwd_context.hash(user.password)
        
        # Create new user
        new_user = User(
            id=str(datetime.utcnow().timestamp()),
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            hashed_password=hashed_password,
            created_at = datetime.utcnow()
        )
        
        session.add(new_user)
        await session.commit()
        
        return {
            "message": "Registration successful",
            "redirect": "/signin"
        }
    
@app.post("/signin", response_model=rq.TokenResponse)
async def signin_user(user: rq.UserLogin):
    async with async_session() as session:
        # Check if user exists and verify password
        db_user = await session.scalar(select(User).where(User.email == user.email))
        
        if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Generate access token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = rq.create_access_token(
            data={"sub": db_user.id},
            expires_delta=access_token_expires
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "message": "Login successful",
            "redirect": "/dashboard"
        }
    

MODEL = joblib.load("/Users/aleksandrcuvpilo/Desktop/PostOnBack/model/best_xgb_model.pkl")
@app.post("/analyze")
async def analyze_content(
    text: str = Form(...),
    images: List[UploadFile] = File(...)
):
    try:
        # Process images
        medium_photo_text = 0
        medium_photo_colorfulness = 0
        cnt_images = 0
        for image in images:
            # Save uploaded image
            file_ext = image.filename.split('.')[-1]
            filename = f"{uuid.uuid4()}.{file_ext}"
            file_path = os.path.join(UPLOAD_DIR, filename)
            
            with open(file_path, "wb") as buffer:
                buffer.write(await image.read())


            has_text = an.detect_text(file_path)
            colorfulness = an.calculate_colorfulness(file_path)

            medium_photo_colorfulness += colorfulness
            medium_photo_text += has_text
            cnt_images += 1

            os.remove(file_path)
        try:
            medium_photo_text /= cnt_images
            medium_photo_colorfulness /= cnt_images
        except:
            medium_photo_text = 0
            medium_photo_colorfulness = 0

        text_analysis = an.analyze_post(text)
            # Cleanup temporary file
        emojicount, tagscount, wordcount, linkcount = an.cnt_text_elem(text)
        features = {
            "text": text,
            "emoji": emojicount,
            "words": wordcount,
            "medium_photo_text": medium_photo_text,
            "medium_photo_colorfulness": medium_photo_colorfulness,
            "parts_cnt": text_analysis["Структура текста"]["Количество абзацев"],
            'difficult': text_analysis["Язык и стиль"]["Сложность текста"],
            'emote': 0
        }
        input_df = pd.DataFrame([features])  

        text_features = vectorizer.transform(input_df['text']).toarray()

        # Step 4: Combine the numerical features with the transformed text features
        numerical_features = input_df.drop(columns=['text']).values  # Drop the 'Text' column
        X_input = np.hstack((numerical_features, text_features))

        # Step 5: Make predictions
        predicted_value = MODEL.predict(X_input)

        # Output the predicted value
        print(f"Predicted value: {predicted_value[0]}")
        return JSONResponse({
            "prediction": predicted_value,
            "feature_breakdown": features
        })
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Bad request: {e}"
        )