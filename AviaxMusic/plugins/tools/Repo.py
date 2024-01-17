
from AviaxMusic import app
from pyrogram import Client, filters
from pyrogram.types import InputMediaVideo, InlineKeyboardMarkup, InlineKeyboardButton


repo_button = InlineKeyboardButton("• ʀᴇᴘᴏ •", callback_data="my_source")
close_button = InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")

@app.on_message(filters.command("repo"))
def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [repo_button, close_button]
    ])
    message.reply_text("ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴍᴀᴅᴀʀᴊᴀᴀᴛ ᴛᴏ sᴇᴇ ᴛʜᴇ ʀᴇᴘᴏ!", reply_markup=keyboard)

@app.on_message(filters.text & ~filters.command)
def echo_message(client, message):
    message.reply_text(message.text)

@app.on_callback_query(filters.regex("my_source"))
async def my_repo_callback(_, callback_query):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://graph.org/file/52b2315b843584a3c4532.mp4", has_spoiler=True),
        reply_markup=InlineKeyboardMarkup([[close_button]]),
    )


