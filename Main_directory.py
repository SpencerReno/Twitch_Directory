#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
import pandas as pd
import numpy as np 
from datetime import datetime
from sqlalchemy import create_engine
from keys import *


# In[2]:


global  bearer, full_directory_lst
full_directory_lst = []

url = f'https://id.twitch.tv/oauth2/token?client_id={my_client_id}&client_secret={my_client_secret}&grant_type=client_credentials'
x = requests.post(url)
bearer = x.text[17:47]


def get_directory():
    url = 'https://api.twitch.tv/helix/games/top'
    headers = { "Client-ID": f'{my_client_id}','Authorization': f'Bearer {bearer}',  'Accept': "application/vnd.twitchtv.v5+json", }
    resp = requests.get(url, headers = headers).json()

    for game in range(10):
        get_directory_viewers(resp['data'][game]['id'], resp['data'][game]['name'])


# In[3]:


def get_directory_viewers(game_id, game_name):
    url= f'https://api.twitch.tv/helix/streams?first=100&game_id={game_id}'
    headers = { "Client-ID": f'{my_client_id}','Authorization': f'Bearer {bearer}',  'Accept': "application/vnd.twitchtv.v5+json", }
    resp = requests.get(url, headers = headers).json()
    pig=resp['pagination']['cursor']

    total = 0


    while len(resp['data']) > 1:
        for x in range(len(resp['data'])):
            total += resp['data'][x]['viewer_count']


        url= f'https://api.twitch.tv/helix/streams?after={pig}&first=100&game_id={game_id}'
        headers = { "Client-ID": f'{my_client_id}','Authorization': f'Bearer {bearer}',  'Accept': "application/vnd.twitchtv.v5+json", }
        resp = requests.get(url, headers = headers).json()
        try:
            pig=resp['pagination']['cursor']
        except:
            pig=''
    
    full_directory_lst.append([game_name, total])


# In[4]:


def make_twitch_df(full_directory_lst):
    twitch_df = pd.DataFrame(columns=['Date', 'Time', 'Directory Name', 'Viewer Count'])
    
    date = str(datetime.now()).split(' ')[0]
    time = str(datetime.now()).split(' ')[1].split('.')[0]

    for item in full_directory_lst:
        twitch_df = twitch_df.append({'Date' : date, 'Time': time, 'Directory Name': item[0], 'Viewer Count' : item[1]},ignore_index=True )
    return twitch_df


# In[5]:


def create_db():
    global engine
    # create sqlite engine
    engine = create_engine('sqlite:///twitch.db', echo=True)
    # create connection to engine
    conn = engine.connect()

    return conn


# In[6]:


def add_to_db(twitch_df, conn):
    sqlite_table = "Twitch_Directory"
    twitch_df.to_sql(sqlite_table, conn, if_exists='append')


# In[7]:


get_directory()
print('Gathering DATA')
twitch_df = make_twitch_df(full_directory_lst)
print('API Gather Sucessful')
conn = create_db()
print('Adding to Database')
add_to_db(twitch_df, conn)
print('All opporations successful')



