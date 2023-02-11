import frappe
from frappe_telegram import (Updater, Update, CallbackContext, CommandHandler, MessageFilter, MessageHandler, Filters)


class Filter(MessageFilter):
    def filter(self, message):
        return 'start' == str(message.text).strip().lower() or "/start" in message.text

handler_filter = Filter()

def setup(telegram_bot, updater: Updater):
    updater.dispatcher.add_handler(MessageHandler(handler_filter, start_handler))


def start_handler(update: Update, context: CallbackContext):
    if frappe.get_hooks("telegram_start_handler"):
        return frappe.get_attr(frappe.get_hooks("telegram_start_handler")[-1])(
            update=update, context=context
        )

    if frappe.session.user == "Guest":
        # Auth Handler will have kicked in and will not reach here
        return
    # msg = """
    # <b>bold</b>, <strong>bold</strong>
    # <i>italic</i>, <em>italic</em>
    # <u>underline</u>, <ins>underline</ins>
    # <s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
    # <span class="tg-spoiler">spoiler</span>
    # <b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
    # """
    update.effective_chat.send_message(frappe._("Welcome!"))#, parse_mode="HTML")
    update.effective_chat.send_message(
        frappe._("You are logged in as: {0}").format(
            frappe.bold(frappe.db.get_value("User", frappe.session.user, "full_name"))), parse_mode="HTML")

