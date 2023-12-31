from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PANEL_MESSAGE = '''**HELLO, ADMIN **
WELCOME TO ADMIN OF  @Linskbanao_Bot '''

START_MESSAGE = '''**Hello, {}
I Am Linksbanao.site, Bulk Link Converter. I Can Convert Links Directly From Your Linksbanao.site Account,
    
1. Go To 👉 https://Linksbanao.site/member/tools/api  
2. Than Copy API Key
3. Than Type /api than give a single space and than paste your API Key (see example to understand more...)**

**/api(space)API Key 
(See Example.👇)
Example:** `/api de303d5270f481aec928f39883da7b7f9a8812ac `

**➕ Hit** 👉 /Features To Know More Features Of This Bot.
**💁‍♀️ Hit** 👉 /help To Get Help.
**➕ Hit** 👉 /channel Command To Get Help About Adding your channel to bot.
**➕ Hit** 👉 /footer To Get Help About Adding your Custom Footer to bot.

If You Want Any **Other Shortner** Link Converter Bot Instead Of SnapUrl than **contact** at 👉 @Ramanandkrgupt (all **shortners** support available.)
'''

HELP_MESSAGE = '''**Hello9, {}
I Am SnapUrl.me, Bulk Link Converter Bot. I Can Convert Links Directly From Your SnapUrl.me Account,**
    
1. Go To 👉 https://SnapUrl.me/member/tools/api
2. Than **Copy API** Key
3. Than Type **/api** than give a **single space** and than **paste** your **API** Key (**see example** to understand more...)

**/api(space)API Key 
(See Example.👇)
Example:** `/api de303d5270f481aec928f39883da7b7f9a8812ac `

**➕ Hit** 👉 /Features To Know More Features Of This Bot.
**💁‍♀️ Hit** 👉 /help To Get Help.
**➕ Hit** 👉 /channel Command To Get Help About Adding your channel to bot.
**➕ Hit** 👉 /footer To Get Help About Adding your Custom Footer to bot.

If You Want Any **Other Shortner** Link Converter Bot Instead Of ""SnapUrl** than **contact** at 👉 @Ramanandkrgupt (all **shortners support** available.)**
'''

ABOUT_TEXT = '''**Hey! My name is @@Linskbanao_Bot. I am Linksbanao.site Link Converter Bot.**

**⚡Features⚡**

• I can **Convert any** links or posts to your **Linksbanao.site** link / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)

• I Can **auto** add custom **footer text** to your every post. Hit 👉 /footer To know more...

• I Can **auto** add custom **Header text** to your every post. Hit 👉 /Header To know more...

• I Can **replace / remove** other's **channel links** with **your channel** link. Hit 👉 /channel To know More...

• I Can **Automatically Replace** Your ***Banner** Image To images in the post. Hit  👉/banner_image To Know More... 

• **No** need to share **password or email** to convert links.**

 Anyone who want to use any **other shortner** instead of SnapUrl than **contact** at 👉 @Ramanandkrgupt (all **shortners support** available.)

**Click On Custom Alias To Create Custom Link**
'''

CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/snapurl | snapurl"""

CHANNELS_LIST_MESSAGE = """
Here is a list of the channels:

{channels}"""

ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""

ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf'), 
        InlineKeyboardButton('Panel', callback_data=f'panel_command')
        
    ],


])

HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('More Features', callback_data=f'about_command')
        
    ]


])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Get Api', url=f'https://Linksbanao.site/member/tools/api')
    ]
])

PANEL_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Admin List', callback_data=f'admin_list'),
        InlineKeyboardButton('Channel List', callback_data=f'channels'),
    ],

[

InlineKeyboardButton(' User Info', callback_data=f'info'),
InlineKeyboardButton('Broadcast', callback_data=f'broadcast'),
    
],
[
InlineKeyboardButton(' 🧑‍💻Stats', callback_data='stats'),
    
]
    
])

BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data="about_command"),
        InlineKeyboardButton("Close", callback_data="delete")
    ],

])

USER_ABOUT_MESSAGE = """
🔧 Here are the current settings for this bot:

- 🧑‍💻 User Id: `{user_id}`

- 🌐 Shortener website: {base_site}

- 🧰 Method: Telegram Bot

- 🔌 {base_site} API: {shortener_api}

- 📎 Username: @{username}

- 📝 Header text:
{header_text}

- 📝 Footer text:
{footer_text}

🖼️ Banner image: {banner_image}


"""

USER_INFO_MESSAGE = """
🔧 Here are the current settings for this bot:

- 🌐 Shortener website: {base_site}

- 🧰 Method: Telegram Bot

- 🔌 {base_site} API: {shortener_api}

- 📎 Username: @{username}

- 📝 Header text:
{header_text}

- 📝 Footer text:
{footer_text}

🖼️ Banner image: {banner_image}


"""







SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/api [api]`
            
Ex: `/api de303d5270f481aec928f39883da7b7f9a8812ac `

Get API From [{base_site}](https://Linksbanao.site/ref/snapurl)

Current {base_site} API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """**Reply to the Footer Text You Want**

This Text will be added to the **bottom** of every message **caption** or text

For adding **line break** use \n
To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """**Hello, I am Linksbanao.site, Bulk Link Converter Bot From Linked Linksbanao.site Account,**

**🌟 Type** /channel (channel link or username)

**example:**
/channel @snapurl
Or
/channel https://t.me/snapurl

**🤘 Hit** 👉 /features To Know More Features Of This Bot.

**- Message @Ramanandkrgupt For More Help -**"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://telegra.ph/file/5e96340a91470256b387a.jpg`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
