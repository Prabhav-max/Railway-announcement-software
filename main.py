import os
import pandas as pd #Used to read csv file
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gtts

def textToSpeech(text,filename):
    '''It will spit out the given 'filename' amd wil speak given 'text' '''
    pass

def mergeAudios(audios):
    '''This function returns pydub audio segment '''
    pass

def generateSkeleton():
    '''It will generate pieces from the given file and then stitch them according to us'''
    audio=AudioSegment.from_mp3('announcement.mp3')

    #1.Generate -Kripya dhyaan dijiye
    start=88000
    finish=90200
    audioProcessed=audio[start:finish]
    audioProcessed.export('1_hindi.mp3',format='mp3')

    #2.Generate -from city 

    #3.Generate -se chalkar
    start=91000
    finish=92200
    audioProcessed=audio[start:finish]
    audioProcessed.export('3_hindi.mp3',format='mp3')
    #4.Generate -via city

    #5.Generate -ke raste
    start=94000
    finish=95000
    audioProcessed=audio[start:finish]
    audioProcessed.export('5_hindi.mp3',format='mp3')

    #6.Generate -to city

    #7.Generate -ko jane wali gaadi sankhya
    start=96000
    finish=98900
    audioProcessed=audio[start:finish]
    audioProcessed.export('7_hindi.mp3',format='mp3')

    #8.Generate  -train no. and name

    #9.Generate -kuch hi samay me platform sankhya
    start=105500
    finish=108200
    audioProcessed=audio[start:finish]
    audioProcessed.export('9_hindi.mp3',format='mp3')

    #10.Generate -platform no.

    #11.Generate -par aa rhi hai
    start=109000
    finish=112250
    audioProcessed=audio[start:finish]
    audioProcessed.export('11_hindi.mp3',format='mp3')



def generateAnnouncement(filename):
    '''It will take an excel file and will generate an announcement from that'''
    df=pd.read_excel(filename)
    print(df)

if __name__ == "__main__":
    
    print('Generating skeleton...')
    generateSkeleton()
    print('Skeleton generated')
    print('Now generating announcement...')
    generateAnnouncement('announce_hindi.xlsx')