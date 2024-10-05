#!/bin/bash

# Установка системных зависимостей
apt-get update && apt-get install -y libc6  # Установка системных пакетов

# Установка Python-зависимостей
pip install -r requirements.txt  # Установка зависимостей из requirements.txt

# Запуск приложения
python3 app.py  # Запуск вашего приложения
