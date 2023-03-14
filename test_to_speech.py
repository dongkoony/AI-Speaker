from gtts import gTTS
from playsound import playsound

# 영어 문장
# text = 'hello'
audio_file = 'sample.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# # 한글 문장
# text = '테스트'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(audio_file)
# playsound(audio_file) # .mp3 파일 재생

# 긴 문장 (파일 불러와서 처리)
with open('sample.txt', 'r', encoding='utf8') as f:
  text = f.read()
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(audio_file)
playsound(audio_file) # .mp3 파일 재생