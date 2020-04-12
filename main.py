import os
import pandas as pd #Used to read csv file or reads data from a dataframe
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gtts

def textToSpeech(text,filename):
    '''It will spit out the given 'filename' amd wil speak given 'text' '''
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=False)#Converts text written in the excel file to speech
    myobj.save(filename)#Saves the speech in the specified file

def mergeAudios(audios):
    '''This function returns pydub audio segment '''
    combined=AudioSegment.empty()# Makes an empty audio file
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)#Accumulates smaller chunks to integrate into a larger
    return combined    

def generateSkeleton():
    '''It will generate pieces from the given file and then stitch them according to us'''
    audio=AudioSegment.from_mp3('announcement.mp3')#Converts mp3 file to python object

    #1.Generate -Kripya dhyaan dijiye
    start=88000
    finish=90200
    audioProcessed=audio[start:finish]
    audioProcessed.export('1_hindi.mp3',format='mp3')

    #2.Generate -from city 

    #3.Generate -se chalkar
    start=91000
    finish=92200
    audioProcessed=audio[start:finish]#Breaks the audio accordingly
    audioProcessed.export('3_hindi.mp3',format='mp3')#Converts python object to mp3 file

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
    for index,item in df.iterrows():
        #2.Generate -from city 
        textToSpeech(item['from'],'2_hindi.mp3')
        #4.Generate -via city
        textToSpeech(item['via'],'4_hindi.mp3')
        #6.Generate -to city
        textToSpeech(item['to'],'6_hindi.mp3')
        #8.Generate -train no. and name
        textToSpeech(item['train_no']+' '+item['train_name'],'8_hindi.mp3')
        #10.Generate -platform no.
        textToSpeech(item['platform'],'10_hindi.mp3')

        audios=[f'{i}_hindi.mp3' for i in range(1,12)]
        announcement=mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format='mp3')

if __name__ == "__main__":
    
    print('Generating skeleton...')
    generateSkeleton()
    print('Now generating announcement...')
    generateAnnouncement('announce_hindi.xlsx')