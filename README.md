﻿# Телеграм-бот 'эхо' 💬 🧞
<p align="center">
      <h2>Телеграмм бот, повторяющий текст за пользователем (библиотека: telebot, Python)</h2>
</p>

<p align="center">
   <img width = "70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/telegram/telegram.png" alt="Unity Version">
   <img width = "70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="Unity Version">
</p>

# О проекте 🖥️

Сейчас расскажу, как я реализовал телеграмм бота, который 'создает эхо' для введенного пользователем текста 

Процесс создания:
### 1. Создаем токен для бота в Botfather (для запуска бота) 
### 2. В Python файле импортируем нужную библиотеку: 
###
-telebot (для настройки бота)
### 3. После программме нужно передать токен для бота (чтобы мы могли запустить его в телеграмме)
### 4. Создаем несколько функций и объявляем для них декоратор @bot.message_handler. В нем задается основной функционал бота

# Документация 📕 (откуда брал материал для разработки)

Официальная документация - https://pypi.org/project/pyTelegramBotAPI/

Статья на хабре - https://habr.com/ru/articles/580408/
