# Используем базовый образ Python
FROM python:3.9-slim

# Указываем рабочую директорию
WORKDIR /usr/src/app

# Копируем файлы с зависимостями
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы бота
COPY . .

# Указываем переменную окружения для токена бота
ENV TELEGRAM_API_TOKEN=6576414245:AAG5zlrj0tl_LxJhEnvFTb92VJqauC-m2Z0

# Запускаем бота
CMD ["python", "./bot.py"]
