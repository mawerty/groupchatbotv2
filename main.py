import discord
from discord.ext import commands
import random
import aiohttp
import requests
import asyncio
import keep_alive
import json
import datetime


bot = commands.Bot(command_prefix='!', self_bot=True)

color = 3092790

__version__ = 1.9

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
        if message.content == '!nigrate':
              embed = discord.Embed(title='nigrate', color = color, description=f"ur nigrate is {random.randint(1,100)}% u black monkey ")
              embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/887809991971581962/898693499787046922/cat-kissing.gif")
              await message.channel.send(embed=embed)


        elif message.content == "!dog":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/dog') 
              dogjson = await request.json()
              embed = discord.Embed(title="what da dog doin", color=color)
              embed.set_image(url=dogjson['link'])
              await message.channel.send(embed=embed)


        elif message.content == "!cat":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/cat') 
              dogjson = await request.json()
              embed = discord.Embed(title="meow", color=color)
              embed.set_image(url=dogjson['link'])
              await message.channel.send(embed=embed)


        elif message.content == "!meme":
          embed = discord.Embed(title="", description="")

          async with aiohttp.ClientSession() as cs:
              async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                  res = await r.json()
                  embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                  await message.channel.send(embed=embed)


        



        elif message.content == "!rat":
             async with aiohttp.ClientSession() as session:
              request = await session.get('https://some-random-api.ml/img/raccoon') 
              dogjson = await request.json()
              embed = discord.Embed(title="ghurbs a rat", color=color)
              embed.set_image(url=dogjson['link'])
              await message.channel.send(embed=embed)


        elif message.content == "!hentai":
            hentai = requests.get("https://nekos.life/api/v2/img/hentai")
            res = hentai.json()
            embed = discord.Embed(color=color)
            embed.set_author(name="hentai",icon_url=message.author.avatar_url)
            embed.set_image(url=res["url"])
            await message.channel.send(embed=embed)


        elif message.content == "!boobs":
          boobs = requests.get("https://nekos.life/api/v2/img/boobs")
          res = boobs.json()
          embed = discord.Embed(color=color)
          embed.set_author(name="boobs",icon_url=message.author.avatar_url)
          embed.set_image(url=res["url"])
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


        elif message.content == "!sex":
          anal = requests.get("https://nekos.life/api/v2/img/anal")
          res = anal.json()
          embed = discord.Embed(color=color)
          embed.set_author(name="cock n ballz",icon_url=message.author.avatar_url)
          embed.set_image(url=res["url"])
          await message.channel.send(embed=embed)


        elif message.content == "!av":
          await message.channel.send('User ID?')
          id = await bot.wait_for('message')
          user = str(id.content)
          await message.channel.send("in progress")

        elif message.content == "!pingsite":
          await message.channel.send('Website??')
          website = await bot.wait_for('message')
          url = str(website.content)
          if url is None: 
              pass
          else:
              try:
                  r = requests.get(url)
                  if r == 404:
                    embed = discord.Embed(title=f'{url}', color = color, description=f"Site is down")
                    await message.channel.send(embed=embed)
              except:
                    embed = discord.Embed(title=f'{url}', color = color, description=f"Site is up")
                    await message.channel.send(embed=embed)  
              else:
                    embed = discord.Embed(title=f'{url}', color = color, description=f"Invalid site")
                    await message.channel.send(embed=embed)  

        elif message.content == '!help':
              embed = discord.Embed(title='List', color = color, description=f"**!ping** - sends the bot latency **!tokeninfo** - checks a tokens info **!ipinfo** - checks the ip \n**!guessinggame** - guessing game (if someone interrupts it breaks) \n**!rat** - sends ghurb \n**!cat** - sends a cat pic \n**!dog** - sends a dog pic \n**!nigrate** - sends ur nigrate u blackie \n**!hentai** - sends some hentai \n**!sex** - sends porn \n**!boobs** - <3 \n**!av** - sends ur av (ur only) \n**!snipe** - sends the last deleted message \n\n credits to xyte only")
              embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/887809991971581962/898693499787046922/cat-kissing.gif")
              await message.channel.send(embed=embed)

        elif message.content == "!ping":
          await message.channel.send(f'Latency: {bot.latency} seconds.')


        elif message.content == "!ipinfo":
            await message.channel.send('Enter the ip.')
            ip = await bot.wait_for('message')
            ip2 = str(ip.content)
            async with aiohttp.ClientSession() as session:
              request = await session.get(f'https://ipapi.co/{ip2}/json') 

              ipjson = await request.json()
              json_formatted_str = json.dumps(ipjson, indent=2)
              ipinfo2 = json_formatted_str.replace(":", " ")
              ipinfo3 = ipinfo2.replace('"', "")
              ipinfo4 = ipinfo3.replace('{', "")
              ipinfo5 = ipinfo4.replace('}', "")
              await message.channel.send(f"""```{ipinfo5}```""")
              
        elif message.content == "!guessinggame":
                await message.channel.send('Guess a number from 1 to 5!')
                number = random.randint(0, 5)
                for i in range(0, 5):
                    response = await bot.wait_for('message')
                    guess = int(response.content)
                    if guess > number:
                        await message.channel.send('Smaller!')
                    elif guess < number:
                        await message.channel.send('Bigger!')
                    else:
                        await message.channel.send('You guessed it!')









keep_alive.keep_alive()            
bot.run("OTEwOTYwNDg3NzAzOTA0Mzg3.YZa-lg.TpvlL8fAK8tSDM6ohyE_o27YTvA")
