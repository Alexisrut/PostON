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
import analyze as an

access_token = '7467ea587467ea587467ea58a97776aa9e774677467ea58173abbe1a90fd6c976a91670'
# owner_id2 = 68661738

count = 0
offset = 0

img = "./downloaded_image.jpg"


f = open("file.pkl", "wb")
with open("yes.txt", "r") as file:
    files = file.read()
    emoji = files.split()
temp = open('temp.txt', "wb")

def getjson(url, params):
    response = requests.get(url, params=params)
    try:
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()  # Try to parse JSON
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")  # Print HTTP error message
        return {}
    except ValueError as e:
        print(f"JSON decode error: {e}")  # Print JSON decode error message
        print("Response text:", response.text)  # Print the raw response text
        return {}

def get_all_posts(access_token, owner_id, count=500, offset=0):
    all_posts = []
    k = 0
    last_post_date = -1

    while True:
        time.sleep(0.3)
        wall = getjson('https://api.vk.com/method/wall.get',
                        {'owner_id': owner_id, 'offset': offset, 'count': count, 'access_token': access_token, 'v': '5.131'})
        count_posts = wall['response']['count']
        posts = wall['response']['items']

        all_posts.extend(posts)

        last_post_date = int(datetime.datetime.fromtimestamp(int(all_posts[-1]['date'])).strftime('%Y'))

        # if k % 50 == 0:
        #     print(k)
        # k += 1
        if last_post_date == 2023:
            break
        else:
            offset += 100
    return all_posts

def filter_data(all_posts):
    filtered_data = []
    photo_cnt = 0
    for post in all_posts:
        try:
            id = post['id']
        except:
            id = ' '
        try:
            text = post['text']
        except:
            text = 'текста нет'
        try:
            likes = post['likes']['count']
        except:
            likes = 0
        try:
            date = post['date']
        except:
            date = 0
        try:
            cnt_comm = post['comments']['count']
        except:
            cnt_comm = 0
        try:
            views = post['views']['count']
        except:
            views = 0
        photo_ids = []
        for i in post['attachments']:
            if i['type'] == 'photo':
                #print(i['photo'])
                #width = i['photo']['width']
                #height = i['photo']['height']
                #print(i['photo']['sizes'])
                for j in i['photo']['sizes']:
                    if j['type'] == 'x':
                        photo_cnt = 1
                        photo_ids.append(j['url'])
                        break
                if(photo_cnt == 0):
                    photo_ids.append(i['photo']['sizes'][0]['url'])

        filtered_post = {'id': id, 'text': text, 'likes': likes, 'date': date, 'cnt_comm': cnt_comm, 'photo_ids': photo_ids, 'views': views}

        filtered_data.append(filtered_post)

    return filtered_data

def get_all_liked_lists(access_token, owner_id, liked_object_id, count=1000, offset=0, friends_only=0):
    time.sleep(0.3)
    api_query = getjson('https://api.vk.com/method/likes.getList',
                        {'access_token': access_token, 'type': 'post', 'owner_id': owner_id, 'item_id': liked_object_id,
                            'filter': 'likes', 'friends_only': friends_only, 'count': count, 'v': '5.131'})
    Users_count = api_query['response']['count']
    List_of_users = api_query['response']['items']
    return Users_count, List_of_users

def get_all_users_bdate(access_token, user_ids, count=100, offset=0):
    time.sleep(0.3)
    User_Birth_date = []
    arr_request = []
    while True:
        time.sleep(0.3)
        arr_request = user_ids[offset:(offset+100)]
        api_query_user_info = getjson('https://api.vk.com/method/users.get',
                                        {'access_token': access_token, 'user_ids': arr_request, 'fields': 'bdate, sex', 'count': count,
                                        'v': '5.131'})
        for i in api_query_user_info['response']:
            User_Birth_date.append(i)
        if offset + 100 > len(user_ids):
            break
        else:
            offset += 100
    
    arr_request = user_ids[offset:len(user_ids)-offset]
    api_query_user_info = getjson('https://api.vk.com/method/users.get',
                                    {'access_token': access_token, 'user_ids': arr_request, 'fields': 'bdate, sex', 'count': count,
                                    'v': '5.131'})
    for i in api_query_user_info['response']:
        User_Birth_date.append(i)
    # User_Birth_date = api_query_user_info['response'][0]
    return User_Birth_date

def create_data(owner_id):
    all_posts = get_all_posts(access_token, owner_id)
    final_filter = filter_data(all_posts)
    ID_list = []
    txt_list = []
    likes_list = []
    date_list = []
    cnt_comm_list = []
    photo_ids_list = []
    view_list = []
    for post1 in final_filter:
        ID_list.append(post1['id'])
        txt_list.append(post1['text'])
        likes_list.append(post1['likes'])
        date_list.append(post1['date'])
        cnt_comm_list.append(post1['cnt_comm'])
        photo_ids_list.append(post1['photo_ids'])
        view_list.append(post1['views'])

    User_lists_collection = []
    Final_list = {}
    t = 0
    for item in ID_list:
        text_id = txt_list[t]
        emojicount, tagscount, wordcount, linkcount = an.cnt_text_elem(text_id)
        liked_object_id = item
        User_list_of_responses = get_all_liked_lists(access_token, owner_id, liked_object_id)
        text_analyze = an.analyze_post(text_id)

        all_text = 0
        all_colorfulness = 0
        cnt_text = 0
        cnt_colorfulness = 0

        for j in photo_ids_list[t]:
            has_text, colorfulness = an.anylyse_url(j)
            all_text += int(has_text)
            all_colorfulness += int(colorfulness)
            cnt_text += 1
            cnt_colorfulness += 1
        try:
            medium_photo_text = all_text/cnt_text
        except:
            medium_photo_text = 0
        try:
            medium_photo_colorfulness = all_colorfulness/cnt_colorfulness
        except:
            medium_photo_colorfulness = 0
        list_of_users_ids = User_list_of_responses[1]
        user_id = str(list_of_users_ids).strip('[]')
        person_bdate = get_all_users_bdate(access_token, user_id)

        nfl = [i for i in person_bdate]
        female_all = [i for i in nfl if 'sex' in i and i['sex'] == 1]
        male_all = [i for i in nfl if 'sex' in i and i['sex'] == 2]
        new_filtered_list = [i for i in person_bdate if 'bdate' in i and len(i['bdate']) > 6 and int(i['bdate'][-4:]) >= 2002 and int(i['bdate'][-4:]) <= 2010]
        nfl2 = [i for i in person_bdate if 'bdate' in i and len(i['bdate']) > 6 and int(i['bdate'][-4:]) <= 1993]

        f = 0
        list_of_likes = len(new_filtered_list)
        list_of_likes2 = len(nfl2)
        lol = len(nfl)
        if list_of_likes != 0:
            f = (list_of_likes / lol) * 100
        f = str(f) + '%'

        Final_list = {'text_id': text_id, 'emoji': emojicount, 'tags': tagscount, 'links': linkcount, 'words': wordcount, 'likes_all': lol, 'likes_count(<21)': list_of_likes, 'likes_count(>31)': list_of_likes2, 'female_likes': len(female_all), 'male_likes': len(male_all), 
                        'date': date_list[t], 'headers_cnt': text_analyze['Структура текста']['Количество заголовков'], 'parts_cnt': text_analyze['Структура текста']['Количество абзацев'], 'difficult': text_analyze['Язык и стиль']['Сложность текста'], 
                            'emote': text_analyze['Язык и стиль']['Эмоциональная окраска'], 'medium_photo_text': medium_photo_text, 'medium_photo_colorfulness': medium_photo_colorfulness, 'views': view_list[t]}
        User_lists_collection.append(Final_list)
        df = pd.DataFrame(User_lists_collection)
