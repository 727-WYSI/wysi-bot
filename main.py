import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.dm_messages = True

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
@bot.command(name='time')
async def get_time(ctx, *, location):
    api_url = f'http://worldtimeapi.org/api/timezone/{location}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        current_time = data['datetime']
        await ctx.send(f'The current time in {location} is: {current_time}')
    else:
        await ctx.send(f'Error fetching time for {location}')
@bot.command(name='weather')
async def get_weather(ctx, *, location):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        await ctx.send(f'The weather in {location} is: {weather_description}, Temperature: {temperature}°C')
    else:
        await ctx.send(f'Error fetching weather for {location}')
@bot.command(name='meme')
async def send_meme(ctx):
    meme_url = 'https://meme-api.herokuapp.com/gimme'
    response = requests.get(meme_url)
    if response.status_code == 200:
        data = response.json()
        meme_image = data['url']
        await ctx.send(meme_image)
    else:
        await ctx.send('Error fetching meme')
bot.run('YOUR_TOKEN')
