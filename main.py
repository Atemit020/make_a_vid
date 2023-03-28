from praw import Reddit
from gtts import gTTS
from random import choice, randint
from PIL import Image
from selenium import webdriver
from moviepy import editor
from mp import videfy

def reddit():
    reddit = Reddit (
        client_id = "ny6eTtYlA1Ns1ZAemd3jhQ",
        client_secret = "yNvsS-AipNEDNCAAMOafYaniYs3lUQ",
        user_agent = "post_scraper_bot_atemit",
    )

    subreddit = reddit.subreddit("Showerthoughts")

    post_ids = list()
    post_text = list()


    with open("./id.txt", "r") as f:
        for i in f.readlines():
            if i != "":
                post_ids.append(i)


    def submission():
        for i in subreddit.top(limit=1000):
            if i.score >= 500:
                post_text.append(i)
        while True:
            a = choice(post_text)
            if a.id not in post_ids:
                with open("./id.txt", "a") as f:
                    f.write(a.id+"\n")
                return a


    for i in range(5):
        _submission = submission()
        #image_geter(_submission.url, i)
        print(_submission.title)
        audio = gTTS(_submission.title)
        audio.save("audio"+ str(i) +".mp3")
    
try:
    vid_amount = int(input("Enter the amount of videos you want: "))
    if vid_amount <= 0: vid_amount = 1

except TypeError:
    print(TypeError)

for i in range(vid_amount):
    reddit()
    videfy(i)
    