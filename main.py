import discord
import os
import datetime
import random
import keep_alive

client = discord.Client()
oldChores = [-2, -2, -2, -2, -2]


def shuffleChores():  # method to shuffle chores: returns string with list of chores assigned to roommates
    chores = [
        "vacuum",
        "kitchen",
        "upstairs bathroom",
        "downstairs bathroom",
        "sweep/mop & living room",
    ]  # list of chores to choose from, should be same size as people list
    people = [
        "Andy",
        "Adrien",
        "Jeson",
        "Justin",
        "Marcus",
    ]  # define list of roommates to split chores between
    newChores = [-1, -1, -1, -1, -1]
    currentDate = datetime.datetime.now()
    returnString = (
        "Weekly Chores: " + str(currentDate.month) + "/" + str(currentDate.day) + "\n"
    )

    def roll(chore_index):  # returns randomly generated index for next chore
        nextChore_index = random.randrange(0, len(chores))
        while (
            chore_index < 4 and nextChore_index == oldChores[chore_index]
        ):  # attempts to ensure new chores are different from old chores
            # first condition (chore_index < 4) keeps method from looping forever on selecting last chore if same as old chore
            nextChore_index = random.randrange(0, len(chores))
        return nextChore_index

    totalChores = len(chores)
    for chore_index in range(totalChores):
        nextChore_index = roll(chore_index)
        if (
            chore_index == 4 and nextChore_index == oldChores[4]
        ):  # if last job is same as before, swap with random other person
            swap_index = random.randrange(4)
            nextChore_index, newChores[swap_index] = (
                newChores[swap_index],
                nextChore_index,
            )
        newChores[chore_index] = nextChore_index
        returnString += people[chore_index] + ": " + chores[nextChore_index] + "\n"
        del chores[nextChore_index]
        oldChores[chore_index] = nextChore_index
    return returnString


@client.event
async def on_ready():
    print("Ready. Logged in as: {0.user}".format(client))


@client.event
async def on_message(message):  # Message Response:
    if message.author == client.user:
        return
    if message.content.startswith("$"):  # All User Response:
        if message.content == "$ hello":
            await message.channel.send("Hello, {0.author.name}!".format(message))
            await message.add_reaction("\U0001F596")
        if message.author.id == int(os.environ["OWNER"]):  # Owner Response:
            if message.content == "$ shuffle chores":
                string = shuffleChores()
                await message.channel.send(string)
        else:  # -- Response for anything starting with $ but not from owner
            print("Message not from owner.")
            print(message.content + "\n" + "ID: " + str(message.author.id))
            await message.channel.send("Who are you, my mother?")


keep_alive.keep_alive()
client.run(os.environ["TOKEN"])
