from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am an Telegram YB Groups Music bot [🎶](https://telegra.ph/file/ae4fecebac9d00089adf9.jpg) 
        I let you play music in your group's voice chat.

Bot Maintained By @YogeshBots 
⚠️You must Join our channel in order to use me😇

The commands I currently support are:

/play - 🎶 Play the replied audio file or YouTube video 
/pause - ▶️ Pause the audio stream 
/resume - ⏸ Resume the audio stream 
/skip - ↪️ Skip the current audio stream
/mute - 🔇 Mute the userbot
/unmute - 🔊 Unmute the userbot
/stop - 🗑🛑 Clear the queue and remove the userbot from the call
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Subscribe", url="https://bit.ly/3ezKasi"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/YogeshBots"
                    )
                ]
            ]
        )
    )
