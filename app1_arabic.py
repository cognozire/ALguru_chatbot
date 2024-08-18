# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# import pathlib
# import textwrap
# import google.generativeai as genai
# import uvicorn
# import os





# genai.configure(api_key='AIzaSyCBkKSe9dtzeQCVW5Of07_QyngJAGONtlQ')

# model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

# import docx2txt

# file_path = pathlib.Path('WA_chatbot.docx')
# content = docx2txt.process(file_path)


# TOKEN = '6766016859:AAH5CQ3MA5n9pPRUXlpcsWmBVtVg52e5ejo'
# BOT_USERNAME = '@algooruBot'

# # Define command handlers
# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hi there!👋I'm ready to answer your questions. Ask me anything!")

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("I am a Test bot. Please type something so I can respond!")

# async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("This is a custom command!")

# # Define message handler
# def handle_response(prompt:str) ->str:
#     processed: str = prompt.lower()
#     if prompt.lower() in ("hi", "hello", "hey"):  # Handle multiple greetings
#         response = "How can I help you today?😊"
#     elif prompt.lower() in ("what is algooru","what services do you offer?","can you give me an overview of your platform","who do you serve?","what does your platform provide?","what are your services?"):
#         response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
#     elif prompt.lower() in ("where is alguru located","where is your headquarters?","where is your location?","where is your company?","where do you conduct sessions?","what are your services?"):
#         response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
#     elif prompt.lower() in ("how can i work with you?","how can i work with you"):
#         response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
#     elif prompt.lower() in ("is there a limit to the number of packages i'm allowed to have?","is there a limit to the number of packages i'm allowed to have"):
#         response = "You can subscribe to multiple packages simultaneously, and our team will assist you with your request."
#     elif prompt.lower() in ("how much do you charge for a session?","how much do you charge for a session"):
#         response = "Our prices per hour range from 88 to 152 SAR, depending on your chosen package. Our experts will recommend a package that best fits your needs and preferences."

#     else:
#         flag = model.generate_content(["If "+prompt+" is related to anything like LGBTQ+, mention of homosexuality, politics, war news, crimes, etc. return '1' else return '0'"])
#         # st.write(flag.text)
#         if '1' in str(flag.text):
#             response = "I am a parenting and educational assistance bot. I am unable to answer these questions. Please ask questions related to educational assistance."
#         elif '0' in str(flag.text):            
#         # context_truncated = textwrap.shorten(content, width=1000)
#             response1 = model.generate_content([
#                 "You are an expert customer assistant from AlGooru Team. I'll give you question and context and you'll return the answer.Answer in 60 words in a paragraph. Do not give random answers. ",
#                 f"Question: {prompt}",
#                 f"Context: {content}"
#             ])
#             response = f"{response1.text}"
#         else:
#             response = "I'm sorry, can you please try rephrasing your question?"
#     return response


# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text
#     # Your message handling logic goes here
#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

#     # if message_type=='group':
#     #     if BOT_USERNAME in text:
#     #         new_text: str = text.replace(BOT_USERNAME,'').strip()
#     #         response: str = handle_response(new_text)
#     #     else:
#     #         return
#     # else:
#     response:str=handle_response(text)
#     print('BOT:',response)
#     await update.message.reply_text(response)

    

# # Define error handler
# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f"Update {update} caused error {context.error}")

# if __name__ == '__main__':
#     print('Starting bot ...')
#     app = Application.builder().token(TOKEN).build()
#     HOST = os.getenv("HOST","0.0.0.0")
#     PORT = os.getenv("PORT",8080)
#     uvicorn.run(app,host=HOST,port = PORT)
    
#     # Register command handlers
#     app.add_handler(CommandHandler('start', start_command))
#     app.add_handler(CommandHandler('help', help_command))
#     app.add_handler(CommandHandler('custom', custom_command))

#     # Register message handler
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))

#     # Register error handler
#     app.add_error_handler(error)

#     # Start polling
#     print("Polling...")
#     app.run_polling(poll_interval=3)


# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# import pathlib
# import textwrap
# import google.generativeai as genai
# import os
# import uvicorn
# import asyncio
# import time

# genai.configure(api_key='AIzaSyDR5LnttOKA1QZWckv8gxrm8FRwOtkj9isAIzaSyDR5LnttOKA1QZWckv8gxrm8FRwOtkj9is')
# model = genai.GenerativeModel('gemini-1.5-flash-latest')

# import docx2txt

# file_path = pathlib.Path('WA_chatbot.docx')
# content = docx2txt.process(file_path)


# TOKEN = '6766016859:AAH5CQ3MA5n9pPRUXlpcsWmBVtVg52e5ejo'
# BOT_USERNAME = '@algooruBot'

# # Cache and cache expiry time in seconds (e.g., 3600 seconds = 1 hour)
# cache = {}
# cache_expiry = 3600

# # Function to clear cache
# async def clear_cache():
#     while True:
#         await asyncio.sleep(cache_expiry)
#         cache.clear()
#         print("Cache cleared")

# # Define command handlers
# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hi there!👋I'm ready to answer your questions. Ask me anything!")

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("I am a Test bot. Please type something so I can respond!")

# async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("This is a custom command!")

# # Define message handler
# def handle_response(prompt: str) -> str:
#     # Check cache first
#     if prompt in cache:
#         return cache[prompt]
    
#     processed: str = prompt.lower()
#     if prompt.lower() in ("hi", "hello", "hey"):  # Handle multiple greetings
#         response = "How can I help you today?😊"
#     elif prompt.lower() in ("what is algooru","what services do you offer?","can you give me an overview of your platform","who do you serve?","what does your platform provide?","what are your services?"):
#         response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
#     elif prompt.lower() in ("where is alguru located","where is your headquarters?","where is your location?","where is your company?","where do you conduct sessions?","what are your services?"):
#         response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
#     elif prompt.lower() in ("how can i work with you?","how can i work with you"):
#         response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
#     elif prompt.lower() in ("is there a limit to the number of packages i'm allowed to have?","is there a limit to the number of packages i'm allowed to have"):
#         response = "You can subscribe to multiple packages simultaneously, and our team will assist you with your request."
#     elif prompt.lower() in ("how much do you charge for a session?","how much do you charge for a session"):
#         response = "Our prices per hour range from 88 to 152 SAR, depending on your chosen package. Our experts will recommend a package that best fits your needs and preferences."

#     else:
#         flag = model.generate_content(["If "+prompt+" is related to anything like LGBTQ+, mention of homosexuality, politics, war news, crimes, etc. return '1' else return '0'"])
#         # st.write(flag.text)
#         if '1' in str(flag.text):
#             response = "I am a parenting and educational assistance bot. I am unable to answer these questions. Please ask questions related to educational assistance."
#         elif '0' in str(flag.text):            
#         # context_truncated = textwrap.shorten(content, width=1000)
#             response1 = model.generate_content([
#                 "You are an expert customer assistant from AlGooru Team. I'll give you question and context and you'll return the answer.Answer in 60 words in a paragraph. Do not give random answers. ",
#                 f"Question: {prompt}",
#                 f"Context: {content}"
#             ])
#             response = f"{response1.text}"
#         else:
#             response = "I'm sorry, can you please try rephrasing your question?"

#     # Cache the response
#     cache[prompt] = response

#     return response


# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text
#     # Your message handling logic goes here
#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

#     # if message_type=='group':
#     #     if BOT_USERNAME in text:
#     #         new_text: str = text.replace(BOT_USERNAME,'').strip()
#     #         response: str = handle_response(new_text)
#     #     else:
#     #         return
#     # else:
#     response:str=handle_response(text)
#     print('BOT:',response)
#     await update.message.reply_text(response)

    

# # Define error handler
# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f"Update {update} caused error {context.error}")

# if __name__ == '__main__':
#     print('Starting bot ...')
#     app = Application.builder().token(TOKEN).build()
#     # HOST = os.getenv("HOST","0.0.0.0")
#     # PORT = os.getenv("PORT",8080)
#     # uvicorn.run(app,host=HOST,port = PORT)

#     # Register command handlers
#     app.add_handler(CommandHandler('start', start_command))
#     app.add_handler(CommandHandler('help', help_command))
#     app.add_handler(CommandHandler('custom', custom_command))

#     # Register message handler
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))

#     # Register error handler
#     app.add_error_handler(error)

#     # Start cache clearing loop
#     app.job_queue.run_repeating(lambda _: asyncio.create_task(clear_cache()), interval=cache_expiry)

#     # Start polling
#     print("Polling...")
#     app.run_polling()


import streamlit as st
import pathlib
import textwrap
import google.generativeai as genai

genai.configure(api_key='AIzaSyCBkKSe9dtzeQCVW5Of07_QyngJAGONtlQ')

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
safe = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_LOW_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_LOW_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_LOW_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_LOW_AND_ABOVE",
    },
]

import docx2txt

file_path = pathlib.Path('WA_chatbot_arabic.docx')
content = docx2txt.process(file_path)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("system"):
    st.write("""
هلا والله👋 معك بوت القورو، كيف أقدر اخدمك اليوم؟
""")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("أدخل استفسارك باللغة العربية."):
    with st.chat_message("user"):
        st.markdown(prompt)


    # ما هو "الجوّرو"؟
    st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt.lower() in ("مرحبا ", "مرحبا ", "هاي "):  # Handle multiple greetings
        response = "كيف أقدر أساعدك اليوم؟"
    elif prompt.lower() in ("ما هو الغورو","ما هي الخدمات التي تقدمها؟","هل يمكن أن تعطيني لمحة عامة عن النظام الأساسي الخاص بك","من تخدم؟","ماذا توفر منصتك؟","ما هي خدماتك؟"):
        response = "AlGooru هي منصة تعليمية تربط أولياء الأمور والطلاب بمعلمين مؤهلين ومدققين، وتقدم جلسات شخصية وعبر الإنترنت في 20 موضوعًا أساسيًا تغطي جميع المستويات التعليمية، إلى جانب بعض المجالات الجامعية والمهنية."
    elif prompt.lower() in ("أين يقع ألغورو","أين يقع مقرك؟","أين موقعك؟","أين شركتك ؟","أين تجري الجلسات؟","ما هي خدماتك؟"):
        response = "AlGooru هي منصة تعليمية تربط أولياء الأمور والطلاب بمعلمين مؤهلين ومدققين، وتقدم جلسات شخصية وعبر الإنترنت في 20 موضوعًا أساسيًا تغطي جميع المستويات التعليمية، إلى جانب بعض المجالات الجامعية والمهنية."
    elif prompt.lower() in ("كيف يمكنني العمل معك؟","كيف يمكنني العمل معك"):
        response = "AlGooru هي منصة تعليمية تربط أولياء الأمور والطلاب بمعلمين مؤهلين ومدققين، وتقدم جلسات شخصية وعبر الإنترنت في 20 موضوعًا أساسيًا تغطي جميع المستويات التعليمية، إلى جانب بعض المجالات الجامعية والمهنية."
    elif prompt.lower() in ("هل هناك حد لعدد الحزم المسموح لي بالحصول عليها؟","هل هناك حد لعدد الحزم المسموح لي بالحصول عليها؟"):
        response = "يمكنك الاشتراك في باقات متعددة في وقت واحد، وسيقوم فريقنا بمساعدتك في تلبية طلبك."
    elif prompt.lower() in ("كم تتقاضى مقابل الجلسة؟","كم تتقاضى مقابل الجلسة"):
        response = "تتراوح أسعارنا للساعة من 88 إلى 152 ريال سعودي، حسب الباقة التي اخترتها. سيوصي خبراؤنا بالحزمة التي تناسب احتياجاتك وتفضيلاتك."

    else:
        try:
             response1 = model.generate_content([
                "You are an expert customer assistant from AlGooru Team. I'll give you question and context and you'll return the answer.Answer in 60 words in a paragraph. Do not give random answers. Always answer in arabic language ",
                f"Question: {prompt}",
                f"Context: {content}"
            ],safety_settings=safe)
             response = f"{response1.text}"
        except:
            response = "آسف السؤال ليس ذات صلة! من فضلك حاول طرح سؤال آخر"
            # st.write("Sorry the question is not relevent! Please try asking another question")
    
         
        # flag = model.generate_content(["If "+prompt+" is related to anything like LGBTQ+, mention of homosexuality, politics, war news, crimes, etc. return '1' else return '0'"], safety_settings='HARM_CATEGORY_HATE_SPEECH')
        # flag = model.generate_content([prompt+"إذا كان مرتبطًا بأي شيء مثل LGBTQ+، أو ذكر المثلية الجنسية، أو السياسة، أو أخبار الحرب، أو الجرائم، وما إلى ذلك. قم بإرجاع 1 وإلا قم بإرجاع 0"])
        # # st.write(flag.text)
        # if '1' in str(flag.text):
        #     response = "I am a parenting and educational assistance bot. I am unable to answer these questions. Please ask questions related to educational assistance."
        # elif '0' in str(flag.text):            
        # # context_truncated = textwrap.shorten(content, width=1000)
        #     response1 = model.generate_content([
        #         "You are an expert customer assistant from AlGooru Team. I'll give you question and context and you'll return the answer.Answer in 60 words in a paragraph. Do not give random answers. Always answer in arabic language ",
        #         f"Question: {prompt}",
        #         f"Context: {content}"
        #     ])
        #     response = f"{response1.text}"
        # else:
            # st.write(str(flag.text))
            # response = "I'm sorry, can you please try rephrasing your question?"

    # st.write(response)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
