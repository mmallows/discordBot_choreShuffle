import discord
import os
import datetime
import random
import keep_alive

client = discord.Client()
oldChores = [-2, -2, -2, -2, -2]

def shuffleChores():
  chores = ["vacuum", "kitchen", "upstairs bathroom", "downstairs bathroom", "sweep/mop & living room"]
  people = ["Andy", "Adrien", "Jeson", "Justin", "Marcus"]
  newChores = [-1, -1, -1, -1, -1]
  currentDate = datetime.datetime.now()
  str0 = "Weekly Chores: " + str(currentDate.month) + "/" + str(currentDate.day) + "\n"
  
  def roll(x):
    rand = random.randrange(0, 5-x)
    while(x < 4 and rand == oldChores[x]):
        rand = random.randrange(0, 5-x)
    return rand
  
  for i in range(5):
    nextChore = roll(i)
    if (i == 4 and nextChore == oldChores[4]):
      rand = random.randrange(4)
      temp = nextChore
      nextChore = newChores[rand]
      newChores[rand] = temp
    newChores[i] = nextChore
    str0 += people[i] + ": " + chores[nextChore] + "\n"
    del chores[nextChore]
  return str0
    
    

@client.event
async def on_ready():
  print("Ready. Logged in as: {0.user}".format(client))

@client.event
async def on_message(message): #Message Response:
  if message.author == client.user:
    return
  if message.content.startswith('$'): #All User Response:
    if message.content == "$ hello":
      await message.channel.send("Hello, {0.author.name}!".format(message))
      await message.add_reaction("\U0001F596")
    if message.author.id == int(os.environ['OWNER']): #Owner Response:
      if message.content == "$ shuffle chores":
        string = shuffleChores()
        await message.channel.send(string)
    else:
      print("Message not from owner.")
      print(message.content + "\n" + "ID: " + str(message.author.id))
      await message.channel.send("Who are you, my mother?")

keep_alive.keep_alive()
client.run(os.environ['TOKEN'])