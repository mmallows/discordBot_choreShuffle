# discordBot_choreShuffle
A discord bot to shuffle chores weekly for my roommates and I.

To run a discord bot, it needs to be hosted from a personal machine or from a server. You can get often sign up to get a free host online. You'll want to put the keep_alive.py and main.py files on the server. The keep_alive.py script will revive the bot when the server is rebooted if it goes down.

Another thing you'll have to do is establish a token in a virtual environment which will also need to be put on the server. That token's value should be set to the specific value for your discord bot. You can see where that is introduced at the bottom of main.py.
Here is an introduction to Discord bots and getting them hosted: 
https://youtu.be/SPTfmiYiuok

To get the bot connected to Discord channel:
Go to the developer applications URL: https://discord.com/developers/application
Add a bot to the Discord App. with the name you want it to have.
Set the bot's permissions stringently so that nobody can do anything attrocious if the bot is overwritten.
Copy the scope link into your browser and add the bot to the server you choose.

If you could get it hosted with a database, it would be a great improvement to make a second command that would store the last distribution of chores to the DB
so that each week, the new set of chores can be guaranteed to be different even when the server goes down. Currently, fresh sets of chores are only (mostly) going to occur when the bot has not lost connection.

Instructions for use:
command for chore shuffle: $ shuffle chores
general hello: $ hello
the general hello message, if sent by the owner, will also display instructions for chore shuffling.