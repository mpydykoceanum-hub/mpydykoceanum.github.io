import ...


web_app = WebAppInfo(url="https://mpydykoceanum-hub.github.io/mpydykoceanum.github.io/")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Site", web_app=web_app)]
    ],
    resize_keyboard=True,
)

cb = CallbackData('btn', 'action')
key = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton('Pay', callback_data='btn:buy')]]
)