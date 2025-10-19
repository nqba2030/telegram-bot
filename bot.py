from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "ضع_توكن_البوت_هنا"

async def start(update: Update, context):
    await update.message.reply_text("مرحبًا! 👋 أنا البوت جاهز للعمل.")

async def help_command(update: Update, context):
    await update.message.reply_text("أرسل أي رسالة لأكررها لك.")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
