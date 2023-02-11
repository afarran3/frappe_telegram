import frappe
from frappe_telegram import (Updater, Update, CallbackContext, CommandHandler, MessageFilter, MessageHandler, Filters)


class Filter(MessageFilter):
    def filter(self, message):
        return 'help' == str(message.text).strip().lower() or "/help" in message.text

handler_filter = Filter()

msg = "Hello!\n\n"
msg += "I'm here to help you get ERP Notifications.\n"
msg += "Please send 'start' to begin your registeration\n\n"


def setup(telegram_bot, updater: Updater):
    updater.dispatcher.add_handler(MessageHandler(handler_filter, help_handler))


def help_handler(update: Update, context: CallbackContext):
    if frappe.get_hooks("telegram_help_handler"):
        return frappe.get_attr(frappe.get_hooks("telegram_help_handler")[-1])(
            update=update, context=context
        )

    update.message.reply_text(msg, reply_to_message_id=update.message.message_id)
   
