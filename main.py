import os
import discord # discord library
from discord.ext import commands
from discord.ext.commands import bot
from keep_alive import keep_alive
import random
import requests
import json
from urllib.request import urlopen

# bot = commands.Bot(command_prefix='?')

client = discord.Client()

@client.event
async def on_ready():
  loja = "Black Ops II"
  await client.change_presence(status = discord.Status.idle, activity = discord.Game(loja))
  print("I'm ready hbu? ;)")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

# RESPONSES PALIDHJE
###  if msg.startswith("-p"):
###    await message.channel.send("You're listening to Eminem right?")

  sharje = ["qi", "qifsha", "kurv", "pederr", "rruspi", "biq", "kaja"]

  if any(word in msg for word in sharje):
    await message.channel.send("Sbon more me sha se ti qiva ropt")

  kar123 = ["kar", "Kar"]
  if any(word in msg for word in kar123):
    await message.channel.send("Quki?, Peci?, Luci?, Cuci?, Penisi?, Paketa?, Phalla?, Patëllgjani?")
  
  pidhi123 = ["pidh", "Pidh"]
  if any(word in msg for word in pidhi123):
    await message.channel.send("Mini?, Kuqi?, Garazha?, Mushi?, Piqka?, Lulja?, Kotelja?, Mackë?, Vagina?")

  if msg == "po du me myt veten":
    await message.channel.send("Don't! Reznov will always love you!")

  if msg == "kom me myt veten":
    await message.channel.send("Don't! Reznov will always love you!")

  palo123 = ["palo", "Palo"]
  if any(word in msg for word in palo123):
    await message.channel.send("Palo more pidhin")
  
  mfal123 = ["mfal", "Mfal"]
  if any(word in msg for word in mfal123):
    await message.channel.send("Ska mfal, ulu n'guj edhe merrma ngoj KURV")

# EMINEM DISS
  singers = ["nicki", "peep", "kendrick", "lil", "limp", "nirvana", "arctic", "gorillaz", "doja", "cole"]
  if any(word in msg for word in singers):
    await message.channel.send("Eminem's better")

# DONAT GIF
  donat = ["donat", "Donat"]
  if any(word in msg for word in donat):
    await message.channel.send("https://media2.giphy.com/media/MAWxnzv6ZGd7q/200.gif")

# KANEKI GIF
  kaneki123 = ["kaneki", "Kaneki"]
  if any(word in msg for word in kaneki123):
    await message.channel.send(file=discord.File("palidhje/kaneki.gif"))

# AOT GIF
  aot123 = ["aot", "Aot"]
  if any(word in msg for word in aot123):
    await message.channel.send("https://media1.tenor.com/images/5f34fc85b29ae7d0720208774f661af2/tenor.gif?itemid=12359371")

# EREN GIF
  eren123 = ["eren", "Eren"]
  if any(word in msg for word in eren123):
    await message.channel.send(file=discord.File("palidhje/eren.gif"))

# SEX GIF
  sex123 = ["sex", "Sex"]
  if any(word in msg for word in sex123):
    await message.channel.send(file=discord.File("palidhje/sex.png"))

# SEKS GIF
  seks123 = ["seks", "Seks"]
  if any(word in msg for word in seks123):
    await message.channel.send(file=discord.File("palidhje/sex.png"))

# LEDI GIFS
  led123 = ["led", "Led"]
  if any(word in msg for word in led123):
    led = open("palidhje/ledi.txt", "r").read().split()
    await message.channel.send(random.choice(led))

# MIKASA GIFS
  mikasa123 = ["mikasa", "Mikasa"]
  if any(word in msg for word in mikasa123):
    mikasa = open("palidhje/mikasa.txt", "r").read().split()
    await message.channel.send(random.choice(mikasa))

# TOUKA GIFS
  touka123 = ["touka", "Touka"]
  if any(word in msg for word in touka123):
    touka = open("palidhje/touka.txt", "r").read().split()
    await message.channel.send(random.choice(touka))

# NEZUKO GIFS
  nezuko123 = ["nezuko", "Nezuko"]
  if any(word in msg for word in nezuko123):
    nezuko = open("palidhje/nezuko.txt", "r").read().split()
    await message.channel.send(random.choice(nezuko))

# DIELL GIFS
  dielli = ["diell", "Diell"]
  if any(word in msg for word in dielli):
    nicki = open("palidhje/dielli.txt", "r").read().split()
    await message.channel.send(random.choice(nicki))

# EMINEM GIF
  if msg == "eminem":
    await message.channel.send("http://31.media.tumblr.com/9c0e366ffee7fa81c816b2d571af199c/tumblr_mkuqr7qZv81ru2fjro1_500.gif")

# ANIME RANDOM GIFS FROM A RANDOM API PO DU SE QUOTES PALIDHJE
  def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)
  if msg == "quote":
    quote = get_quote()
    await message.channel.send(quote)

# RANDOM CAT FACTS
  def get_cat():
    response = requests.get("https://some-random-api.ml/facts/cat")
    json_data = json.loads(response.text)
    cat = json_data
    return(cat)

  macja = ["cat", "Cat"]
  if any(word in msg for word in macja):
    cat = get_cat()
    embed = discord.Embed(title = "Cat Fact", color = discord.Color.blue())
    embed.set_image(url = "https://res.cloudinary.com/jerrick/image/upload/v1514493943/teqcyxcn1hboqpuwifcq.gif")
    embed.add_field(name = cat, value = "Yes, it's random :)")
    await message.channel.send(embed = embed)

# RANDOM DOG FACTS
  def get_dog():
    response = requests.get("https://some-random-api.ml/facts/dog")
    json_data = json.loads(response.text)
    dog = json_data
    return(dog)

  dog123 = ["dog", "Dog"]
  if any(word in msg for word in dog123):
    dog = get_dog()
    embed = discord.Embed(title = "Dog Fact", color = discord.Color.dark_red())
    embed.set_image(url = "https://64.media.tumblr.com/beeb302ec92b3c3cee2062c6b4c191a5/8b08f96b91ec8bac-02/s400x600/cd2204b368f37a3a84192dc69d799c70b9bf9457.gif")
    embed.add_field(name = dog, value = "Yes, it's random :)")
    await message.channel.send(embed = embed)

# RANDOM KOALA FACTS
  def get_koala():
    response = requests.get("https://some-random-api.ml/facts/koala")
    json_data = json.loads(response.text)
    koala = json_data
    return(koala)

  koala123 = ["koala", "Koala"]
  if any(word in msg for word in koala123):
    koala = get_koala()
    embed = discord.Embed(title = "Koala Fact", color = discord.Color.dark_green())
    embed.set_image(url = "https://i2.wp.com/gifimage.net/wp-content/uploads/2017/08/koala-gif-14.gif")
    embed.add_field(name = koala, value = "Yes, it's random :)")
    await message.channel.send(embed = embed)

# CHESS GIF
  chess123 = ["chess", "Chess"]
  if any(word in msg for word in chess123):
    await message.channel.send("https://i.pinimg.com/originals/a6/df/ae/a6dfae596fffbf8657844a8ca90ed5f0.gif")

# CHESS GIF
  shah123 = ["shah", "Shah"]
  if any(word in msg for word in shah123):
    await message.channel.send("https://i.pinimg.com/originals/a6/df/ae/a6dfae596fffbf8657844a8ca90ed5f0.gif")

# ROCK, PAPER SCISSORS RANDOM RESPONSE
  hands = ["https://i.pinimg.com/originals/c5/4a/af/c54aaf9f829a884e9e9b3ff2cd28dd48.gif", "https://media2.giphy.com/media/ozf26DV8FqaCpkYt6n/giphy.gif", "https://media3.giphy.com/media/huana0WQzdDDG/200.gif"]
  hands123 = [".rock", ".paper", ".scissors"]
  if any(word in msg for word in hands123):
    await message.channel.send(random.choice(hands))

# ME BO RANDOM PLAY 1 FROM EMINEM S ALBUMS N GROOVY

  if msg == "!p eminem":
    play_albums = ["Encore", "Relapse", "The Marshall Mathers LP", "The Marshall Mathers LP 2", "Recovery", "The Eminem Show", "The Slim Shady LP"]
    await message.channel.send("-p " + random.choice(play_albums) + " Eminem")

# EMINEM ALBUMS
  if msg == "!eminem albums":
    eminem_albums = "**Infinite (1996)\nThe Slim Shady LP (1999)\nThe Marshall Mathers LP (2000)\nThe Eminem Show (2002)\nEncore (2004)\nRelapse (2009)\nRecovery (2010)\nThe Marshall Mathers LP2 (2013)\nRevival (2017)\nKamikaze (2018)\nMusic To Be Murdered By (2020)\nMusic To Be Murdered By - Side B (2020)**"
    embed = discord.Embed(title = "EMINEM ALBUMS", color = discord.Color.dark_magenta())
    embed.add_field(name = "\u200b", value = eminem_albums)
    await message.channel.send(embed = embed)

# HOW MANY SERVERS I'M IN
  if msg == "!servers":
    await message.channel.send("I'm in " + str(len(client.guilds)) + " servers baby!")

# BOT LINK
  if msg == "!botlink":
    await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=849954952255111239&permissions=2148006976&scope=bot")

# BOT DESCRIPTION
  if msg == "!description":
    description = open("palidhje/description.txt").read()
    await message.channel.send(description)

# OUTPUTS ALMOST EVERY COMMAND
  if msg == "!help":
    embed = discord.Embed(title = "MY COMMANDS", color = discord.Color.dark_magenta())
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/callofduty/images/d/d1/ViktorReznovBlackout.png/revision/latest?cb=20210417210650")
    embed.set_image(url="https://thumbs.gfycat.com/AridAnyIberianchiffchaff-size_restricted.gif")
    embed.set_footer(text = "I'm watching youuu ;)")
    embed.add_field(name = "\u200b", value = "**[-p]\n[-skip]\n[.skip]\n[qi]\n[kar]\n[pidh]\n[po du me myt veten]\n[kom me myt veten]\n[palo]\n[mfal]\n[kendrick]\n[nicki]\n[lil]\n[peep]\n[eminem]\n[!eminem albums]\n[quote]\n[cat]\n[dog]\n[koala]\n[kaneki]\n[aot]\n[eren]\n[sex]\n[mikasa]\n[touka]\n[!rock !paper or !scissors]\n[!description]\n[!servers]\n[!botlink]\n[!help] shows this page]\n**")
    embed.add_field(name = "Some of these commands can also be activated even if typed inbetween senteces.", value = "\u200b", inline = True)
# inline = False e qet nkryerresht?
    await message.channel.send(embed = embed)

keep_alive()

# BOT TOKEN
client.run (os.environ['donat'])
