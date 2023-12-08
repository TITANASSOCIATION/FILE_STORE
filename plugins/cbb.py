#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

UPGRADE = "HERE ARE THE PREMIUM PLANS"

PREMIUM1 = """⭐ TITAN COMMUNITY ⭐

💎 PREMIUM 1

[ 30/- Rs per Months💥]
──────────────
🎯 Oᥙr Pᥣᥲᥒ Sᥱrviᥴᥱ & Benefit 🎉
──────────────
 ├ ✅ NO ADS/LINKS ONLY FILES
 ├ ✅ NEW/OLD [MOVIES/SERIES] Channel 🎬
 ├ ✅ KOREAN/JAPANESE DRAMAS
 ├ ✅ MOVIES AND SERIES NEW/OLD
───────────────
Wannna buy this? sure click on buy now"""

PREMIUM2 = """⭐ TITAN COMMUNITY ⭐

💎 PREMIUM 2

[ 59/- Rs per Months💥]
──────────────
🎯 Oᥙr Pᥣᥲᥒ Sᥱrviᥴᥱ & Benefit 🎉
──────────────
 ├ ✅ NO ADS/LINKS ONLY FILES
 ├ ✅ NEW/OLD [MOVIES/SERIES] Channel 🎬
 ├ ✅ KOREAN/JAPANESE DRAMAS
 ├ ✅ MOVIES AND SERIES NEW/OLD
 ├ ✅ REQUEST GROUP [ONLY BOT] 
───────────────
Wannna buy this? sure click on buy now"""

PREMIUM3 = """⭐ TITAN COMMUNITY ⭐

💎 PREMIUM 3

[ 99/- Rs per Months💥]
──────────────
🎯 Oᥙr Pᥣᥲᥒ Sᥱrviᥴᥱ & Benefit 🎉
──────────────
 ├ ✅ NO ADS/LINKS ONLY FILES
 ├ ✅ NEW/OLD [MOVIES/SERIES] Channel 🎬
 ├ ✅ KOREAN/JAPANESE DRAMAS
 ├ ✅ MOVIES AND SERIES NEW/OLD
 ├ ✅ REQUEST GROUP [YOUR REQUEST WILL LOOKAFTER BY ADMINS]
───────────────
Wannna buy this? sure click on buy now"""

PREMIUM4 = """⭐ TITAN COMMUNITY ⭐

💎 PREMIUM 4

[ 149/- Rs per Months💥]
──────────────
🎯 Oᥙr Pᥣᥲᥒ Sᥱrviᥴᥱ & Benefit 🎉
──────────────
 ├ ✅ NO ADS/LINKS ONLY FILES
 ├ ✅ NEW/OLD [MOVIES/SERIES] Channel 🎬
 ├ ✅ KOREAN/JAPANESE DRAMAS
 ├ ✅ MOVIES AND SERIES NEW/OLD
 ├ ✅ MOVIES AND SERIES NEW/OLD
 ├ ✅ REQUEST GROUP [YOUR REQUEST WILL LOOKAFTER BY ADMINS]
 ├ ✅ 18+ CHANNEL [DAILY VIDEOS IN FILES]
───────────────
Wannna buy this? sure click on buy now"""

ABOUT_TXT = """<b>○ 𝖬𝗒 𝖭𝖺𝗆𝖾: {}
○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='https://t.me/piroxbots'>𝖳𝗁𝗂𝗌 𝖯𝖾𝗋𝗌𝗈𝗇</a>
○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥 
○ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖺𝗌𝗒𝗇𝖼𝗂𝗈 𝟢.𝟣𝟩.𝟣 
○ 𝖲𝖾𝗋𝗏𝖾𝗋 : Contabo
○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : <a href='https://www.mongodb.com'>𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝖥𝗋𝖾𝖾 𝖳𝗂𝖾𝗋</a>
○ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : v1.0.1 [BeTa]
○ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉 : <a href='https://t.me/raixchat'>𝖳𝖺𝗉 𝖧𝖾𝗋𝖾</a>"""

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "hey":
        await query.message.edit_text(
            text=f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n○ Channel : @CodeXBotz\n○ Support Group : @CodeXBotzSupport</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔒 Close", callback_data="close")]
                ]
            )
        )
    elif data == "premium":
        await query.message.edit_text(
            text=UPGRADE,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton('PREMIUM 1', callback_data='premium1'),
                    InlineKeyboardButton('PREMIUM 2', callback_data='premium2')
                ],
                [
                    InlineKeyboardButton('PREMKUM 3', callback_data='premium3'),
                    InlineKeyboardButton('PREMIUM 4', callback_data='premium4')
                ],
                [
                    InlineKeyboardButton('⛔ CLOSE ⛔', callback_data='start')
                ]
            ])
        )
    elif data == "premium1":
        await query.message.edit_text(
            text=PREMIUM1,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton('⛔ BACK TO MENU ⛔', callback_data='premium')
                ],
                [
                    InlineKeyboardButton('⛔ PAY HERE NOW !!! ⛔', callback_data='close')
                ]
            ])
        )
    elif data == "premium2":
        await query.message.edit_text(
            text=PREMIUM2,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton('⛔ BACK TO MENU ⛔', callback_data='premium')
                ],
                [
                    InlineKeyboardButton('⛔ PAY HERE NOW !!! ⛔', callback_data='close')
                ]
            ])
        )
    elif data == "premium3":
        await query.message.edit_text(
            text=PREMIUM3,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton('⛔ BACK TO MENU ⛔', callback_data='premium')
                ],
                [
                    InlineKeyboardButton('⛔ PAY HERE NOW !!! ⛔', callback_data='close')
                ]
            ])
        )
    elif data == "premium4":
        await query.message.edit_text(
            text=PREMIUM4,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton('⛔ BACK TO MENU ⛔', callback_data='premium')
                ],
                [
                    InlineKeyboardButton('⛔ PAY HERE NOW !!! ⛔', callback_data='close')
                ]
            ])
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton('⛔ BACK ⛔', callback_data='start')
                ]
            ])
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚂", url="https://t.me/Titan_Association"),
                        InlineKeyboardButton("𝙰𝙱𝙾𝚄𝚃", callback_data="about")
                    ],
                    [
                        InlineKeyboardButton("𝙱𝚄𝚈 𝙿𝚁𝙴𝙼𝙸𝚄𝙼 𝙽𝙾𝚆 !!!", callback_data="premium")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
