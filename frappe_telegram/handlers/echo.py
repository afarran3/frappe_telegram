import frappe
from frappe_telegram import (Updater, Update, CallbackContext, CommandHandler, MessageHandler, Filters)


def setup(telegram_bot, updater: Updater):
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


def echo(update: Update, context: CallbackContext):
    if frappe.get_hooks("telegram_echo_handler"):
        return frappe.get_attr(frappe.get_hooks("telegram_echo_handler")[-1])(
            update=update, context=context
        )

    update.message.reply_text(update.message.text)
