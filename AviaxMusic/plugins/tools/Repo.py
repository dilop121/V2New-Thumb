from AviaxMusic import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaVideo

repo_button = InlineKeyboardButton("• ʀᴇᴘᴏ •", callback_data="my_source")
close_button = InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")

@app.on_message(filters.command(["repo", "repolist", "repository"]))
def repo_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [repo_button, close_button]
    ])
    message.reply_text("ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴍᴀᴅᴀʀᴊᴀᴀᴛ!", reply_markup=keyboard)

@app.on_callback_query(filters.regex("my_source"))
async def my_repo_callback(_, callback_query: CallbackQuery):
    await callback_query.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup([[close_button]]),
    )
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://telegra.ph/file/8f06e45caf4959feb24f8.mp4")
    )
