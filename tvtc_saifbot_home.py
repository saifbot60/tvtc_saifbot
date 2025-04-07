
import telebot

TOKEN = "8129207692:AAFATXlT3c6s-WWHd1oeVIw2gsjIzJlmzcY"
bot = telebot.TeleBot(TOKEN)

user_states = {}

reference_data = {
    "63118": {
        "المقرر": "حاسب 101",
        "اسم المقرر": "مقدمات تطبيقات الحاسب",
        "اسم المدرب": "نواف الوسيدي الحربي",
        "المبنى": "مبنى الدراسات العامة",
        "القاعة": "1890200000",
        "اليوم": "الأحد",
        "الوقت": "11:50 - 13:30"
    },
    "63116": {
        "المقرر": "حاسب 101",
        "اسم المقرر": "مقدمات تطبيقات الحاسب",
        "اسم المدرب": "نواف الوسيدي الحربي",
        "المبنى": "مبنى الدراسات العامة",
        "القاعة": "1890200000",
        "اليوم": "الأربعاء",
        "الوقت": "09:00 - 10:40"
    }
}

@bot.message_handler(func=lambda message: message.text.lower() == "ابدأ")
def start_conversation(message):
    user_states[message.chat.id] = "waiting_for_reference"
    bot.reply_to(message, "مرحبًا بك!\nمن فضلك أدخل الرقم المرجعي (رقم الشعبة).")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    text = message.text.strip()

    if user_states.get(user_id) == "waiting_for_reference":
        if text in reference_data:
            data = reference_data[text]
            response = (
                f"رقم الشعبة: {text}\n"
                f"المقرر: {data['المقرر']}\n"
                f"اسم المقرر: {data['اسم المقرر']}\n"
                f"اسم المدرب: {data['اسم المدرب']}\n"
                f"المبنى: {data['المبنى']}\n"
                f"القاعة: {data['القاعة']}\n"
                f"اليوم: {data['اليوم']}\n"
                f"الوقت: {data['الوقت']}"
            )
        else:
            response = "عذرًا، لم أجد معلومات لهذه الشعبة. تأكد من الرقم."
        user_states.pop(user_id)
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "أرسل كلمة 'ابدأ' لبدء المحادثة.")

print("البوت يعمل الآن...")
bot.polling()
