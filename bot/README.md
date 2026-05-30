# 🤖 Telegram-бот «Генератор открыток»

Бот спрашивает **кому / текст / подпись / тему** и выдаёт готовую ссылку-открытку,
которая открывается на сайте (`card/gen.html` на GitHub Pages).

## 1️⃣ Получить токен
1. Открой в Telegram **@BotFather**
2. Отправь `/newbot`, придумай имя и логин (заканчивается на `bot`)
3. Сохрани **токен** вида `123456789:AAE...`

## 2️⃣ Запуск локально (для теста и демо)
```bash
cd bot
pip install -r requirements.txt

# Windows (PowerShell):
$env:BOT_TOKEN="СЮДА_ТОКЕН"
python bot.py

# macOS / Linux:
export BOT_TOKEN="СЮДА_ТОКЕН"
python bot.py
```
Бот работает, пока запущена программа.

## 3️⃣ Бесплатный хостинг 24/7 (актуально на 2026)

⚠️ Важно: «вечно бесплатных» VPS почти не осталось (Fly.io / Railway / PythonAnywhere
урезали free). Ниже — реально рабочие варианты.

### ✅ Вариант A — спецхостинг для ботов (самый простой, без карты)
Платформы, заточенные под Telegram-боты, с бесплатным always-on:
- **Pella** — pella.app (поддерживает pyTelegramBotAPI, без карты)
- **JustRunMy.App** — justrunmy.app/telegram-bots

Шаги: зарегистрируйся → залей папку `bot/` → добавь секрет `BOT_TOKEN` → старт.

### ✅ Вариант B — Koyeb (бесплатный нано-инстанс)
1. koyeb.com → Create Service → из GitHub-репо
2. Run command: `python bot.py`
3. Environment → `BOT_TOKEN`
4. Инстанс `Free` → Deploy

### ✅ Вариант C — самый надёжный (нужна карта для верификации)
- **Oracle Cloud Always Free** — настоящий бесплатный VPS 24/7. Запуск через `screen` или `systemd`.

> Для портфолио достаточно Варианта A — быстро, бесплатно и без карты.

## 📄 Файлы
- `bot.py` — код бота (polling)
- `requirements.txt` — зависимости

## 🔗 Схема ссылки
```
https://zxcursed667.github.io/proekt1/card/gen.html?to=Имя&msg=Текст&from=Подпись&theme=pink
```
Темы: `pink`, `sunny`, `night`.
