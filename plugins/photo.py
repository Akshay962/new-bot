from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters


@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="π‘πππππ", callback_data="bright"),
                        InlineKeyboardButton(text="π¬πππΎπ½", callback_data="mix"),
                        InlineKeyboardButton(text="π‘ & πΆ", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="π’πππΌππΎ", callback_data="circle"),
                        InlineKeyboardButton(text="π‘πππ", callback_data="blur"),
                        InlineKeyboardButton(text="π‘πππ½πΎπ", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="π²πππΌππΎπ", callback_data="stick"),
                        InlineKeyboardButton(text="π±πππΊππΎ", callback_data="rotate"),
                        InlineKeyboardButton(text="π’πππππΊππ", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="π²πΎπππΊ", callback_data="sepia"),
                        InlineKeyboardButton(text="π―πΎππΌππ", callback_data="pencil"),
                        InlineKeyboardButton(text="π’πΊπππππ", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="π¨πππΎππ", callback_data="inverted"),
                        InlineKeyboardButton(text="π¦ππππΌπ", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="π±πΎππππΎ π‘π¦", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="π’ππππΎ", callback_data="close_data"),
                    ],
                ]
            ),
            reply_to_message_id=message.id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text(f"{e} \nSomething went wrong!", quote=True)
            except Exception:
                return
