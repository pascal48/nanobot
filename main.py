import time
#Log the amount of time it takes to start the bot
start_time = time.time()

import logging, datetime, os
import discord
from art import text2art
from nextcord.ext import commands
from colorama import Fore, Back, Style # Background colors are like Back.COLOR, Background is Back.COLOR
from dotenv import load_dotenv
from os import getenv

print(f"os.name tells us that this system is {os.name}")

beecolor = f"{Back.YELLOW}{Fore.BLACK}"

load_dotenv()
# Environment Variable checking
nextcordlogenv = getenv('NEXTCORDLOGGING')
if nextcordlogenv == 'True':
    print(f"{Back.GREEN}Nextcord Logfile Enabled")
    # I'm worried this logfile could get really big, so I would probably not use this yet.
    logger = logging.getLogger('nextcord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
else:
    print(f"{beecolor}Nextcord API Logfile Disabled{Style.RESET_ALL}")

# Cosmetic name of the bot instance
botname = getenv('NAME')
if botname == None:
  botname = "nanobot"
  print(f"{beecolor}No name set. Defaulting to '{botname}'{Style.RESET_ALL}")

# Bot prefix
prefix = getenv('PREFIX')
if prefix == None:
  prefix = "!!"
  print(f"{beecolor}No prefix set. Defaulting to '{prefix}'{Style.RESET_ALL}")

# Github source page
sourcepage = getenv('SOURCEPAGE')
if sourcepage == None:
  sourcepage == "https://github.com/pascal48/nanobot"
  print(f"{beecolor}No sourcepage set. Defaulting to '{sourcepage}'{Style.RESET_ALL}")

# Bot token ( https://discord.com/developers/docs )
token = getenv('TOKEN')
if token == None:
  print(f"{Fore.RED}No token added. Exiting...")
  exit()


intents = discord.Intents.default()
intents.members = True

print(f"Starting {botname}")


bot = commands.Bot(
    command_prefix=prefix,
    case_insensitive=True,
        allowed_mentions=discord.AllowedMentions(
        users=False,         # Whether to ping individual user @mentions
        everyone=False,      # Whether to ping @everyone or @here mentions
        roles=False,         # Whether to ping role @mentions
        replied_user=False,  # Whether to ping on replies to messages
    ),
)


_author_ = "coff3e"
_name_ = botname
_version_ = "DEV-12132021"


def cogservice():
  if os.path.exists("service.txt"):
    fs = "service.txt"
    service = open(fs, 'r')
    cog_file = service.read()
    cogsenabled = cog_file.split()
    service.close()
    for cogs in cogsenabled:
      try:
        cog_start_time = time.time()
        bot.load_extension(cogs)
        cog_end_time = time.time()
        print(f"{Fore.YELLOW}loading {cogs.replace('.','/')} {Style.DIM}({round((cog_end_time - cog_start_time) * 1000)}ms){Style.RESET_ALL}")
      except Exception as e:
        print(f"{Fore.RED}loading {cogs.replace('.','/')} ({e}){Style.RESET_ALL}")
  else:
    print(f"{Fore.RED}service.txt doesn't exist. Exiting.{Style.RESET_ALL}")
    exit()

    
@bot.event
async def on_ready():
    #nanobot startup ascii art
    startprint = print(f"{Fore.MAGENTA}{text2art(_name_,'random')}{Style.RESET_ALL}\n{_version_}{Style.RESET_ALL}")
    if "DEV" in _version_:
      print(f"{Fore.RED}!!!DEV VERSION!!!\n!!!UNSTABLE, EXPECT MANY BUGS!!!")
      print(f"Report bugs to: https://github.com/pascal48/nanobot{Style.RESET_ALL}")

  #did the bot login to the discord API? 
    print("\n----------------------------------------")
    print(f'{Fore.GREEN}Logged in as {bot.user} {Style.DIM}({bot.user.id})')
    print(f'Prefix: {prefix}{Style.RESET_ALL}')
    print("----------------------------------------\n")
    
    cogservice()

  #Printing list of joined guilds and its data
    print(f"\n{Style.DIM}Joined guilds:{Style.RESET_ALL}")
    for guilds in bot.guilds:
      try:
        print([guilds])
      except:
        print(bot.guilds)

    #printing the time it took to start the bot
    end_time = time.time()
    print(f"{Style.DIM}\nTook {round((end_time - start_time) * 1000)}ms ({round((end_time - start_time) * 1)}s) to start-up")

    #set the bot status and then screw off
    try:
      await bot.change_presence(activity=discord.Game(name=prefix))
      print(f"Set bot status as {prefix}{Style.RESET_ALL}")
    except Exception as e:
      print(f"{Fore.RED}Setting bot status failed.\n{e}")


# Loading TOKEN from .env
bot.run(token)

#https://tutorial.vcokltfre.dev/
#https://nextcord.readthedocs.io/
# helpful things ^
