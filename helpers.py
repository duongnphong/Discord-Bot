import requests
import json
import datetime
import pytz
import discord


def get_quote():
    api = requests.get("https://zenquotes.io/api/random")
    quote = json.loads(api.text)
    quote = quote[0]['q']
    return (quote)


def get_time():
    zone = pytz.timezone("Asia/Bangkok")
    now = datetime.datetime.now(zone)
    return (now.strftime("%d-%m-%y %H:%M:%S"))


def is3(x, y):
    if x == 3 or y == 3:
        return True
    else:
        return False


def blanks():
    return "\N{WHITE MEDIUM SQUARE}" * 5


def worldle_layout():
    em = discord.Embed(title="Worlde")
    em.description = "\n".join([blanks()] * 6)
    em.set_footer(text="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return em


def update_alphabet(guess_letter, alphabet):
    alphabet = alphabet.replace(guess_letter, "")
    return alphabet


def update_em(em: discord.Embed, clue: str, alphabet: str):
    em.description = em.description.replace(blanks(), clue, 1)
    em.set_footer(text=alphabet)
    return em


def check(answer, guess, alphabet):
    guess = guess.lower()
    position = 0
    clue = ""
    for letter in guess:
        alphabet = alphabet.replace(letter.upper(), "")
        if letter == answer[position]:
            clue += "🟩"
        elif letter in answer:
            clue += "🟨"
        else:
            clue += "🟥"
        position += 1
    return (alphabet, clue, clue == "🟩🟩🟩🟩🟩")
