# 🤖 Telegram-бот «Генератор открыток» — хостинг на Pella

Бот спрашивает **кому / текст / подпись / тему** и выдаёт:
- 🔗 готовую ссылку-открытку (`card/gen.html` на GitHub Pages)
- 🖨️ превью самой открытки картинкой
- 📷 QR-код на ссылку
- 📤 кнопки «Открыть» и «Поделиться»

**Стек:** Python 3 + pyTelegramBotAPI • entry-файл `main.py` • хостинг [Pella](https://www.pella.app) (бесплатно, без карты).

## ⌨️ Команды
- `/start` — создать открытку
- `/about` — о боте и ссылка на код

Меню команд устанавливается автоматически при запуске (`set_my_commands`).

---

## 1️⃣ Получить токен бота
1. Открой в Telegram **@BotFather**
2. Отправь `/newbot` → придумай имя и логин (заканчивается на `bot`)
3. Скопируй **токен** вида `123456789:AAE...`

## 2️⃣ Зарегистрироваться на Pella
1. **https://www.pella.app** → *Sign up* (карта не нужна)
2. **Create / New Server** → **Telegram Bot** → **Python**

## 3️⃣ Залить код
**Способ А — из GitHub (рекомендую):** *Import from GitHub* → `zxcursed667/proekt1` → папка `bot`, main file `main.py`.

**Способ Б — загрузка:** *File Upload* → файлы `main.py` и `requirements.txt` из папки `bot/`.

> Pella сама выполнит `pip install -r requirements.txt`.

## 4️⃣ Добавить токен в Environment
Вкладка **Environment / Secrets** → добавь:
- **Key:** `BOT_TOKEN`
- **Value:** токен от @BotFather

⚠️ Токен никогда не пиши в коде и не коммить в GitHub.

## 5️⃣ Запустить
1. **Start / Run command** = `python main.py`
2. **Start** → в логах `Бот запущен.`
3. Открой бота в Telegram и отправь `/start` ✅

---

## 🎨 Оформление бота в @BotFather (для портфолио)
- `/setdescription` — текст на экране до старта:
  > Собираю красивые персональные открытки и даю ссылку, превью и QR-код. Нажми /start 🎨
- `/setabouttext` — коротко в профиле:
  > Генератор интерактивных открыток • пет-проект
- `/setuserpic` — поставь аватарку (напр. `card/preview.png` или стикер)

## ⚠️ Про бесплатный план Pella
Бесплатный контейнер может засыпать при простое — иногда нужно нажать **Start** снова.
Для портфолио этого хватает. Жёсткий 24/7 — см. Koyeb / Oracle Cloud в общем README.

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

## 🔗 Схема ссылки
```
https://zxcursed667.github.io/proekt1/card/gen.html?to=Имя&msg=Текст&from=Подпись&theme=pink
```
Темы: `pink`, `sunny`, `night`, `mint`, `ocean`, `gold`. Параметр `&open=1` — режим превью (без анимации).
