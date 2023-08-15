# Don't Edit

import contextlib
import datetime
import logging

from validators import *
from config import *
from database import *
from database.users import *
from helpers import *
from pyrogram import *
from pyrogram.types import *
from translation import *
from bot import *

logger = logging.getLogger(__name__)

user_commands = ["set_api", "header", "footer", "username", "banner_image", "me"]
avl_web = ["mdiskpro.in", "mdiskpro.xyz",]

avl_web1 = "".join(f"- {i}\n" for i in avl_web)

@Client.on_message(filters.command('start') & filters.private & filters.incoming)
async def start(c:Client, m:Message):
    NEW_USER_REPLY_MARKUP = [
                [
                    InlineKeyboardButton('Ban', callback_data=f'ban#{m.from_user.id}'),
                    InlineKeyboardButton('Close', callback_data='delete'),
                ]
            ]
    is_user = await is_user_exist(m.from_user.id)

    reply_markup = InlineKeyboardMarkup(NEW_USER_REPLY_MARKUP)

    if not is_user and LOG_CHANNEL: await c.send_message(LOG_CHANNEL, f"#NewUser\n\nUser ID: `{m.from_user.id}`\nName: {m.from_user.mention}", reply_markup=reply_markup)
    new_user = await get_user(m.from_user.id)  
    t = START_MESSAGE.format(m.from_user.mention, new_user["method"], new_user["base_site"])

    if WELCOME_IMAGE:
        return await m.reply_photo(photo=WELCOME_IMAGE, caption=t, reply_markup=START_MESSAGE_REPLY_MARKUP)
    await m.reply_text(t, reply_markup=START_MESSAGE_REPLY_MARKUP, disable_web_page_preview=True)


@Client.on_message(filters.command('help') & filters.private)
async def help_command(c, m: Message):
    s = HELP_MESSAGE.format(
                firstname=temp.FIRST_NAME,
                username=temp.BOT_USERNAME)

    if WELCOME_IMAGE:
        return await m.reply_photo(photo=WELCOME_IMAGE, caption=s, reply_markup=HELP_REPLY_MARKUP)
    await m.reply_text(s, reply_markup=HELP_REPLY_MARKUP, disable_web_page_preview=True)

@Client.on_message(filters.command('panel') & filters.private & filters.user(ADMINS))
async def panel_command(c, m: Message):
    reply_markup=PANEL_MESSAGE_REPLY_MARKUP
    
    bot = await bot.get_me()
    await query.message.edit(PANEL_MESSAGE.format(bot.mention(style='md')), reply_markup=PANEL_MESSAGE_REPLY_MARKUP, disable_web_page_preview=True)

    
@Client.on_message(filters.command('features'))
async def about_command(c, m: Message):
    reply_markup=ABOUT_REPLY_MARKUP

    bot = await c.get_me()
    if WELCOME_IMAGE:
        return await m.reply_photo(photo=WELCOME_IMAGE, caption=ABOUT_TEXT.format(bot.mention(style='md')), reply_markup=reply_markup)
    await m.reply_text(ABOUT_TEXT.format(bot.mention(style='md')),reply_markup=reply_markup , disable_web_page_preview=True)


@Client.on_message(filters.command('api') & filters.private)
async def shortener_api_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command
    if len(cmd) == 1:
        s = SHORTENER_API_MESSAGE.format(base_site=user["base_site"], shortener_api=user["shortener_api"])

        return await m.reply(s)
    elif len(cmd) == 2:
        api = cmd[1].strip()
        await update_user_info(user_id, {"shortener_api": api})
        await m.reply(f"Shortener API updated successfully to {api}")

@Client.on_message(filters.command('header') & filters.private)
async def header_handler(bot, m: Message):
    user_id = m.from_user.id
    cmd = m.command
    user = await get_user(user_id)
    if m.reply_to_message:
        header_text = m.reply_to_message.text.html
        await update_user_info(user_id, {"header_text": header_text})
        await m.reply("Header Text Updated Successfully")
    elif "remove" in cmd:
        await update_user_info(user_id, {"header_text": ""})
        return await m.reply("Header Text Successfully Removed")
    else:
        return await m.reply(HEADER_MESSAGE + "\n\nCurrent Header Text: " + user["header_text"].replace("\n", "\n"))

@Client.on_message(filters.command('footer') & filters.private)
async def footer_handler(bot, m: Message):
    user_id = m.from_user.id
    cmd = m.command
    user = await get_user(user_id)
    if not m.reply_to_message:
        if "remove" not in cmd:
            return await m.reply(FOOTER_MESSAGE + "\n\nCurrent Footer Text: " + user["footer_text"].replace("\n", "\n"))

        await update_user_info(user_id, {"footer_text": ""})
        return await m.reply("Footer Text Successfully Removed")
    elif m.reply_to_message.text:
        footer_text = m.reply_to_message.text.html
        await update_user_info(user_id, {"footer_text": footer_text})
        await m.reply("Footer Text Updated Successfully")

@Client.on_message(filters.command('channel') & filters.private)
async def username_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command
    if len(cmd) == 1:
        username = user["username"] or None
        return await m.reply(USERNAME_TEXT.format(username=username))
    elif len(cmd) == 2:
        if "remove" in cmd:
            await update_user_info(user_id, {"channel": ""})
            return await m.reply("Channel Successfully Removed")
        else:
            username = cmd[1].strip().replace("@", "")
            await update_user_info(user_id, {"username": username})
            await m.reply(f"Channel updated successfully to {username}")


@Client.on_message(filters.command('banner_image') & filters.private)
async def banner_image_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command
    if len(cmd) == 1:
        if not m.reply_to_message or not m.reply_to_message.photo:
            return await m.reply_photo(user["banner_image"], caption=BANNER_IMAGE) if user["banner_image"] else await m.reply("Current Banner Image URL: None\n" + BANNER_IMAGE)

        fileid = m.reply_to_message.photo.file_id
        await update_user_info(user_id, {"banner_image": fileid})
        return await m.reply_photo(fileid, caption="Banner Image updated successfully")
    elif len(cmd) == 2:
        if "remove" in cmd:
            await update_user_info(user_id, {"banner_image": ""})
            return await m.reply("Banner Image Successfully Removed")
        else:
            image_url = cmd[1].strip()
            valid_image_url = await extract_link(image_url)
            if valid_image_url:
                await update_user_info(user_id, {"banner_image": image_url})
                return await m.reply_photo(image_url, caption="Banner Image updated successfully")

            else:
                return await m.reply_text("Image URL is Invalid")


@Client.on_message(filters.command('settings') & filters.private)
async def me_handler(bot, m:Message):
    user_id = m.from_user.id
    user = await get_user(user_id)

    user_id = m.from_user.id
    user = await get_user(user_id)

    first_name = m.from_user.first_name 
    
    res = USER_ABOUT_MESSAGE.format(
                
                base_site=user["base_site"],
                method=user["method"], 
                shortener_api=user["shortener_api"], 
                mdisk_api=user["mdisk_api"],
                username=user["username"],
                header_text=user["header_text"].replace(r'\n', '\n') if user["header_text"] else None,
                footer_text=user["footer_text"].replace(r'\n', '\n') if user["footer_text"] else None,
                banner_image=user["banner_image"],
                first_name=first_name,
                user_id=user["user_id"])

    buttons = await get_me_button(user)
    reply_markup = InlineKeyboardMarkup(buttons)
    return await m.reply_text(res, reply_markup=reply_markup, disable_web_page_preview=True)





@Client.on_message(filters.command('ban') & filters.private & filters.user(ADMINS))
async def banned_user_handler(c: Client, m: Message):
    try:
        if len(m.command) == 1:
            x = "".join(f"- `{user}`\n" for user in temp.BANNED_USERS)
            txt = BANNED_USER_TXT.format(users=x or "None")
            await m.reply(txt)
        elif len(m.command) == 2:
            user_id = m.command[1]
            user = await get_user(int(user_id))
            if user:
                if not user["banned"]:
                    await update_user_info(user_id, {"banned": True})
                    with contextlib.suppress(Exception):
                        temp.BANNED_USERS.append(int(user_id))
                        await c.send_message(user_id, "You are now banned from the bot by Admin")
                    await m.reply(f"User [`{user_id}`] has been banned from the bot. To Unban. `/unban {user_id}`")

                else:
                    await m.reply("User is already banned")
            else:
                await m.reply("User doesn't exist")
    except Exception as e:
        logging.exception(e, exc_info=True)

@Client.on_message(filters.command('unban') & filters.private & filters.user(ADMINS))
async def unban_user_handler(c: Client, m: Message):
    try:
        if len(m.command) == 1:
            x = "".join(f"- `{user}`\n" for user in temp.BANNED_USERS)
            txt = BANNED_USER_TXT.format(users=x or "None")
            await m.reply(txt)
        elif len(m.command) == 2:
            user_id = m.command[1]
            user = await get_user(int(user_id))
            if user:
                if user["banned"]:
                    await update_user_info(user_id, {"banned": False})
                    with contextlib.suppress(Exception):
                        temp.BANNED_USERS.remove(int(user_id))
                        await c.send_message(user_id, "You are now free to use the bot. You have been unbanned by the Admin")

                    await m.reply(f"User [`{user_id}`] has been unbanned from the bot. To ban. `/ban {user_id}`")

                else:
                    await m.reply("User is not banned yet")
            else:
                await m.reply("User doesn't exist")
    except Exception as e:
        logging.exception(e, exc_info=True)

@Client.on_message(filters.command("stats") & filters.private & filters.user(ADMINS))
async def stats_handler(c: Client, m: Message):
    try:
        txt = await m.reply("`Fetching stats...`")
        link_stats = await get_bot_stats()
        
        
        
        
        total_users = await total_users_count()

        msg = f"""
**- Total User👶:** `{total_users}`
**- Total Shortener Links Shortened:** `{link_stats['shortener_links']}`



    """


        return await txt.edit(msg)
    except Exception as e:
        logging.error(e, exc_info=True)


@Client.on_message(filters.command("info") & filters.private & filters.user(ADMINS))
async def get_user_info_handler(c: Client, m: Message):
    try:
        if len(m.command) != 2:
            return await m.reply_text("Wrong Input!!\n`/info user_id`")
        user = await get_user(int(m.command[1]))
        if not user:
            return await m.reply_text("User doesn't exist")
        user_first_name = user["first_name"]  # Get the user's first name from the user object
        res = USER_ABOUT_MESSAGE.format(
            first_name=user_first_name,  # Include the user's first name in the format
            base_site=user["base_site"],
            method=user["method"],
            shortener_api=user["shortener_api"],
            mdisk_api="This is something secret",
            username=user["username"],
            header_text=user["header_text"].replace("\n", "\n")
            if user["header_text"]
            else None,
            footer_text=user["footer_text"].replace("\n", "\n")
            if user["footer_text"]
            else None,
            banner_image=user["banner_image"],
        )

        res = f'User: `{user["user_id"]}`\n{res}'
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Ban", callback_data=f'ban#{user["user_id"]}'),
                    InlineKeyboardButton("Close", callback_data="delete"),
                ]
            ]
        )

        return await m.reply_text(res, reply_markup=reply_markup, quote=True)
    except Exception as e:
        await m.reply_text(e)
        logging.error(e)
