# 🤖 Telegram-бот «Генератор открыток» — хостинг на Pella

Бот спрашивает **кому / текст / подпись / тему** и выдаёт готовую ссылку-открытку,
которая открывается на сайте (`card/gen.html` на GitHub Pages).

**Стек:** Python 3 + pyTelegramBotAPI • entry-файл `main.py` • хостинг [Pella](https://www.pella.app) (бесплатно, без карты).

---

## 1️⃣ Получить токен бота
1. Открой в Telegram **@BotFather**
2. Отправь `/newbot` → придумай имя и логин (заканчивается на `bot`)
3. Скопируй **токен** вида `123456789:AAE...` — он понадобится на шаге 4

## 2️⃣ Зарегистрироваться на Pella
1. Зайди на **https://www.pella.app** → *Sign up* (можно через Discord/Google, карта не нужна)
2. В панели нажми **Create / New Server** → выбери **Telegram Bot** → **Python**

## 3️⃣ Залить код (2 способа)

**Способ А — из GitHub (рекомендую для портфолио):**
- Выбери *Import from GitHub* → репозиторий `zxcursed667/proekt1`
- В настройках укажи **папку бота**: `bot`
- **Main file:** `main.py`

**Способ Б — загрузка файлов:**
- Выбери *File Upload* и загрузи содержимое папки `bot/` (файлы `main.py` и `requirements.txt`)

> В обоих случаях Pella сама выполнит `pip install -r requirements.txt`.

## 4️⃣ Добавить токен в Environment
1. Открой вкладку **Environment / Secrets** своего сервера на Pella
2. Добавь переменную:
   - **Key:** `BOT_TOKEN`
   - **Value:** токен от @BotFather
3. Сохрани. ⚠️ Токен никогда не пиши прямо в коде и не коммить в GitHub.

## 5️⃣ Запустить
1. Убедись, что **Start / Run command** = `python main.py` (или просто Main file = `main.py`)
2. Нажми **Start** → в логах появится `Бот запущен.`
3. Открой бота в Telegram и отправь `/start` ✅

---

## ⚠️ Важно про бесплатный план Pella
Бесплатный контейнер может **засыпать / останавливаться** при неактивности — иногда нужно зайти
в панель и нажать **Start** снова. Для портфолио этого хватает. Если нужен
жёсткий 24/7 — см. Koyeb или Oracle Cloud Always Free в общем README.

## 🖥️ Локальный запуск (для теста)
```bash
cd bot
pip install -r requirements.txt

# Windows (PowerShell):
$env:BOT_TOKEN="СЮДА_ТОКЕН"
python main.py

# macOS / Linux:
export BOT_TOKEN="СЮДА_ТОКЕН"
python main.py
```

## 📄 Файлы
- `main.py` — код бота (polling с автоперезапуском)
- `requirements.txt` — зависимости

## 🔗 Схема ссылки
```
https://zxcursed667.github.io/proekt1/card/gen.html?to=Имя&msg=Текст&from=Подпись&theme=pink
```
Темы: `pink`, `sunny`, `night`.
