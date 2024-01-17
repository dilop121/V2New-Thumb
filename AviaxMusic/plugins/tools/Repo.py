from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaVideo
from AviaxMusic import app

@app.on_message(filters.command("repo") & filters.group)
async def help_group(client: Client, message: Message):
    video_url = "https://telegra.ph/file/3ae24ed057b2bcc03ca55.mp4"
    await message.reply_video(
        video=video_url,
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=video_url)
                ]
            ]
        ),
    )

@app.on_message(filters.command("repo") & filters.private)
async def help_private(client: Client, message: Message):
    video_url = "https://telegra.ph/file/3ae24ed057b2bcc03ca55.mp4"
    await message.reply_video(
        video=video_url,
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=video_url)
                ]
            ]
        ),
    )
