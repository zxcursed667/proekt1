# -*- coding: utf-8 -*-
"""
Телеграм-бот «Генератор открыток».
Собирает имя / текст / подпись / тему и выдаёт готовую ссылку-открытку.

Хостинг Pella: entry-файл = main.py, токен задаётся в Environment как BOT_TOKEN.
Локально: установи BOT_TOKEN и запусти `python main.py`.
Подробнее — в README.md.
"""
import os
import time
from urllib.parse import quote

import telebot
from telebot import types

# Базовый адрес страницы-открытки на GitHub Pages
BASE_URL = "https://zxcursed667.github.io/proekt1/card/gen.html"

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise SystemExit("Не задан BOT_TOKEN. Добавь его в Environment на Pella или в переменную окружения. См. README.md")

bot = telebot.TeleBot(TOKEN)

# Временное хранилище данных по чату
sessions = {}

THEMES = {
    "pink": "Розовая 💗",
    "sunny": "Солнечная ☀️",
    "night": "Ночная 🌙",
}


def build_url(d):
    parts = ["to=" + quote(d.get("to", "")), "msg=" + quote(d.get("msg", ""))]
    if d.get("from"):
        parts.append("from=" + quote(d["from"]))
    parts.append("theme=" + quote(d.get("theme", "pink")))
    return BASE_URL + "?" + "&".join(parts)


@bot.message_handler(commands=["start", "help"])
def cmd_start(m):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🎨 Создать открытку")
    bot.send_message(
        m.chat.id,
        "Привет! 👋 Я соберу красивую интерактивную открытку и дам ссылку, "
        "которую можно отправить кому угодно. Нажми кнопку, чтобы начать.",
        reply_markup=kb,
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
    kb = types.InlineKeyboardMarkup()
    for key, label in THEMES.items():
        kb.add(types.InlineKeyboardButton(label, callback_data="theme:" + key))
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
    bot.send_message(
        c.message.chat.id,
        "Твоя открытка готова! 🎉\n\n" + url + "\n\nПросто перешли эту ссылку тому, кому она предназначена ❤\n\nСоздать ещё одну — /start",
        disable_web_page_preview=False,
    )


if __name__ == "__main__":
    print("Бот запущен.")
    # Устойчивый polling: при сетевых ошибках бот сам перезапускается (важно на хостинге)
    while True:
        try:
            bot.infinity_polling(skip_pending=True, timeout=30)
        except Exception as e:
            print("Ошибка polling, перезапуск через 5с:", e)
            time.sleep(5)
