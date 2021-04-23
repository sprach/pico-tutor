# Raspberry Pi Pico tutorial


# PyCharm

## MicroPython 플러인 설치
pycharm 실행
Plugins > Marketplace > 검색란에 'micropython' > 'Install' 버튼 클릭으로 설치

## New pico project
Project > New Project
Location: <프로젝트 위치 지정>
Python interpreter: New Virtualenv environment
New environment using: Virtualenv
Location: <앞서 지정한 프로젝트 Location>\venv
Base interpreter: <Python 3.x 설치 디렉토리>\python.exe
'Create' 버튼 클릭

## Raspberry Pi Pico Micropython Development Environment Settings
File > Settings
Languages ??& Frameworks > MicroPython 확장 > Enable MicroPython support 체크
Device type: Pyboard

아래 둘 중 하나
(1) Auto-detect detect path 체크
(2) Auto-detect detect path 체크 해제후 Device path: 해당 COM 포트 지정 (ex: COM7)
