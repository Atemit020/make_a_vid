from moviepy import editor, video
from random import randint
import os


def videfy(i):
    clip = editor.VideoFileClip("./vid.mp4")
    clip.resize(height = 1920, width = 1080)
    clip = clip.subclip(randint(15.00, 35.00), randint(clip.start, 600.00))
    a0 = editor.AudioFileClip("./audio0.mp3")
    a2 = editor.AudioFileClip("./audio1.mp3")
    a3 = editor.AudioFileClip("./audio2.mp3")
    a4 = editor.AudioFileClip("./audio3.mp3")
    a5 = editor.AudioFileClip("./audio4.mp3")
    outro = editor.AudioFileClip("./outro.mp3")
   # clip = clip_.subclip(randint(15.00, 600.00), randint(15.00, 600.00))

    mixed = editor.CompositeAudioClip([a0, a2.set_start(a0.end + 0.50),
                                        a3.set_start(a0.end + 0.50 + a2.end + 0.50),
                                        a4.set_start(a0.end + 0.50 + a2.end + 0.50 + a3.end + 0.50),
                                        a5.set_start(a0.end + 0.50 + a2.end + 0.50 + a3.end + a4.end + 0.50),
                                        outro.set_start(a0.end + 0.50 + a2.end + 0.50 + a3.end + a4.end + 0.50 + a5.end + 1.50)])



    subclip = clip.set_duration(mixed.duration + 3)
    subclip.audio = mixed
    subclip.fps = 24

    subclip.write_videofile("f" + str(i) + ".mp4")
    os.system("ffmpeg -i f" + str(i) + ".mp4 -vf scale=1080:1920 nm" + str(i) + ".mp4")