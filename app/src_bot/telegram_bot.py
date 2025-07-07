import telegram.ext
from .auth import TOKEN, CHAT_ID


def send_message(text_message:str) -> None:
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    updater.bot.send_message(chat_id=CHAT_ID, text=text_message)

if __name__ == '__main__':
    send_message('TEST TEST')