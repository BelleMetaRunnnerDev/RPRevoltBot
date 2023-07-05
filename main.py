import voltage
from voltage.ext import commands
import random
import asyncio
import aiohttp

client = commands.CommandsClient("+")

@client.command(description="Some Information about me")
async def info(ctx):
    embed = voltage.SendableEmbed(title="Roleplay Bot Information", description=f"Servers Im in: {len(client.servers)}\nMy Creator: <@01H0BYBK514G00MJQ68ZSD6QKQ>\nSource Code: https://github.com/BelleMetaRunnnerDev/RPRevoltBot", color="#FFA200")
    await ctx.send(embed=embed)

@client.command(description="Makes me say things. Arguments required. Example: +say Hi")
async def say(ctx, *, message):
    await ctx.send(f'{message}')
    await ctx.message.delete()

@client.command(description="Makes me say things in a embed. Arguments required. Example: +esay Hi")
async def esay(ctx, *, message):
    embed = voltage.Embed(description=f'{message}', color="#FFA200")
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(description="Masquerade. Arguments required. Example: +commandname Hi")
async def commandhere(ctx, *, message):
    await ctx.send(f"{message}", masquerade=voltage.MessageMasquerade(name="NAME_HERE", avatar="IMAGE_URL_HERE"))
    await ctx.message.delete()





client.run("BOT_TOKEN_HERE")
