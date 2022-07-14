import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def english_textToSpeech(text,filename):
    mytext=str(text)
    language = "en"
    myobj=gTTS(text=mytext , lang=language , slow=True)
    myobj.save(filename)

def hindi_textToSpeech(text,filename):
    mytext=str(text)
    language = "hi"
    myobj=gTTS(text=mytext , lang=language , slow=True)
    myobj.save(filename)
def mergeAudios(audio1,audio2):
    combined=AudioSegment.empty()
    for audio in audio1:
        combined +=AudioSegment.from_mp3(audio)
    for audio in audio2:
        combined +=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio=AudioSegment.from_mp3('railway.mp3')


    # 1 - Generate kripya dheyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")
#******************English***********************************************
    # 12 may i have your attention please train no
    start=66000
    finish=70000
    audioProcessed=audio[start:finish]
    audioProcessed.export("12_english.mp3", format="mp3")
    
    # 14 from
    start=76500
    finish=77000
    audioProcessed=audio[start:finish]
    audioProcessed.export("14_english.mp3", format="mp3")
    # 16 to
    start=78000
    finish=78500
    audioProcessed=audio[start:finish]
    audioProcessed.export("16_english.mp3", format="mp3")
    # 18 via
    start=80000
    finish=80900
    audioProcessed=audio[start:finish]
    audioProcessed.export("18_english.mp3", format="mp3")
    # 20 arriving shortly from platform no
    start=82500
    finish=86500
    audioProcessed=audio[start:finish]
    audioProcessed.export("20_english.mp3",format="mp3")  

   

def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():

        # 2 - Generate from-city
         hindi_textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via-city
         hindi_textToSpeech(item['via'], '4_hindi.mp3')

        # 6 - Generate to-city
         hindi_textToSpeech(item['to'], '6_hindi.mp3')

        # 8 - Generate train no and name
         hindi_textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10 - Generate platform number
         hindi_textToSpeech(item['platform'], '10_hindi.mp3')
        # 13 train no and name
         english_textToSpeech(item['train_no'] + " " + item['train_name'],'13_english.mp3')
        #  15 from city
         english_textToSpeech(item['from'],'15_english.mp3')
        #17 to city
         english_textToSpeech(item['to'],'17_english.mp3')
        # 19 via city
         english_textToSpeech(item['via'],'19_english.mp3')
         # 21 platform number
         english_textToSpeech(item['platform'],'21_english.mp3')

        
        
         audio1 = [f"{i}_hindi.mp3" for i in range(1,12)]
         audio2=  [f"{i}_english.mp3" for i in range(12,22)]
         announcement = mergeAudios(audio1,audio2)
         announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__ == "__main__":
    print("Generating skeleton")
    generateSkeleton()
    print("Now generating announcement")
    generateAnnouncement("announce_hindi.xlsx")

