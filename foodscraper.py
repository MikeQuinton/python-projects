from urllib.request import Request, urlopen
from discord.ext import tasks
import json, discord, time, sys

discord_token = "" # Discord token id
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} | {client.user.id} has logged in')

@client.event
async def on_message(message):

    channel = client.get_channel(733404047045820458)
    counter = 1
    
    url = 'https://www.reddit.com/r/FoodPorn.json'
    request = Request(url, headers = {'User-Agent' : 'Food Porn image scraper bot'})
    info = urlopen(request).read()
    data = json.loads(info)
    
    if '!food' in message.content.lower():
    
        while counter <= 25:
            
            post_link = data['data']['children'][counter]['data']['url']
            post_title = data['data']['children'][counter]['data']['title']
            counter += 1

            embed = discord.Embed(
                title = post_title,
                colour = discord.Colour.blue()
                )

            embed.set_image(url = post_link)
            
            await channel.send(embed = embed)
            time.sleep(5)
        
client.run(discord_token)
