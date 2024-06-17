from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import pathlib
import textwrap
import google.generativeai as genai
import os
import uvicorn

genai.configure(api_key='AIzaSyDR5LnttOKA1QZWckv8gxrm8FRwOtkj9isAIzaSyDR5LnttOKA1QZWckv8gxrm8FRwOtkj9is')
model = genai.GenerativeModel('gemini-1.5-flash-latest')

import docx2txt

file_path = pathlib.Path('WA_chatbot.docx')
content = docx2txt.process(file_path)


TOKEN = '6766016859:AAH5CQ3MA5n9pPRUXlpcsWmBVtVg52e5ejo'
BOT_USERNAME = '@algooruBot'

# Define command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi there!👋I'm ready to answer your questions. Ask me anything!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a Test bot. Please type something so I can respond!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

# Define message handler
def handle_response(prompt:str) ->str:
    processed: str = prompt.lower()
    if prompt.lower() in ("hi", "hello", "hey"):  # Handle multiple greetings
        response = "How can I help you today? 😊"
    elif prompt.lower() in ("what is algooru","what services do you offer?","can you give me an overview of your platform","who do you serve?","what does your platform provide?","what are your services?"):
        response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
    elif prompt.lower() in ("where is alguru located","where is your headquarters?","where is your location?","where is your company?","where do you conduct sessions?","what are your services?"):
        response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
    elif prompt.lower() in ("how can i work with you?","how can i work with you"):
        response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
    elif prompt.lower() in ("is there a limit to the number of packages i'm allowed to have?","is there a limit to the number of packages i'm allowed to have"):
        response = "You can subscribe to multiple packages simultaneously, and our team will assist you with your request."
    elif prompt.lower() in ("how much do you charge for a session?","how much do you charge for a session"):
        response = "Our prices per hour range from 88 to 152 SAR, depending on your chosen package. Our experts will recommend a package that best fits your needs and preferences."

    else:
        response = "going in else"
        flag = model.generate_content(["If "+prompt+" is related to anything like LGBTQ+, mention of homosexuality, politics, war news, crimes, etc. return '1' else return '0'"])
        response = flag
        # st.write(flag.text)
        if '1' in str(flag.text):
            response = "I am a parenting and educational assistance bot. I am unable to answer these questions. Please ask questions related to educational assistance."
        elif '0' in str(flag.text):            
        # context_truncated = textwrap.shorten(content, width=1000)
            response1 = model.generate_content([
                "You are an expert customer assistant from AlGooru Team. I'll give you question and context and you'll return the answer.Answer in 60 words in a paragraph. Do not give random answers. ",
                f"Question: {prompt}",
                f"Context: {content}"
            ])
            response = f"{response1.text}"
        else:
            response = "I'm sorry, can you please try rephrasing your question?"
    return response


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    # Your message handling logic goes here
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # if message_type=='group':
    #     if BOT_USERNAME in text:
    #         new_text: str = text.replace(BOT_USERNAME,'').strip()
    #         response: str = handle_response(new_text)
    #     else:
    #         return
    # else:
    response:str=handle_response(text)
    print('BOT:',response)
    await update.message.reply_text(response)

    

# Define error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print('Starting bot ...')
    app = Application.builder().token(TOKEN).build()
    # HOST = os.getenv("HOST","0.0.0.0")
    # PORT = os.getenv("PORT",8080)
    # uvicorn.run(app,host=HOST,port = PORT)

    # Register command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Register error handler
    app.add_error_handler(error)

    # Start polling
    print("Polling...")
    app.run_polling(poll_interval=3)
