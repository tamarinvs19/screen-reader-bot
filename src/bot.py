import logging
import time
import requests

from telegram import Update, ForceReply, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater

import config as cfg
import main
import get_answer as mod_get_answer


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

button_j = KeyboardButton('j')
greet_kb = ReplyKeyboardMarkup([[button_j]], True)

def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=greet_kb,
    )


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("""
    Commands:
    /help          : this help
    /start         : say hello
    /j <or> 0 <text>      : find text in all questions and return answers
    /a <or> 9 <text>      : find text in all answers and return answers
    /inf           : run an infinity checking screens and sending here
    /channal       : run an infinity checking screens and sending to the channal
    /up <px>       : up the top parsing line
    /down <px>     : down the top parsing line
    /reset         : reset parsing line
    /ll            : move left the left parsing line
    /lr            : move right the left parsing line
    /rl            : move left the right parsing line
    /rr            : move right the right parsing line
    /resetlr       : reset the left and the right lines
    <another text> : found screens on this computer and retrun answers
    """)


def echo(update: Update, _: CallbackContext) -> None:
    answers = main.main()
    send_info(answers, update.message.reply_text)


def get_answer(update: Update, context: CallbackContext) -> None:
    answers = mod_get_answer.get_answer(context.args[0])
    send_info(answers, update.message.reply_text)


def find_answer(update: Update, context: CallbackContext) -> None:
    answers = mod_get_answer.get_answer(' '.join(context.args))
    send_info(answers, update.message.reply_text)


def run_infty_autoscaning(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Activated infty scaninig mode')
    while True:
        answers = main.main()
        send_info(answers, update.message.reply_text)
        time.sleep(cfg.DELAY)


def autosending_to_channal(update: Update, context: CallbackContext):
    update.message.reply_text('Activated infty scaninig mode for channal')
    while True:
        answers = main.main()
        send_info(answers, send_telegram)


def send_telegram(text: str):
    url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
    x = requests.get(url.format(cfg.TOKEN, cfg.CHANNEL_ID, text))


def send_info(answers: list[dict], sender):
    if len(answers) < cfg.MAX_MESSAGE_COUNT:
        for answer in answers:
            sender(
                '__Question__: {} \n\n__Answer__: {}'.
                format(str(answer['question']), str(answer['answer'])),
                reply_markup=greet_kb,
                )


def up_line(update: Update, context: CallbackContext) -> None:
    cfg.CROP_TOP -= int(context.args[0])
    update.message.reply_text(
        'CROP_TOP = {0}'.format(cfg.CROP_TOP),
        reply_markup=greet_kb,
    )


def down_line(update: Update, context: CallbackContext) -> None:
    cfg.CROP_TOP += int(context.args[0])
    update.message.reply_text(
        'CROP_TOP = {0}'.format(cfg.CROP_TOP),
        reply_markup=greet_kb,
    )


def left_left_line(update: Update, context: CallbackContext) -> None:
    cfg.CROP_LEFT -= int(context.args[0])
    update.message.reply_text(
        'CROP_LEFT = {0}'.format(cfg.CROP_LEFT),
        reply_markup=greet_kb,
    )


def left_right_line(update: Update, context: CallbackContext) -> None:
    cfg.CROP_LEFT += int(context.args[0])
    update.message.reply_text(
        'CROP_LEFT = {0}'.format(cfg.CROP_LEFT),
        reply_markup=greet_kb,
    )


def right_left_line(update: Update, context: CallbackContext) -> None:
    cfg.CROP_RIGHT -= int(context.args[0])
    update.message.reply_text(
        'CROP_RIGHT = {0}'.format(cfg.CROP_RIGHT),
        reply_markup=greet_kb,
    )


def right_right_line(update: Update, context: CallbackContext) -> None:
    cfg.CROP_LEFT += int(context.args[0])
    update.message.reply_text(
        'CROP_RIGHT = {0}'.format(cfg.CROP_RIGHT),
        reply_markup=greet_kb,
    )


def reset(update: Update, context: CallbackContext) -> None:
    cfg.CROP_TOP = cfg.DEFAULT_CROP_TOP
    update.message.reply_text(
        'CROP_TOP = {0}'.format(cfg.CROP_TOP),
        reply_markup=greet_kb,
    )

def reset_left_right(update: Update, context: CallbackContext) -> None:
    cfg.CROP_LEFT = cfg.DEFAULT_CROP_LEFT
    cfg.CROP_RIGHT = cfg.DEFAULT_CROP_RIGHT
    update.message.reply_text(
        'CROP_LEFT = {0}\nCROP_RIGHT'.format(cfg.CROP_LEFT, cfg.CROP_RIGHT),
        reply_markup=greet_kb,
    )


def main_bot() -> None:
    """Start the bot."""
    updater = Updater(cfg.TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("inf", run_infty_autoscaning))
    dispatcher.add_handler(
        CommandHandler("inf_channal", autosending_to_channal)
    )
    dispatcher.add_handler(CommandHandler("up", up_line))
    dispatcher.add_handler(CommandHandler("down", down_line))
    dispatcher.add_handler(CommandHandler("reset", reset))
    dispatcher.add_handler(CommandHandler("ll", left_left_line))
    dispatcher.add_handler(CommandHandler("lr", left_right_line))
    dispatcher.add_handler(CommandHandler("rl", left_left_line))
    dispatcher.add_handler(CommandHandler("rr", left_right_line))
    dispatcher.add_handler(CommandHandler("resetlr", reset_left_right))
    dispatcher.add_handler(CommandHandler("j", get_answer))
    dispatcher.add_handler(CommandHandler("a", find_answer))
    dispatcher.add_handler(CommandHandler("0", get_answer))
    dispatcher.add_handler(CommandHandler("9", find_answer))
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, echo)
    )

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main_bot()
