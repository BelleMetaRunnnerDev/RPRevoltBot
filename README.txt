Roleplay Bot for Revolt Source Code
Source code by: Belle MR Dev

This is the source code to make a custom Roleplay bot for your server using Revolt's masquerade feature.
This source code is using Voltage which is a Python package for Revolt bots and is easily customizable.



1. Run the following command: pip install git+https://github.com/EnokiUN/voltage (You have to install Voltage from git instead of pypi since the pypi method does not work.
2. Download/Fork the source code and go to https://app.revolt.chat/settings/bots and create a bot.
3. Replace BOT_TOKEN_HERE with your own Bot token you copied from the bots setting
4. Time to modify the masquerade command here:
@client.command(description="Masquerade. Arguments required. Example: +commandname Hi")
async def commandhere(ctx, *, question):
    await ctx.send(f"{question}", masquerade=voltage.MessageMasquerade(name="NAME_HERE", avatar="IMAGE_URL_HERE"))
    await ctx.message.delete()

commandhere = Replace with the actual command name you want to use
NAME_HERE = Replace with the name of the Masquerade
IMAGE_URL_HERE = Replace with the url of the avatar you want for the Masquerade

5. Copy and paste the Masquerade command and repeat step 4 for every masquerade you want to add.
6. Run the Bot.
--- When inviting and using the bot, make sure the bot has the following permissions: Masquerade, Manage Messages, View Channel, and Send Messages



FOLLOW THE SOURCE CODE CREATOR:
Youtube: https://www.youtube.com/channel/UChBm9wK2m5SuFzAUuPHuULg
Youtube Development: https://www.youtube.com/channel/UCCYCRAt1srptO3dc7eeN4Yw
Twitter: https://twitter.com/AxolDemon
Twitter Development: https://twitter.com/BelleMRdev
Reddit: https://www.reddit.com/user/BelleMR