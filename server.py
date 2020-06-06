import re
from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=6)
Previous_Date_Formatted = Previous_Date.strftime ('%d/%m/%y') # format the date to dd/mm/yy
pre_date = str(Previous_Date_Formatted)

f = open("WhatsApp Chat with s3 - whatsapp summary bot.txt", "r")

def make_reply(msg):
    reply = None
    if msg is not None:
        for x in f:
            if re.search("code",x):
                if re.search("^[0-9]",x):
                    reply = x[20:]
                    break
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = "some exception"
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
