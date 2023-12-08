import os
import random
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user

help_text = """#HELP_NEEDED

Opps someone want your help here are the details!!
the user id of the #user  = {user_id}
the user name is of the user = {username}
the first name of the user = {user}
the last name of the user = {last}"""

PICS = [
    "https://telegra.ph/file/057d2ac31007228da3b8d.jpg",
    "https://telegra.ph/file/68576f8c8f3b4b9192348.jpg",
    "https://telegra.ph/file/39b11b9b63d2a4973f923.jpg",
    "https://telegra.ph/file/70573a3245aa860bf5fcc.jpg",
]

BANNED_USERS = {6409842915}

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id

    if id in BANNED_USERS:
        await message.reply_text("Sorry, you are banned.")
        return
        
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.edit_text("[■□□□□□□□□□] 10%")
        await asyncio.sleep(1)
        await temp_msg.edit_text("[■■□□□□□□□□] 20%")
        await asyncio.sleep(1)
        await temp_msg.edit_text("[■■■□□□□□□□] 30%")
        await asyncio.sleep(1)
        await temp_msg.edit_text("[■■■■□□□□□□] 40%")
        await asyncio.sleep(1)
        await temp_msg.edit_text("[■■■■■□□□□□] 50%")
        await asyncio.sleep(1)
        await temp_msg.edit_text("[■■■■■■□□□□] 60%")
        await asyncio.sleep(1)
        await temp_msg.edit_text("[■■■■■■■□□□] 70%")
        await asyncio.sleep(1)
        await temp_msg.edit_text("[■■■■■■■■□□] 80%")
        await asyncio.sleep(1)
        await temp_msg.edit_text("[■■■■■■■■■□] 90%")
        await asyncio.sleep(1)
        await temp_msg.edit_text("[■■■■■■■■■■] 100%")
        await asyncio.sleep(3)
        await temp_msg.edit_text("ッ Wait thanks for choosing srm ❤️‍🩹")
        await temp_msg.delete()
    
        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
            except:
                pass
        return
    else:
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
        await message.reply_photo(
            photo=random.choice(PICS),
            caption = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            quote = True
        )
        return

    
#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##

@Bot.on_message(filters.command('help') & filters.private & subscribed)
async def help_command(client: Client, message: Message):
    id = message.from_user.id

    if id in BANNED_USERS:
        await message.reply_text("Sorry, you are banned.")
        return
        
    user = message.from_user.first_name
    last = message.from_user.last_name
    user_id = message.from_user.id
    username = message.from_user.username
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="YOUR MESSAGE HAS BEEN SENT TO THE ADMINS!!! PLS YEHA MESSAGE KARO @TITAN_OWNER_INDIA"
    ),
    await client.send_message(
            chat_id=-1001919036915,
            text=help_text.format(
                user_id=user_id,
                username=username
            )
    )

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):

    if id in BANNED_USERS:
        await message.reply_text("Sorry, you are banned.")
        return
        
    buttons = [
        [
            InlineKeyboardButton(
                "Join Channel",
                url = client.invitelink)
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'Try Again',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()

@Bot.on_message(filters.command('restart') & filters.private & filters.user(ADMINS))
async def restart_text(client: Bot, message: Message):
    await bot.send_message(message.chat.id, "Restarting...")
    os.system("heroku restart -a filestoretitantestindia")
