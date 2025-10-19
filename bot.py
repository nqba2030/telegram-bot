from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً! 👋 أنا بوتك الجديد، كيف أقدر أساعدك؟")

# أمر /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "الأوامر المتاحة:\n"
        "/start - بدء المحادثة\n"
        "/help - عرض المساعدة\n"
        "أرسل لي أي رسالة وسأكررها لك!"
    )

# رد تلقائي على أي رسالة نصية
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"أنت قلت: {user_message}")

# تشغيل التطبيق
app = ApplicationBuilder().token("8222360770:AAHR8UiJsyTtaNhVFtOo-8GRaHmWg7dWBko").build()

# ربط الأوامر
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("✅ البوت يعمل الآن... انتقل إلى تيليجرام وجرب /help أو أرسل رسالة عادية")

# تشغيل البوت
app.run_polling()
