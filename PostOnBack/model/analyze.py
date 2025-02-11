import requests
import time
import pickle
import datetime
import json
import time
import pandas as pd
import os
import cv2
import numpy as np
from PIL import Image
from torchvision import models, transforms
from transformers import pipeline
import easyocr
from matplotlib import pyplot as plt
import seaborn as sns
import re

with open("/Users/aleksandrcuvpilo/Desktop/PostOnBack/model/yes.txt", "r") as file:
    files = file.read()
    emoji = files.split()

# Наличие текста
def detect_text(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    return 1 if result else 0

# Оценка красочности
def calculate_colorfulness(image_path):
    image = cv2.imread(image_path)
    (B, G, R) = cv2.split(image.astype("float"))
    rg = np.abs(R - G)
    yb = np.abs(0.5 * (R + G) - B)
    rg_mean, rg_std = np.mean(rg), np.std(rg)
    yb_mean, yb_std = np.mean(yb), np.std(yb)
    std_root = np.sqrt((rg_std ** 2) + (yb_std ** 2))
    mean_root = np.sqrt((rg_mean ** 2) + (yb_mean ** 2))
    colorfulness = std_root + (0.3 * mean_root)
    return min(10, max(1, int(colorfulness / 10)))

# Запрос к llama_request
def llama_request(prompt):
    """Отправка запроса к LLM и получение ответа."""
    # URL вашего сервера
    url = 'http://localhost:11434/api/chat'
    payload = {
        "model": "llama3.1:8b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
        "max_token": 10000
    }

    # Отправка POST-запроса
    response = requests.post(
        url,
        data=json.dumps(payload)
    )
    return response.json()['message']['content']

# Анализ текста с помощью llama
def analyze_post(post_text):
    # 1. Тематика поста
    # 2. Структура текста
    word_count = len(post_text.split())
    char_count = len(post_text)
    
    # Проверка наличия заголовков и списков
    headers = len(re.findall(r'(^|\n)(#+\s|\s*\d+\.\s|\*\s)', post_text))
    paragraphs = post_text.strip().split("\n\n")
    has_lists = bool(re.search(r'(^|\n)(\d+\.\s|\*\s)', post_text))
    
    # 3. Язык и стиль
    
    slang_prompt = f"Оцени простоту текста ответив только оценку 1 до 10 без точки в конце. Оцени насколько сложен текст с точки зрения трудных слов, сложных/длинных граматических констркуций и тому подобное. \"{post_text}\"."
    uses_slang = llama_request(slang_prompt)
    
    emotion_prompt = f"Определи эмоциональную окраску текста одним словом: \"{post_text}\". Пример ответа: радостная, грустная, нейтральная. Ответь только слово - эмоциональная окраска. Больше ничего не пиши."
    emotion = llama_request(emotion_prompt)
    
    # Результаты анализа
    result = {
        "Структура текста": {
            "Количество слов": word_count,
            "Количество символов": char_count,
            "Количество заголовков": headers,
            "Количество абзацев": len(paragraphs),
            "Есть списки": has_lists,
        },
        "Язык и стиль": {
            "Сложность текста": uses_slang,
            "Эмоциональная окраска": emotion,
        },
    }
    
    return result

def cnt_text_elem(text):
    tsplit = text.split()
    emojicount = 0
    tagscount = 0
    wordcount = 0
    linkcount = 0
    for i in range(len(tsplit)):
        tsp = tsplit[i]
        x = tsp.find('#')
        if x != (-1):
            tagscount += 1
            wordcount -= 1
        for j in range(len(tsp)):
            if tsp[j] in emoji:
                emojicount +=1
        if tsp not in emoji:
            wordcount += 1
        y = tsp.find('.')
        if y != (-1) and y != len(tsp)-1:
            linkcount += 1
            wordcount -= 1
    return emojicount, tagscount, wordcount, linkcount

def anylyse_url(url):
    img = "./downloaded_image.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        with open(img, "wb") as file:
            file.write(response.content)
        #print(f"Image downloaded successfully and saved as '{img}'.")
    else:
        pass
        #print(f"Failed to download image. HTTP status code: {response.status_code}")
    image_path = img
    has_text = detect_text(image_path)
    #has_people = detect_people(image_path)
    #objects = detect_objects(image_path)
    colorfulness = calculate_colorfulness(image_path)
    os.remove(img)
    return has_text, colorfulness