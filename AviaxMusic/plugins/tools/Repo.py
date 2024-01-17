from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AviaxMusic import app

@app.on_message(filters.command("repo"))
def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("ʀᴇᴘᴏ❥", callback_data='repo_callback')]
    ])

    message.reply_text("ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴍᴀᴅᴀʀᴊᴀᴀᴛ ᴛᴏ sᴇᴇ ᴛʜᴇ ʀᴇᴘᴏ!", reply_markup=keyboard)

@app.on_callback_query(filters.regex(r'^repo_callback'))
def handle_repo_callback(client, callback_query):
    user_id = callback_query.from_user.id
    video_file = "https://graph.org/file/52b2315b843584a3c4532.mp4"

    try:
        client.send_video(
            chat_id=user_id,
            video=video_file,
            reply_to_message_id=callback_query.message.message_id
        )
    except Exception as e:
        print(f"Error sending video: {e}")
