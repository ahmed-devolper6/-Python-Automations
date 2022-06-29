from ntpath import realpath
import os
from posixpath import dirname
import shutil
print(''''
    Weclome the script is for 
    clean up ur falies (audio,videos,img,apps)
    Take to code on dir u want to clean up
    and the script take all ur files and clean up
''')
corrent = os.path.dirname(os.path.realpath(__file__))
for failename in os.listdir(corrent):
    #script of img clean up 
    if failename.endswith((".jpg" , "png")):
        
        if not os.path.exists('images'):
            os.mkdir('images')
        shutil.copy(failename, 'images')
        os.remove(failename)
        print(f"{failename}: done")
#script of video clean up 
    if failename.endswith((".webm" , ".mkv" , ".flv" , "mp4")):
        if not os.path.exists('videos'):
            os.mkdir('videos')
        shutil.copy(failename, 'videos')
        os.remove(failename)
        print(f"{failename}: done")
#script of video clean up 
    if failename.endswith((".webm" , ".mkv" , ".flv" , ".mp4")):
        if not os.path.exists('videos'):
            os.mkdir('videos')
        shutil.copy(failename, 'videos')
        os.remove(failename)
        print(f"{failename}: done")
#script of apps clean up 
    if failename.endswith((".exe" )):
        if not os.path.exists('apps'):
            os.mkdir('apps')
        shutil.copy(failename, 'apps')
        os.remove(failename)
        print(f"{failename}: done")
#script of audio clean up 
    if failename.endswith(("mp3")):
        if not os.path.exists('audio'):
            os.mkdir('audio')
        shutil.copy(failename, 'audio')
        os.remove(failename)
        print(f"{failename}: done")
#script of audio clean up 
    if failename.endswith((".zip" , ".rar")):
        if not os.path.exists('archivers'):
            os.mkdir('archivers')
        shutil.copy(failename, 'archivers')
        os.remove(failename)
        print(f"{failename}: done")
#script of code clean up 
    if failename.endswith((".py" , ".js" , ".html" , ".css" ,)):
        if not os.path.exists('code'):
            os.mkdir('code')
        shutil.copy(failename, 'code')
        os.remove(failename)
        print(f"{failename}: done")
