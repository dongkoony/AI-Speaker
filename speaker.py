import time, os
import speech_recognition as sr
import openai

from gtts import gTTS
from playsound import playsound
from pyaudio import PyAudio

# Chat GPT API Key
openai.api_key = ("챗 gpt API 키 넣는 자리")

# 음성 인식(Listen, STT)
def listen(recognizer, audio):
  try:
    text = recognizer.recognize_google(audio, language='ko')
    print('[사용자]' + text) 
    answer(text)
  except sr.UnknownValueError:
    print('음성 인식 실패.') # 음성 인식 실패한 경우 출력
  except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) # API Key 오류, 네트워크 확인

def answer(input_text):
    answer_text = ''
    
# AI-Speacker 호출
    if '안녕' in input_text:
      answer_text = '안녕하세요. 반갑습니다.'
    elif '종료' in input_text:
      answer_text = '도움 필요하시면 말씀하세요.'
      stop_listening(wait_for_stop=False) # 백그라운드 아웃
    else:
      answer_text = '다시 한 번 말씀해 주시겠어요?'
    speak(answer_text)


# Chat-GPT Answer
def answer(input_text):
    prompt = f"Q: {input_text}\nA:"
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()
    speak(message)

# TEST Answer
# def answer(input_text):
#     answer_text = ''
    
    
#     if '안녕' in input_text:
#       answer_text = '안녕하세요. 반갑습니다.'
    
#     # 테스트 예제 출력 문구 #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#     # elif '날씨' in input_text:
#     #   answer_text = '오늘의 서울 기온은 10도 이며, 맑은 하늘이 예상 됩니다.'
#     # elif '환율' in input_text:
#     #   answer_text = '원 달러 환율은 1300원 입니다.'
#     # elif '고마워' in input_text:
#     #   answer_text = '별 말씀을요.'
#     # 테스트 예제 출력 문구 #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
#     elif '종료' in input_text:
#       answer_text = '도움 필요하시면 말씀하세요.'
#       stop_listening(wait_for_stop=False) # 백그라운드 아웃
#     else:
#       answer_text = '다시 한 번 말씀해 주시겠어요?'
#     speak(answer_text)

# 읽기(TTS)
def speak(text):
  print('[인공지능]' + text)
  file_name = 'voice.mp3'
  tts = gTTS(text=text, lang='ko')
  tts.save(file_name)
  playsound(file_name)
  
r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)


while True:
  time.sleep(0.1)