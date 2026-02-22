import os
import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands
from utils import commands as bot_commands

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not TOKEN:
    print("⚠️ DISCORD_BOT_TOKEN missing in .env")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online!")

async def main():
    # Register commands
    await bot_commands.register(bot)

    try:
        await bot.start(TOKEN)
    except discord.LoginFailure:
        print("❌ Login failed: check your DISCORD_BOT_TOKEN in .env")
        exit(1)
    except Exception as e:
        print(f"⚠️ Bot crashed: {e}")

# Termux-friendly event loop
asyncio.run(main())
