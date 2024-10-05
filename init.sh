#!/bin/bash

# Установка системных зависимостей
apt-get update && apt-get install -y libgl1-mesa-glx
Flask
opencv-contrib-python-headless
ultralytics
libc6
# Запуск приложения
python3 app.py
