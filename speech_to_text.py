import pyaudio
import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
  print('듣고 있습니다.')
  audio = r.listen(source) # 마이크로 부터 음성 인풋
  
try:
  # 영어
  # # Google API >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  # text = r.recognize_google(audio, language='en-US')
  # # Google API >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  # print(text)
  
  # 한국어
  text = r.recognize_google(audio, language='ko')
  print(text)
except sr.UnknownValueError:
  print('음성 인식 실패.') # 음성 인식 실패한 경우 출력
except sr.RequestError as e:
  print('요청 실패 : {0}'.format(e)) # API Key 오류, 네트워크 확인