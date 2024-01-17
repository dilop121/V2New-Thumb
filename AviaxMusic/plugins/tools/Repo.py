
from AviaxMusic import app
from pyrogram import Client, filters
from pyrogram.types import InputMediaVideo, InlineKeyboardMarkup, InlineKeyboardButton


close_button = InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")

@app.on_message(filters.command("repo"))
def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("ʀᴇᴘᴏ❥", callback_data='repo_calls')]
    ])

    message.reply_markup = keyboard

@app.on_callback_query(filters.regex("repo_calls"))
async def gib_repo_callback(_, callback_query):
    media_url = "https://graph.org/file/52b2315b843584a3c4532.mp4"

    await callback_query.edit_message_media(
        media=InputMediaVideo(media_url),
        reply_markup=InlineKeyboardMarkup([[close_button]])
    )
