from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://te.legra.ph/file/2ed8a1ae8298a6d573acf-9f4d47a4c6854d4aa4.jpg",
        caption=f"""✦ » ʜᴇʏ  {msg.from_user.mention}  ✤,
✦ » ɪ ᴀᴍ {me2},

✦ » Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

✦ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [⎯꯭֯🖤⃪ ꯭⃛֯ ̶̲̽͟𓆩⃪ͥ͢ ᷟ𓆩𝙍𝘼𝘿𝙃𝙀 ⃪𝄀꯭𝄄꯭ا✾༐𓂃⃪꯭,, ㅤ ™](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="▪ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ▪️", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🔸 sᴜᴘᴘᴏʀᴛ🔸", url="https://t.me/BOT_SUPPORT_GROUP7"),
                    InlineKeyboardButton("▫️ ᴜᴘᴅᴀᴛᴇs▫️", url="https://t.me/ll_BOTCHAMBER_ll")
                ],
                [
                    InlineKeyboardButton("🔸 ᴀʀᴀᴅʜʏᴀ ᴍᴜsɪᴄ 🔸", url="https://t.me/ZEUS_MUSIC_ROBOT"),
                    InlineKeyboardButton("▫️ʀᴀᴅʜᴇ ᴍᴜsɪᴄ▫️", url="https://t.me/RADHE_MUSIC_ROBOT")
                ]                
            ]
        )
    )
