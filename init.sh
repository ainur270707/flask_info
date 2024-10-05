#!/bin/bash

set -e  # Завершить скрипт при ошибке

# Обновление списка пакетов и установка системных зависимостей
apt-get update && apt-get install -y libc6

# Установка Python-зависимостей
pip install --no-cache-dir -r requirements.txt
