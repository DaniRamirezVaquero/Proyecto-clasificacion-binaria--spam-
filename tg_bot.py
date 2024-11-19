import logging
import joblib
import re
import os
from langdetect import detect
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token del bot desde las variables de entorno
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Cargar los modelos y vectorizadores
model_en = joblib.load('./joblib/best_model_en.joblib')
vectorizer_en = joblib.load('./joblib/vectorizer_en.joblib')
model_es = joblib.load('./joblib/best_model_es.joblib')
vectorizer_es = joblib.load('./joblib/vectorizer_es.joblib')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

def detect_language(text):
    try:
        lang = detect(text)
        return lang  # 'en' para inglés, 'es' para español
    except:
        return 'unknown'

def preprocess_text(text):
    # Convertir a minúsculas
    text = text.lower()
    # Eliminar signos de puntuación y caracteres especiales
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def predict_spam(message):
    # Preprocesar el mensaje
    message = preprocess_text(message)

    # Detectar el idioma del mensaje
    language = detect_language(message)

    # Seleccionar el modelo y el vectorizador según el idioma
    if language == 'en':
        message_vec = vectorizer_en.transform([message])  # Aplicar vectorizador en inglés
        prediction = model_en.predict(message_vec)  # Usar el modelo en inglés
    elif language == 'es':
        message_vec = vectorizer_es.transform([message])  # Aplicar vectorizador en español
        prediction = model_es.predict(message_vec)  # Usar el modelo en español
    else:
        prediction = ["unknown"]  # Devolver un mensaje claro si no se detecta el idioma

    return prediction[0]  # Retorna la predicción (0 para ham, 1 para spam)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages and delete if spam."""
    message = update.message.text
    user = update.effective_user

    if predict_spam(message) == 'spam':
        await update.message.delete()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"⚠️ @{user.username}, he borrado tu mensaje de spam, cuidaito'."
        )
    else:
        await update.message.reply_text("Tu mensaje no es spam.")

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - handle the message
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()