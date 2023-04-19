from aiomcrcon import Client
import asyncio
import os
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv


async def GetPlayers():
    # Get Player Data from Minecraft Server
    password = RCON_PASSWORD
    command = "list"

    client = Client(RCON_IP, RCON_PORT, password)
    await client.connect()

    response = await client.send_cmd(command, 15.0)
    await client.close()

    # Parse Player Data
    playerData = response[0].split(": ")
    playerData.pop(0)
    players = playerData[0].split('\n')
    while len(players) > 0 and players[-1] == '':
    # if players[-1] == "":
        del players[-1]
    if len(players) > 0:
        players = players[0].split(", ")
    return players

def GetJoinLeave(players, players_last):
    # Get players that joined and left
    message = ""
    for player in players:
        if player not in players_last:
            message += player + " joined the server\n"
    for player in players_last:
        if player not in players:
            message += player + " left the server\n"
    return message

if __name__ == "__main__":
    # get env variables
    load_dotenv()
    DISCORD_WEBHOOK = os.getenv('DISCORD_WEBHOOK')
    RCON_PASSWORD = os.getenv('RCON_PASSWORD')
    RCON_IP = os.getenv('RCON_IP')
    RCON_PORT = os.getenv('RCON_PORT')

    # set up webhook
    webhook = DiscordWebhook(content="", username="Minecraft Bot", url=DISCORD_WEBHOOK)

    players = asyncio.run(GetPlayers())

    # if no file exists, create one
    if not os.path.exists("players.txt"):
        file = open("players.txt", "w+")
        file.close()

    # compare players list with file containing previous runs players
    file = open("players.txt", "r+")
    players_last = file.read().splitlines()
    if players == players_last:
        pass
    else:
        print("Change")
        message = GetJoinLeave(players, players_last)
        webhook.content = message
        response = webhook.execute()
        
    file.seek(0)
    file.truncate()
    file.write("\n".join(players))
    file.close()
          