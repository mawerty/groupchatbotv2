import discord 
from discord.ext import commands
import random
import aiohttp
import requests
import asyncio
import json
from datetime import datetime
import base64
from itertools import cycle
import linecache
import os
import time

adminaccess = 
token = ""
bot = commands.Bot(command_prefix='!', bot=False)

kissgifs = ['http://i.imgur.com/0D0Mijk.gif ', 'http://i.imgur.com/TNhivqs.gif', 'http://i.imgur.com/3wv088f.gif', 'http://i.imgur.com/7mkRzr1.gif', 'http://i.imgur.com/8fEyFHe.gif']

languages = {
							'da'		: 'Danish, Denmark',
							'de'		: 'German, Germany',
							'en-GB' : 'English, United Kingdom',
							'en-US' : 'English, United States',
							'es-ES' : 'Spanish, Spain',
							'fr'		: 'French, France',
							'hr'		: 'Croatian, Croatia',
							'lt'		: 'Lithuanian, Lithuania',
							'hu'		: 'Hungarian, Hungary',
							'nl'		: 'Dutch, Netherlands',
							'no'		: 'Norwegian, Norway',
							'pl'		: 'Polish, Poland',
							'pt-BR' : 'Portuguese, Brazilian, Brazil',
							'ro'		: 'Romanian, Romania',
							'fi'		: 'Finnish, Finland',
							'sv-SE' : 'Swedish, Sweden',
							'vi'		: 'Vietnamese, Vietnam',
							'tr'		: 'Turkish, Turkey',
							'cs'		: 'Czech, Czechia, Czech Republic',
							'el'		: 'Greek, Greece',
							'bg'		: 'Bulgarian, Bulgaria',
							'ru'		: 'Russian, Russia',
							'uk'		: 'Ukranian, Ukraine',
							'th'		: 'Thai, Thailand',
							'zh-CN' : 'Chinese, China',
							'ja'		: 'Japanese',
							'zh-TW' : 'Chinese, Taiwan',
							'ko'		: 'Korean, Korea'
					}


locales = [
							"da", "de",
							"en-GB", "en-US",
							"es-ES", "fr",
							"hr", "it",
							"lt", "hu",
							"nl", "no",
							"pl", "pt-BR",
							"ro", "fi",
							"sv-SE", "vi",
							"tr", "cs",
							"el", "bg",
							"ru", "uk",
							"th", "zh-CN",
							"ja", "zh-TW",
							"ko"
					]

@bot.event
async def on_message_delete(message):
		global snipe_message_content
		global snipe_message_author
		global snipe_message_id
		snipe_message_content = message.content
		snipe_message_author = message.author.id
		snipe_message_id = message.id
		await asyncio.sleep(60)
		if message.id == snipe_message_id:
				snipe_message_author = None
				snipe_message_content = None
				snipe_message_id = None



@bot.event
async def on_message(message):
				args = message.content.split()
				
				
				if message.content == "!help":
					await message.channel.send('''**Help Categories:**
					
> **Utility**
> **Image**
> **Economy**
> **Fun**
					
***Now supports args!***
Developed by xyte''')
				
					
				elif args[0] ==	'!help' and args[1] == "utility":
					await message.channel.send("""```

Utility
!snipe - sends the last deleted message 
!b64encode/decode <text> - encodes/decodes something in base64 
!botinvite <bot id> - sends a invite to a bot
!linkvertise <linkvertise link> - bypasses a linkvertise link
!leak <email> - checks a query on intelx (only emails)
!idinfo <id> - checks an id
!ipinfo <ip> - checks an ip 
!tokeninfo <token> - checks a tokens info 
!spamwebhook <webhook> - spams a webhook (spams long arabic characters and pings everyone on default, might change)
!deletewebhook <webhook> - deletes a webhook 
```""")

				elif args[0] == "!help" and args[1] == "image":
					await message.channel.send("""```


Image
!banner <user (id or ping) - steals anyones banner
!av <id> (id or ping) - steals anyones avatar
!racc - sends a raccoon pic 
!cat - sends a cat pic 
!dog - sends a dog pic 
!hentai - you already know what it does 
!kiss <user> - kissy kissy
```""")
					
				elif args[0] == "!help" and args[1] == "economy":
					await message.channel.send("""```


Economy
!leaderboard/!lb - shows the leaderboard of richest people
!crime - commit crime, with a chance of losing money
!work - work, gives you money
!slots <amount> slots
!rob <user> robs someones wallet (wallet only)
!balance - checks  your balance
!withdraw <amount> - withdraws an amount of money from your bank
!deposit <amount> - deposits an amount of money into your bank
!send <user> <amount> - transfers money to someone from your bank
```""")
					
				elif args[0] == "!help" and args[1] == "fun":
					await message.channel.send("""```

Fun
!cf - flips a coin
!poll - <question> creates a poll
!guessinggame - guessing game 
!nigrate - sends ur nigrate u blackie 
```""")
					
				elif args[0] == "!exec":
					if message.author.id == 871480725407432795:
						code = args[1:]
						code2 = ' '.join(code)
						exec(code2)
					else:
						await message.channel.send('Unathorized')
				

				
				elif args[0] == "!kiss":
					kisseduser = args[1]
					await message.channel.send(f'<@{message.author.id}> Kissed {kisseduser}! {kissgifs[random.randint(0,4)]}')
	
				elif args[0] == "!randomserver":
					server = linecache.getline('servers.txt', random.randint(1, 1600))
					await message.channel.send(server)

				elif args[0] == "!hentai":
					r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
					res = r.json()
					url=res['url']
					await message.channel.send(f'''hentiea\n{url}''')



				elif args[0] ==	"!cf":
					ht = random.randint(1,2)
					if ht == 1:
						await message.channel.send("Heads!") #why did u make everything into args[0] again
					else:
						await message.channel.send("Tails!")


				elif args[0] ==	"!poll":
					question = args[1:]
					q = ' '.join(question)
					message = await message.channel.send(f"""`Poll!`\n{q}""")
					await message.add_reaction('✅')
					await message.add_reaction('❎')


				elif args[0] ==	"!leak":
					search = {args[1]}
					search2 = str(search).replace("@", "%40").strip('{').strip('}').strip("'")
					await message.channel.send(f"<https://intelx.io/?s={search2}>")
					


				elif args[0] ==	"!botinvite":
					await message.channel.send(f'https://discord.com/api/oauth2/authorize?client_id={args[1]}&permissions=0&scope=bot')

											
				elif args[0] ==	'!deletewebhook':
					try:
						requests.delete(args[1])
						await message.channel.send(f"Deleted webhook '{eval(args[1])}''")
					except:
						await message.channel.send(f"Error! {eval(args[1])}")

				elif args[0] ==	"!b64encode":
					string = args[1:]
					strink = ' '.join(string)
					string_bytes = strink.encode("ascii")
					base64_bytes = base64.b64encode(string_bytes) 
					base64_string = base64_bytes.decode("ascii") 
					await message.channel.send(f"Encoded: `{base64_string}`")

				elif args[0] ==	"!b64decode":
					string_bytes = args[1].encode("ascii")
					base64_bytes = base64.b64decode(string_bytes) 
					base64_string = base64_bytes.decode("ascii")
					await message.channel.send(f"Decoded: {base64_string}")


				elif args[0] ==	'!nigrate':
					await message.channel.send(f"`ur nigrate is {random.randint(0,100)}% u black monkey `")


				elif args[0] ==	"!dog":
						 async with aiohttp.ClientSession() as session:
							 request = await session.get('https://some-random-api.ml/img/dog') 
							 dogjson = await request.json()
							 await message.channel.send(dogjson['link'])



					
				elif args[0] ==	"!spamwebhook":
					webhook = args[1]
					try:
						for i in range(100):
							requests.post(
									webhook.content,
									json={'content': f"""@everyone ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽ @everyone ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽"""})
					except:
						print('err')



				elif args[0] ==	"!cat":
						 async with aiohttp.ClientSession() as session:
								request = await session.get('https://some-random-api.ml/img/cat') 
								dogjson = await request.json()
								await message.channel.send(dogjson['link'])


				elif args[0] ==	"!racc" or args[0] ==	"!rat":
						 async with aiohttp.ClientSession() as session:
								request = await session.get('https://some-random-api.ml/img/raccoon') 
								dogjson = await request.json()
								await message.channel.send(dogjson['link'])



				elif args[0] ==	"!tokeninfo":
					 token = args[1]
					 headers = {
							 'Authorization': token,
							 'Content-Type': 'application/json'
					 }
					 try:
							 res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
							 res = res.json()
							 user_id = res['id']
							 locale = res['locale']
							 avatar_id = res['avatar']
							 language = languages.get(locale)
							 creation_date = "nvm"
					 except KeyError:
							 headers = {
									 'Authorization': "Bot " + token,
									 'Content-Type': 'application/json'
							 }
							 try:
									 res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
									 res = res.json()
									 user_id = res['id']
									 locale = res['locale']
									 avatar_id = res['avatar']
									 language = languages.get(locale)
									 creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
											 '%d-%m-%Y %H:%M:%S UTC')
									 em = discord.Embed(color=0x2f3136,
											 description=f"Name: `{res['username']}#{res['discriminator']} ` **(BOT**)\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
									 fields = [
											 {'name': 'Flags', 'value': res['flags']},
											 {'name': 'Local language', 'value': res['locale'] + f"{language}"},
											 {'name': 'Verified', 'value': res['verified']},
									 ]
									 for field in fields:
											if field['value']:
													 em.add_field(name=field['name'], value=field['value'], inline=False)
													 em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
									 return await message.channel.send(embed=em)
							 except KeyError:
									 await message.channel.send("Invalid token")
					 em = discord.Embed(color=0x2f3136,
							 description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
					 nitro_type = "None"
					 if "premium_type" in res:
							 if res['premium_type'] == 2:
									 nitro_type = "Nitro Premium"
							 elif res['premium_type'] == 1:
									 nitro_type = "Nitro Classic"
					 fields = [
							 {'name': 'Phone', 'value': res['phone']},
							 {'name': 'Flags', 'value': res['flags']},
							 {'name': 'Local language', 'value': res['locale'] + f"{language}"},
							 {'name': 'MFA', 'value': res['mfa_enabled']},
							 {'name': 'Verified', 'value': res['verified']},
							 {'name': 'Nitro', 'value': nitro_type},
					 ]
					 await message.channel.send(f"`Name:` `{res['username']}#{res['discriminator']}`\n`ID:` `{res['id']}`\n`Email:` `{res['email']}`\n`PFP:` https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}\n`Phone:` {res['phone']} \n`Flags:` {res['flags']}\n`Language:` {language}\n`2FA:` {res['mfa_enabled']}\n`Verified:` {res['verified']}\n`Nitro:` {nitro_type}")



				elif args[0] ==	"!idinfo":
					response2 = args[1]
					user = await bot.fetch_user(response2)
					time1 = user.created_at.timestamp()
					timestamp = datetime.fromtimestamp(time1)
					await message.channel.send(f"""
**Username:** {user.name}#{user.discriminator}
**Id:** {response2}
**Created at:** {timestamp}
""")

				elif args[0] ==	"!linkvertise":
					headers = {
					"Host": "bypass.bot.nu",
					"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
					"Accept": "*/*",
					"Accept-Language": "en-US,en;q=0.5",
					"Accept-Encoding": "gzip, deflate, br",
					"Referer": "https://bypass.bot.nu/",
					"Connection": "keep-alive",
							}
					link = args[1]
					data = requests.get(f"https://bypass.bot.nu/bypass2?url={link}", headers=headers)
					link = data.json()["destination"]
					await message.channel.send(f"Link: {link}")

				elif args[0] ==	"!av":
					user = message.mentions[0]
					await message.channel.send(user.avatar_url)



				elif args[0] ==	"!banner":
					user = message.mentions[0]
					req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid = user.id))
					banner_id = req["banner"]
					if banner_id == None:
						await message.channel.send("No banner!")
					else:
						banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
						await message.channel.send(banner_url)


				elif args[0] ==	"!ipinfo":
						ip2 = args[1]
						if ip2 == "Link?":
							pass
						else:
							async with aiohttp.ClientSession() as session:
								request = await session.get(f'https://ipapi.co/{ip2}/json') 

								ipjson = await request.json()
								json_formatted_str = json.dumps(ipjson, indent=2)
								ipinfo = json_formatted_str.strip('{').strip('}').replace('"', "⁣").replace(',', '⁣').replace('	⁣', '⁣')

								await message.channel.send(f"""```{ipinfo}```""")
							
		

				elif args[0] ==	'!snipe':
						if snipe_message_content==None:
								await message.channel.send("NOTHING TO SNIPE U FAT LITTLE MONKEY")
						else:
								await message.channel.send(f"""
Sniped: `{snipe_message_content}`
Sent by: <@{snipe_message_author}>""")



					
				elif args[0] ==	"!guessinggame":
								await message.channel.send('Guess a number from 1 to 5!')
								number = random.randint(1, 5)
								for i in range(1, 5):
										response = await bot.wait_for('message')
										guess = int(response.content)
										if guess > number:
												await message.channel.send('Smaller!')
										elif guess < number:
												await message.channel.send('Bigger!')
										else:
												await message.channel.send('You guessed it!')

				elif args[0] == "!balance" or args[0] == "!bal":
					if len(args) > 1 and len(message.mentions) > 0:
					  user = message.mentions[0]
					else:
					  user = message.author
					users = await get_bank_data()

					wallet_amt = users[str(user.id)]["wallet"]
					bank_amt = users[str(user.id)]["bank"]

					await message.channel.send(f"__**{user}**'s Balance:__\n> Wallet Balance: `{wallet_amt}`\n> Bank Balance: `{bank_amt}`")
					
                    
				elif args[0] == "!fish":
					await open_account(message.author)

					users = await get_bank_data()
					user = message.author

					if random.randint(0,100) < 2:
						await message.channel.send('You caught the ultra rare fish! (5000$)')
						users[str(user.id)]["wallet"] += 5000
						with open("mainbank.json", "w") as f:
							json.dump(users,f)
					elif random.randint(0,100) < 10:
						await message.channel.send('You caught the rare fish! (350$)')
						users[str(user.id)]["wallet"] += 350
						with open("mainbank.json", "w") as f:
							json.dump(users,f)			
					elif random.randint(0,100) < 23:
						await message.channel.send('You caught the common fish! (175$)')
						users[str(user.id)]["wallet"] += 175
						with open("mainbank.json", "w") as f:
							json.dump(users,f)
					elif random.randint(0,100) < 65:
						await message.channel.send('You caught the poopie fish! (100$)')
						users[str(user.id)]["wallet"] += 100
						with open("mainbank.json", "w") as f:
							json.dump(users,f)
					elif random.randint(0,100) < 75:
						await message.channel.send('You caught nothing dumb ass ur so bad.... also u broke ur fishing rod and lost 50 money haha!!!')
						users[str(user.id)]["wallet"] -= 50
						with open("mainbank.json", "w") as f:
							json.dump(users,f)
				




				elif args[0] == "!work":
					await open_account(message.author)

					users = await get_bank_data()
					user = message.author
					earnings = random.randrange(10,30)
					earnings2 = random.randrange(31,50)
					earnings3 = random.randrange(51,70)
					earnings4 = random.randrange(80,110)
					
					chance = random.randint(1,10)
					if chance == 1:	
						await message.channel.send('task: print 010101 in python...')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == 'print("010101")':
							await message.channel.send(f"u earned {earnings}$!")

							users[str(user.id)]["wallet"] += earnings

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus!')
                            

                            
					elif chance == 2:
						await message.channel.send('task: tell me what 3 times 3 is :rage:')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == "9":
							await message.channel.send(f"u earned {earnings2}$!")

							users[str(user.id)]["wallet"] += earnings2

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus!')
					elif chance == 3:
						await message.channel.send('task: tell me who made gc bot?')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == "xyte":
							await message.channel.send(f"u earned {earnings3}$!")

							users[str(user.id)]["wallet"] += earnings3

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus! answer: xyte')
					elif chance == 4:
						await message.channel.send('task: say nigger')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == "nigger":
							await message.channel.send(f"u earned {earnings2}$!")

							users[str(user.id)]["wallet"] += earnings2

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus!')
					elif chance == 5:
						await message.channel.send('task: on the scale of 1/10, how pedo is lucifer?')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == "10/10":
							await message.channel.send(f"u earned {earnings}$!")

							users[str(user.id)]["wallet"] += earnings

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus! answer: 10/10')
					elif chance == 6:
						await message.channel.send('task: do we hate faggots?')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == "yes":
							await message.channel.send(f"u earned {earnings3}$!")

							users[str(user.id)]["wallet"] += earnings3

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus!')
					elif chance == 7:
						await message.channel.send('task: tell me is monarch god?')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == "no":
							await message.channel.send(f"u earned {earnings3}$!")

							users[str(user.id)]["wallet"] += earnings3

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus! answer: no')
					elif chance == 8:
						await message.channel.send('task: tell me is 4ren skid?')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == "yes":
							await message.channel.send(f"u earned {earnings2}$!")

							users[str(user.id)]["wallet"] += earnings2

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus! correct answer: yes')
					elif chance == 9:
						await message.channel.send('task: tell me is 0xbc sexy?')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == "no":
							await message.channel.send(f"u earned {earnings3}$!")

							users[str(user.id)]["wallet"] += earnings3

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus! answer: no')
					elif chance == 10:
						await message.channel.send('task: tell me is xyte skid?')
						check = lambda m: m.author == message.author and message.channel == message.channel
						answer = await bot.wait_for("message", check=check, timeout=30)
						if answer.content == "no":
							await message.channel.send(f"u earned {earnings4}$!")

							users[str(user.id)]["wallet"] += earnings4

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						else:
							await message.channel.send('incorrect dingus! Your balance has been reset!')
						


				elif args[0] == "!withdraw" or args[0] == "!with":
					amount = args[1]
					await open_account(message.author)
					if amount == None:
						await message.channel.send('u need to put in a number dingus')
					bal = await update_bank(message.author)

					amount = int(amount)
					if amount>bal[1]:
						await message.channel.send('no money poor dingus')
						return
					if amount<0:
						await message.channel.send('amount must be positive')
						return

					await update_bank(message.author,amount,"wallet")
					await update_bank(message.author,-1*amount,"bank")
					await message.channel.send(f"you withdrew {amount}$")
				
				elif args[0] == "!deposit" or args[0] == "!dep":
					amount = args[1]
					await open_account(message.author)
					if amount == None:
						await message.channel.send('u have to deposit something dingus')
						return
					bal = await update_bank(message.author)
					amount = int(amount)
					if amount>bal[0]:
						await message.channel.send("you dont have this much poor boy")
						return
					if amount<0:
						await message.channel.send("amount must be positive")
						return

					await update_bank(message.author, -1*amount)
					await update_bank(message.author,amount,"bank")

					await message.channel.send(f"you deposited {amount}$")
					
				elif args[0] == "!send":
					member = args[1]
					amount = args[2]
					member = int(member.strip('<@!>'))
					member = await bot.fetch_user(member)
					await open_account(message.author)
					await open_account(member)

					if amount == None:
						await message.channel.send('dingus what are you sending, enter an amount')
						return
					bal = await update_bank(message.author)

					amount = int(amount)
					if amount>bal[1]:
						await message.channel.send('your too poor')
						return
					if amount<0:
						await message.channel.send('amount must be positive ')
						return
					await update_bank(message.author,-1*amount, "bank")
					await update_bank(member,amount,"bank")

					await message.channel.send(f"you gave {member} {amount}$")
				elif args[0] == "!rob":
					member = args[1]
					member = int(member.strip('<@!>'))
					member = await bot.fetch_user(member)
					await open_account(message.author)
					await open_account(member)
					
					bal = await update_bank(member)
					
					if bal[0]<100:
						await message.channel.send('they not worth it dingus!')
						return
					earnings = random.randrange(0, bal[0])
					
					if random.randint(1,5) < 4:
						await update_bank(message.author,earnings)
						await update_bank(member,-1*earnings)
						await message.channel.send(f'you robbed {earnings}$') 
					else:
						await update_bank(message.author,-500)
						await message.channel.send(f'you tripped on a nigger and lost 500$ trying to rob.') 

				elif args[0] == "!forcetakewallet":
					if message.author.id == adminaccess:
						member = args[1]
						member = int(member.strip('<@!>'))
						member = await bot.fetch_user(member)
						await open_account(message.author)
						await open_account(member)
						
						bal = await update_bank(member)
						
						earnings = int(args[2])
						
						await update_bank(message.author,earnings)
						await update_bank(member,-1*earnings)
						await message.channel.send(f'you took {earnings}$') 
					else:
						await message.channel.send('you cant do that lil nigga')

				elif args[0] == "!forcetakebank":
					if message.author.id == adminaccess:
						member = args[1]
						member = int(member.strip('<@!>'))
						member = await bot.fetch_user(member)
						await open_account(message.author)
						await open_account(member)
						
						bal = await update_bank(member)
						
						earnings = int(args[2])
						
						await update_bank(message.author,earnings, "bank")
						await update_bank(member,-1*earnings, "bank")
						await message.channel.send(f'you took {earnings}$') 
					else:
						await message.channel.send('you cant do that lil nigga')
					
				elif args[0] == "!addbank":
					if message.author.id == adminaccess:
						member = args[1]
						member = int(member.strip('<@!>'))
						member = await bot.fetch_user(member)
						await open_account(message.author)
						await open_account(member)
						
						bal = await update_bank(member)
						
						earnings = int(args[2])
						
						await update_bank(member,+1*earnings, "bank")
						await message.channel.send(f'you added {earnings}$') 
					else:
						await message.channel.send('you cant do that lil nigga')

				elif args[0] == "!addwallet":
					if message.author.id == adminaccess:
						member = args[1]
						member = int(member.strip('<@!>'))
						member = await bot.fetch_user(member)
						await open_account(message.author)
						await open_account(member)
						
						bal = await update_bank(member)
						
						earnings = int(args[2])
						
						await update_bank(message.author,earnings, "wallet")
						await update_bank(member,earnings, "wallet")
						await message.channel.send(f'you added {earnings}$') 
					else:
						await message.channel.send('you cant do that lil nigga')

				elif args[0] == "!slots":
					amount = args[1]
					await open_account(message.author)
					if amount == None:
						await message.channel.send('u have to put a number in dingus')
						return
					bal = await update_bank(message.author)
					amount = int(amount)
					if amount>bal[0]:
						await message.channel.send('ur too poor haha')
						return
					if amount<0:
						await message.channel.send('amount must be positive')
						return
					final = []
					for i in range(3):
						a = random.choice(["S", "E", "X"])
						final.append(a)
					await message.channel.send(str(final))
					if final[0] == final[1] or final[0] == final[2]:
						await update_bank(message.author,0.5*amount)
						await message.channel.send(f'you won {amount}$')
					else:
						await update_bank(message.author, -1*amount)
						await message.channel.send('you lost hahahahah ezzzzzzzzzz')
                        
				elif args[0] == "!crime":
					await open_account(message.author)

					users = await get_bank_data()
					user = message.author
					earnings = random.randrange(200,300)
					unearnings = random.randrange(150,200)
					lw = random.randint(1,3)
						
					await message.channel.send('What crime do you want to commit? \n> **1** = rob an old lady\n> **2** = heist\n> **3** = steal a car')
					check = lambda m: m.author == message.author and message.channel == message.channel
					answer = await bot.wait_for("message", check=check, timeout=30)
					if answer.content == "1":
						if lw == 1:
							await message.channel.send(f"u earned {earnings}$!")

							users[str(user.id)]["wallet"] += earnings

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						elif lw == 2 or 3:
							await message.channel.send(f'the old lady smacked you with her bag and you lost {earnings}$ dingus ezz')
							users[str(user.id)]["wallet"] -= unearnings

							with open("mainbank.json", "w") as f:
								json.dump(users,f) 
					elif answer.content == "2":
						if lw == 1:
							await message.channel.send(f"u earned {earnings}$!")

							users[str(user.id)]["wallet"] += earnings

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						elif lw == 2 or 3:
							await message.channel.send(f'you got caught in 4k trying to break in the vault and lost {earnings}$ dingus ezz')
							users[str(user.id)]["wallet"] -= unearnings

							with open("mainbank.json", "w") as f:
								json.dump(users,f) 
					elif answer.content == "3":
						if lw == 1:
							await message.channel.send(f"u earned {earnings}$!")

							users[str(user.id)]["wallet"] += earnings

							with open("mainbank.json", "w") as f:
								json.dump(users,f)
						elif lw == 2 or 3:
							await message.channel.send(f'the car owner caught you and you were fined {earnings}$ dingus ezz')
							users[str(user.id)]["wallet"] -= unearnings

							with open("mainbank.json", "w") as f:
								json.dump(users,f) 
					else:
						await message.channel.send('invalid choice dingus! try again never')


				elif args[0] == "!leaderboard":
					x = 5
					users = await get_bank_data()
					leader_board = {}
					total = []
					for user in users:
						name = int(user)
						total_amount = users[user]["wallet"] + users[user]["bank"]
						leader_board[total_amount] = name
						total.append(total_amount)

					total = sorted(total,reverse=True)


					lb = []
					index = 1
					for amt in total:
						id_ = leader_board[amt]
						mem = bot.get_user(id_)
						name = mem.name
						lb.append(f"> **{index}.** __{name}__ - `{amt}`\n")
						if index == x:
							break
						else:
							index += 1

					await message.channel.send(f' '.join(lb))




async def open_account(user):
	users = await get_bank_data()
	if str(user.id) in users:
		return False
	else:
		users[str(user.id)] = {}
		users[str(user.id)]["wallet"] = 0
		users[str(user.id)]["bank"] = 0
	with open("mainbank.json", "w") as f:
		json.dump(users,f)
	return True
async def get_bank_data():
		with open("mainbank.json", "r") as f:
			users = json.load(f)
		return users
async def update_bank(user,change = 0,mode = "wallet"):
	users = await get_bank_data()
	users[str(user.id)][mode] += change
	with open("mainbank.json", "w") as f:
		json.dump(users,f)
	bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
	return bal
	
bot.run(token)
