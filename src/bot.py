#!/usr/bin/env python
# -- coding: utf-8 -- –

import logging
import time
import requests

import main
import get_answer as mod_get_answer

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = ''

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, _: CallbackContext) -> None:
    info = main.main()
    if len(info) < 15:
        for data in info:
            update.message.reply_text('__Question__: {} \n\n__Answer__: {}'.format(str(data['question']), str(data['answer'])))


def get_answer(update: Update, context: CallbackContext) -> None:
    info = mod_get_answer.get_answer(context.args[0])
    if len(info) < 15:
        for data in info:
            update.message.reply_text('__Question__: {} \n\n__Answer__: {}'.format(str(data['question']), str(data['answer'])))

def inf_echo(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('OK')
    while True:
        info = main.main()
        for data in info:
            update.message.reply_text('__Question__: {} \n\n__Answer__: {}'.format(str(data['question']), str(data['answer'])))
        time.sleep(15)


def main_bot() -> None:
    """Start the bot."""
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("run_inf", inf_echo))
    dispatcher.add_handler(CommandHandler("j", get_answer))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main_bot()
