from twitchio.ext import commands  # twitch bot package. commands is for chatbots
import os  # direct access to your operating system to get the '.env' file key value pairs
from dotenv import load_dotenv  # allows access to the .env files

filePath = 'outputs.txt'

dynamic_variables = {}  # list of dynamic variables that I need like social media links. i.e. if
# I want to change the link to my discord server I can store them here.

new_commands = {}  # dictionary to store new commands that you can write in twitch chat.

if os.path.exists(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
        if len(lines) % 2 == 0:
            for i in range(0, len(lines), 2):
                curr_line = lines[i].strip("\n")
                matching_value = lines[i+1].strip("\n")
                dynamic_variables[curr_line] = matching_value
        else:
            print("***error: one key does not have a matching value. input temporary value***")


print(str(dynamic_variables))


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
    if "twitter" in dynamic_variables:
        await ctx.send(dynamic_variables["twitter"])
    else:
        await ctx.send("No Twitter link found.")


@bot.command()
async def discord(ctx: commands.Context) -> None:
    if "twitter" in dynamic_variables:
        await ctx.send(dynamic_variables["discord"])
    else:
        await ctx.send("No Discord link found.")


@bot.command()
async def grindserver(ctx: commands.Context) -> None:
    if "twitter" in dynamic_variables:
        await ctx.send(dynamic_variables["grindserver"])
    else:
        await ctx.send("No Grind Server link found.")


@bot.command()
async def addcom(ctx: commands.Context) -> None:
    chatToString = ' '.join(ctx)


@bot.command()
async def editcom(ctx: commands.Context, commandName: str) -> None:
    return

if __name__ == '__main__':
    bot.run()
