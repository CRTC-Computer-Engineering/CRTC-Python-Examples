import discord
import sys
import os
import asyncio
import git
import time
import json

g = git.cmd.Git('~/discord')

with open("auto_joe_responses.json", "r") as f: # Load all the responses
    responses = json.load(f)

def restart_program(): # def defines a function, this one in particular restarts the program
    #g.pull() # Would pull a new version from github if in a git repo
    python = sys.executable # use executable in following line 
    os.execl(python, python, * sys.argv) # restart


client = discord.Client()
@client.event # On any event from the discord connection (client)
async def on_message(message): #When a message comes in
    content=message.content # Get the content of the message
    user=message.author # Get the author of the message
    channel=message.channel # the the channel the message was sent in
    
    if user == client.user: # If the user is the robot itself
        return # dont say anything in response to something the robot says

    for key in responses:
        if key.upper() in (content.strip()).upper(): # if in the string content, exists "cool beans"
            print(responses[key])
            await channel.send(responses[key]) # using await so we sync with discord API, send cool beans ASAP

    if "define the word is" in content.strip():
        print("Reboot called by " + str(user))
        await channel.send("Rebooted")
        restart_program() # call function

with open("auto_joe.json", "r") as f:
    robot_data = json.load(f)
    
print("Starting robot with id: " + (robot_data["token"]))
client.run(robot_data["token"])
