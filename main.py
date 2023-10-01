from twitchio.ext import commands  # twitch bot package. commands is for chatbots
import os  # direct access to your operating system to get the '.env' file key value pairs
from dotenv import load_dotenv  # allows access to the .env files

file = 'outputs.txt'
twitterLink = ""
discordLink = ""

load_dotenv()  # load the .env file in this project. I got exceptions when I didn't have this code

bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['NICK'],
    prefix='!',
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event()
async def event_ready():
    print("Bot is reading from chat as " + bot.nick)


@bot.command()
async def twitter(ctx: commands.Context) -> None:
    await ctx.send(twitterLink)
    print(twitterLink)


@bot.command()
async def discord(ctx: commands.Context) -> None:
    await ctx.send(discordLink)
    print(discordLink)


@bot.command()
async def editCommand(ctx: commands.Context, commandName: str) -> None:
    return


if __name__ == '__main__':
    bot.run()
