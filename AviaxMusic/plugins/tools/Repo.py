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
    message.reply_text("ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴍᴀᴅᴀʀᴊᴀᴀᴛ ᴛᴏ sᴇᴇ ᴛʜᴇ ʀᴇᴘᴏ!", reply_markup=keyboard)

@app.on_callback_query(filters.regex("my_source"))
async def my_repo_callback(_, callback_query: CallbackQuery):
    try:
        await callback_query.answer()
        await callback_query.edit_message_media(
            media=InputMediaVideo("https://graph.org/file/52b2315b843584a3c4532.mp4"),
            reply_markup=InlineKeyboardMarkup([[close_button]]),
        )
    except Exception as e:
        print(f"Error editing message media: {e}")

