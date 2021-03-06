from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from kingbot import kingbot, vr ,Adminsettings
__MODULE__ = "purgeme"
__HELP__ = """
__**This command helps you to delete your last 'n' messages in the chat**__
──「 **Usage** 」──
-> `purgeme`
"""

@kingbot.on_message(filters.command("purgeme",vr.get("HNDLR")) & filters.user(Adminsettings))  
def purgeme(client , message):
    msg_text=message.text
    chat_id=message.chat.id
    if " " in msg_text:
        number=msg_text[msg_text.index(" ")+1 : len(msg_text)]
        if(not number.isnumeric()):
            message.reply("Need a number to delete !")
        else:
            number=int(number)
            msg_id=message.message_id - 1
            while number > 0:
                try:
                    print(msg_id)
                    if kingbot.get_messages(chat_id , msg_id).from_user.id == kingbot.get_users("me").id:
                        client.delete_messages(chat_id , msg_id)
                        print("Heyyy")
                        number=number-1
                    msg_id=msg_id-1
                except Exception as e:
                    msg_id=msg_id-1
    else:
        message.reply("Give me a number to delete !!")