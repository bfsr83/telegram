from telegram.ext import Updater
from config.auth import token
if __name__ == '__main__':
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('david_borges_bot')
