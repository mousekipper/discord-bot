import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from collections import defaultdict
from profanity_check import predict, predict_prob
import os


# 봇의 명령어 접두사와 인텐트 설정
intents = discord.Intents.default()
intents.members = True  # 멤버 관련 이벤트를 받기 위해 필요
bot = Bot(command_prefix='!', intents=intents)

# 봇이 준비되었을 때 실행되는 이벤트
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# 간단한 인사 명령어
@bot.command()
async def hello(ctx):
    await ctx.reply('Hi, there!')

prefix = "~" 
intents = discord.Intents.all()

import discord
from discord.ext import commands
from collections import defaultdict
from asyncio import sleep

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.spam_count = defaultdict(int)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    bot.spam_count[message.author] += 1
    if bot.spam_count[message.author] > 6:
        await message.channel.purge(limit=bot.spam_count[message.author], check=lambda m: m.author == message.author)
        embed = discord.Embed(title="경고", description=f"{message.author.mention}, 도배가 감지되었습니다. 메시지를 삭제하였습니다.", color=0xff0000)
        await message.channel.send(embed=embed)
        bot.spam_count[message.author] = 0
    else:
        await sleep(2)
        bot.spam_count[message.author] -= 1

    await bot.process_commands(message)

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# 욕설 리스트를 정의
bad_words = ["시발", "개새끼", "미친"]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # 메시지에 욕설이 포함되어 있는지 확인합니다.
    if any(bad_word in message.content for bad_word in bad_words):
        await message.delete()
        embed = discord.Embed(title="경고", description=f"{message.author.mention}, 욕설이 감지되었습니다. 메시지를 삭제하였습니다.", color=0xff0000)
        await message.channel.send(embed=embed)

    await bot.process_commands(message)


access_token = os.environ["BOT_TOKEN"]
bot.run('access_token')
