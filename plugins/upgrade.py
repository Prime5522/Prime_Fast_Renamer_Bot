"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 3GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price 50 ₹ /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price 100 ₹ /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price 199 ₹ /🌎 2.5$  per Month
	
	
	Pay Using Upi I'd ```7808912076@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mRiderDM"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN SUPPORT 🛂",url = "https://t.me/Prime_Admin_Nayem")], 
        			[InlineKeyboardButton("Bikash",url = "https://envs.sh/0lv.jpg"),
        			InlineKeyboardButton("Any Method",url = "https://t.me/Prime_Admin_Support_ProBot")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 3GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price 50 ₹ /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price 100 ₹ /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price 199 ₹ /🌎 2.5$  per Month
	
	
	Pay Using Upi I'd ```7808912076@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mRiderDM"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN SUPPORT 🛂",url = "https://t.me/Prime_Admin_Nayem")], 
        			[InlineKeyboardButton("Bikash",url = "https://envs.sh/0lv.jpg"),
        			InlineKeyboardButton("Any Method",url = "https://t.me/Prime_Admin_Support_ProBot")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
