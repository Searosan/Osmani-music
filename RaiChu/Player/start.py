
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from RaiChu.config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("Asbuuc", 60 * 60 * 24 * 7),
    ("Malinta", 60 ** 2 * 24),
    ("Saca", 60 ** 2),
    ("Daqiiqada", 60),
    ("Mirirka", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/02e51c229a2867e13c21e.jpg",
        caption=f"""**👋Salama'Aniga Waxaan Ahay 𝙊𝙨𝙢𝙖𝙣𝙞 𝘽𝙤𝙩 Botkaan 
        Waxa aad gashan kartaa Oo ku isticmaali kartaa Group kaaga.!.....
😎  Real bot owner [Ribaj](t.me/ribajosmani)
Powered By [Ribaj Global](t.me/meribaj) ...
**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✪𝗦𝗮𝗺𝗲𝘆𝗮𝗵𝗮✪", url="https://t.me/meribaj"
                    ),
                    InlineKeyboardButton(
                        "❓ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗟𝗶𝘀𝘁 ❓", url="https://telegra.ph/%F0%9D%99%8A%F0%9D%99%A8%F0%9D%99%A2%F0%9D%99%96%F0%9D%99%A3%F0%9D%99%9E-%F0%9D%98%BD%F0%9D%99%A4%F0%9D%99%A9-02-19"
                    )
                  ],[
                    InlineKeyboardButton(
                       " 🇸🇴 𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/osmanigroupbot"
                    ),
                    InlineKeyboardButton(
                        "𝗖𝗵𝗮𝗻𝗻𝗲𝗹 📢", url="https://t.me/osmanibots"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ 𝗔𝗱𝗱 𝗢𝘀𝗺𝗮𝗻𝗶𝗣𝗹𝗮𝘆𝗲𝗿 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
