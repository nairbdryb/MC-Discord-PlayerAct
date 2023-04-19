# MC-Discord-PlayerAct
Publishes messages to discord when players join or leave

## Description
This bot is a discord bot that allows your discord members to see when players join and leave the server.

## Deployment
- Clone the repository
- Rename example_env.txt to .env
- Change the values in the .env file
- Install dependencies (requires python3)
    
        pip install -r requirements.txt
        
- Set up a cron job that will run the main.py script with python

## .env File

DISCORD_WEBHOOK: Discord webhook bot will post to.

RCON_PASSWORD: Password configured in your server config file.

RCON_IP: Ip of your mc server.

RCON_PORT: Rcon port specified in your server config file. This may be different depending on port forwarding rules
