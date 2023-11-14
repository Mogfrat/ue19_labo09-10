import requests
import discord
from discord import app_commands
from os import environ

token = environ["token"]

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Connexion
@client.event
async def on_ready():
    await tree.sync()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Conversion en cours..."))
    print("Fonctionnel")


@tree.command(name= "convert", description="Convertit un montant d'une devise à une autre", guild=None)
async def convert(interaction:discord.Interaction, devise_from:str, devise_to:str, ammount:int):
    response = requests.get(f'https://api.currencybeacon.com/v1/convert?api_key=HumGsoCSF5ujJWmBK7ManRBw8olFpP5W&from={devise_from}&to={devise_to}&amount={amount}')
    if response.status_code == 200 :
        resp = response.json()
        embed = discord.Embed()
        embed.add_field(name="Montant total:",value=f'{res["repsonse"]["value"]} {res["response"]["to"].lower()}')
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Veuillez vérifier vos paramètres")

if __name__ == "__main__":
    client.run(token)