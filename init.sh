#!/bin/bash

set -e  # Завершить скрипт при ошибке

echo "Начало выполнения init.sh"

echo "Активация виртуального окружения..."
source /opt/venv/bin/activate

echo "Установка Python-зависимостей из requirements.txt..."
pip install --no-cache-dir -r requirements.txt

echo "init.sh выполнен успешно."
