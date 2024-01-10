# AI-Speaker

## 현 프로젝트의  목표
```
AI-Speaker 프로젝트의 주요 목표는 AWS EC2 Ubuntu 환경에서 작동하는, 
Chat-GPT API 기반의 인공지능 스피커를 개발하는 것입니다. 이 프로젝트는 다음과 같은 특정 기술 요소들을 포함합니다

1. Python 기반 개발: Python 3.10을 사용하여 AI 스피커 애플리케이션을 개발합니다.

2. 필요한 라이브러리 설치
- openai: Chat-GPT API 활용을 위한 설치.
- gTTS (Google Text-to-Speech): 텍스트를 음성으로 변환.
- playsound 1.2.2: 사운드 재생을 위해 1.3.0에서 1.2.2로 다운그레이드하여 사용 (버그 대응).
- Pyaudio: 오디오 인터페이스를 위한 라이브러리.
- SpeechRecognition: 음성 인식 기능을 위한 라이브러리.

3. 환경 설정 및 해결 방안
- EC2 Ubuntu 환경에서 사운드카드 문제 해결을 위해 alsa-base 및 pulseaudio 설치.
- Pyaudio 관련 에러 발생 시, portaudio 설치를 통한 문제 해결.
- Python ALSA 라이브러리(pyalsa) 설치.

4. 컨테이너화 및 배포:
- Docker를 사용하여 AI 스피커 애플리케이션을 컨테이너화.
- CI/CD 파이프라인을 통해 Docker 컨테이너를 Kubernetes 클러스터로 배포.

5. 최종 목표
- 효율적인 개발과 배포 프로세스를 통해, 안정적이고 확장 가능한 AI 스피커 서비스 구축.
- 사용자의 음성 명령을 인식하고, 적절한 응답을 생성하여 음성으로 전달하는 기능 구현.

```

## python version 
```
python3.10
```

## pip3 install
```
pip3 install openai # Chat-GPT API 사용 하기 위한 설치
```

```
pip3 install gTTS
```
```
pip3 install playsound==1.2.2 # 버그로 인한 1.3.0 -> 1.2.2 다운그레이드
```
```
pip3 install Pyaudio
```
##### Pyaudio error시 portaudio 설치
```
pip3 install SpeechRecognition
```

ec2 ubuntu 환경 내 사운드카드 없음. 인풋 아웃풋 불가능.
```
$ sudo apt-get install alsa-base pulseaudio
```

##### pyalsa install
```
[pip3 install SpeechRecognition](https://www.alsa-project.org/files/pub/pyalsa/)
```

