from decouple import config
import telepot
from telepot.loop import MessageLoop
import time
from unicodedata import normalize


def prepare_text(txt):
    bad_chars = '?!'
    txt = ''.join(character for character in txt if character not in bad_chars)
    txt = txt.strip()
    txt = txt.lower()
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if chat_type in ['group', 'supergroup'] and content_type == 'text':
        if prepare_text(msg['text']) == 'galvao':
            galvao_bot.sendMessage(chat_id, MSG_GALVAO)
            time.sleep(1)
            tino_bot.sendMessage(chat_id, MSG_TINO)


MSG_GALVAO = 'Fala, Tino!'
MSG_TINO = 'Sentiu!'
GALVAO_TOKEN = config('GALVAO_TOKEN')
TINO_TOKEN = config('TINO_TOKEN')
galvao_bot = telepot.Bot(GALVAO_TOKEN)
tino_bot = telepot.Bot(TINO_TOKEN)

MessageLoop(galvao_bot, handle).run_as_thread()
print('Listening...')

while 1:
    time.sleep(10)
