#!/bin/bash

# Установка системных зависимостей
apt-get update && apt-get install -y libgl1-mesa-glx

# Запуск приложения
python3 app.py
