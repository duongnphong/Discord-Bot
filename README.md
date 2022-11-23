# Discord Bot: Cheems The Doggo

#### Video Demo: <https://youtu.be/SK-4TqMkMFE>

#### Description:

For the final project of CS50 2022, I decided to make a simple and basic Discord bot that can interact with users and offer a few simple games. As I researched before starting the project, JavaScript and Python both have libraries that support the making of a Discord bot. However, my decision was to use Python since I am more confident with the syntax and writing in Python. I also watched the lecture about Object-Oriented-Program from CS50P in order to prepare myslef for this project.

Project start date: 18/10/2022
project end date: 23/10/2022

The first task was to create the bot via [Discord Developer Applications](https://discord.com/developers/applications). At this stage, I obtained the TOKEN of the bot ready to input into my code.

The whole project consists of:

1. **bot.py**: contains the main part of my code, it consists of the initialization of bot to bot events and bot command registration. The main library I used in Discord.py, I utilized a lot of functions and features of this library, from functions that ask the bot to listen to user's message to making an embedded display and making buttons. I also used many other modules and libraries such as _datetime_, _json_ and _requests_
2. **helpers.py**: contains all the functions that I used in **bot.py** so that I can keep my main program tidy and clean.
3. **words.txt**: contain 2500 5-letter words that I used to make the game of guess word.
4. **README.md**: is this file that you are reading.

The Discord bot TOKEN is stored in a .env file for the reason of privacy and security.

This following part will a brief introduction to the capability of my Discord bot with the prefix to commands is **!**
`!helper`: Display a Discord embed that introduces users to the usage of the bot
`!quote`: Upon calling, it will display to the user a random quote which is requested from API. The cooldown of this command is 24 hours. Users will get notice how long they have to wait if they keep calling this command.
`!rps`: Display 3 options of rock, paper, scissors and play a game of rps with user to see who reached 3 points first.
`!word`: Let user play a game of Wordle, a random word from **words.txt** will be chosen and the user has 6 times to guess the correct words. The correct letters at the correct position will give a _green_ hint, the correct word at the wrong position will give a _yellow_ hint and the wrong word will yield a _red_ hint. The command will reject invalid guess, for instant, not 5-character input from the user.

Besides, the bot has some other interaction when the user mentions the bot or has a certain word or character in their message.

There are still a lot of things I want to add to my bot. For example, integrate the use of databases so I can, for example, give each user a point when I win a game and display the whole database as a leaderboard. I will save those ideas for my future development of the bot.

This is a link to invite the bot to the server: [Invite Cheems](https://discord.com/api/oauth2/authorize?client_id=1031921467681673246&permissions=292058033152&scope=bot)
