# -*- coding: utf-8 -*-
"""
Телеграм-бот «Генератор открыток».
Собирает имя / текст / подпись / тему и выдаёт готовую ссылку-открытку
с превью, QR-кодом и кнопкой «Поделиться».

Хостинг Pella: entry-файл = main.py, токен в Environment как BOT_TOKEN.
Локально: установи BOT_TOKEN и запусти `python main.py`. Подробнее — README.md.
"""
import os
import time
from urllib.parse import quote

import telebot
from telebot import types

BASE_URL = "https://zxcursed667.github.io/proekt1/card/gen.html"
QR_API = "https://api.qrserver.com/v1/create-qr-code/?size=400x400&margin=12&data="
SHOT_API = "https://image.thum.io/get/width/720/crop/980/"
PREVIEW_FALLBACK = "https://zxcursed667.github.io/proekt1/card/preview.png"
REPO_URL = "https://github.com/zxcursed667/proekt1"

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise SystemExit("Не задан BOT_TOKEN. Добавь его в Environment на Pella. См. README.md")

bot = telebot.TeleBot(TOKEN)

# Временное хранилище данных по чату
sessions = {}

THEMES = {
    "pink": "Розовая 💗",
    "sunny": "Солнечная ☀️",
    "night": "Ночная 🌙",
    "mint": "Мятная 🌿",
    "ocean": "Морская 🌊",
    "gold": "Золотая ✨",
}


def build_url(d, preview=False):
    parts = ["to=" + quote(d.get("to", "")), "msg=" + quote(d.get("msg", ""))]
    if d.get("from"):
        parts.append("from=" + quote(d["from"]))
    parts.append("theme=" + quote(d.get("theme", "pink")))
    if preview:
        parts.append("open=1")
    return BASE_URL + "?" + "&".join(parts)


@bot.message_handler(commands=["start"])
def cmd_start(m):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🎨 Создать открытку")
    bot.send_message(
        m.chat.id,
        "Привет! 👋 Я соберу красивую интерактивную открытку и дам ссылку, превью и QR-код, "
        "которые можно отправить кому угодно. Нажми кнопку, чтобы начать.",
        reply_markup=kb,
    )


@bot.message_handler(commands=["about"])
def cmd_about(m):
    bot.send_message(
        m.chat.id,
        "🎀 *Генератор открыток*\n\n"
        "Собираю персональную анимированную открытку и отдаю ссылку, превью и QR-код.\n"
        "Открытка работает без бэкенда — всё кодируется прямо в адресе.\n\n"
        "Стек: Python + pyTelegramBotAPI, HTML/CSS/JS, GitHub Pages.\n"
        "Код: " + REPO_URL + "\n\nНачать — /start",
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )


@bot.message_handler(func=lambda m: m.text == "🎨 Создать открытку")
def ask_to(m):
    bot.send_message(
        m.chat.id,
        "Кому открытка? Напиши имя в родительном падеже (напр. «Ангелины»).",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    bot.register_next_step_handler(m, get_to)


def get_to(m):
    sessions[m.chat.id] = {"to": (m.text or "").strip()[:40]}
    bot.send_message(m.chat.id, "Отлично! Теперь напиши текст пожелания ✍️")
    bot.register_next_step_handler(m, get_msg)


def get_msg(m):
    sessions.setdefault(m.chat.id, {})["msg"] = (m.text or "").strip()[:300]
    bot.send_message(m.chat.id, "От кого подпись? (или отправь «-», чтобы без подписи)")
    bot.register_next_step_handler(m, get_from)


def get_from(m):
    frm = (m.text or "").strip()
    sessions.setdefault(m.chat.id, {})["from"] = "" if frm == "-" else frm[:40]
    kb = types.InlineKeyboardMarkup(row_width=2)
    btns = [types.InlineKeyboardButton(label, callback_data="theme:" + key)
            for key, label in THEMES.items()]
    kb.add(*btns)
    bot.send_message(m.chat.id, "Выбери оформление:", reply_markup=kb)


@bot.callback_query_handler(func=lambda c: c.data.startswith("theme:"))
def choose_theme(c):
    theme = c.data.split(":", 1)[1]
    d = sessions.get(c.message.chat.id)
    if not d:
        bot.answer_callback_query(c.id, "Сессия истекла, начни заново: /start")
        return
    d["theme"] = theme
    url = build_url(d)
    bot.answer_callback_query(c.id, "Готово!")

    share = "https://t.me/share/url?url=" + quote(url) + "&text=" + quote("Тебе открытка ❤")
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🎁 Открыть открытку", url=url))
    kb.add(types.InlineKeyboardButton("📤 Поделиться", url=share))

    # 1) Превью самой открытки (скриншот живой страницы; при сбое — запасная картинка)
    shot = SHOT_API + build_url(d, preview=True)
    try:
        bot.send_photo(c.message.chat.id, shot,
                       caption="Вот как выглядит твоя открытка 👇", reply_markup=kb)
    except Exception:
        bot.send_photo(c.message.chat.id, PREVIEW_FALLBACK,
                       caption="Твоя открытка готова 👇", reply_markup=kb)

    # 2) QR-код + ссылка
    qr = QR_API + quote(url)
    bot.send_photo(c.message.chat.id, qr,
                   caption="QR-код 📷 наведи камеру — или скопируй ссылку:\n" + url)

    bot.send_message(c.message.chat.id, "Создать ещё одну — /start")
    sessions.pop(c.message.chat.id, None)


def setup_commands():
    try:
        bot.set_my_commands([
            types.BotCommand("start", "Создать открытку 🎨"),
            types.BotCommand("about", "О боте ℹ️"),
        ])
    except Exception as e:
        print("Не удалось установить меню команд:", e)


if __name__ == "__main__":
    print("Бот запущен.")
    setup_commands()
    # Устойчивый polling: при сетевых ошибках бот сам перезапускается
    while True:
        try:
            bot.infinity_polling(skip_pending=True, timeout=30)
        except Exception as e:
            print("Ошибка polling, перезапуск через 5с:", e)
            time.sleep(5)
