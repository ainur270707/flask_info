#!/bin/bash

# Установка системных зависимостей
apt-get update && apt-get install -r requirements.txt
Flask
opencv-contrib-python-headless
ultralytics
libc6
# Запуск приложения
python3 app.py
