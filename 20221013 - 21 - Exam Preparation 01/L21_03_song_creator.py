# 20221013 - Python - Python Advanced - Exam Preparation 01
# 03 - Song Creator - judge: https://judge.softuni.org/Contests/Practice/Index/3534#2


# _______________ version 1 _________________ judge 100%


def add_songs(*tuples):
    songs = {}

    for tuple in tuples:
        song, lyrics = tuple

        if song not in songs:                   # songs[song] = songs.get(song, []) + [lyrics]
            songs[song] = []
        songs[song].extend(lyrics)

    output = []

    for s_title, s_lyrics in songs.items():
        output.append('- ' + s_title)
        output.extend(s_lyrics)

    return '\n'.join(output)                    # same as:   os.linesep.join(output)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time", ["Just in time, I found you just in time",
                      "Before you came, my time was running low",
                      "I was lost, the losing dice were tossed",
                      "My bridges all were crossed, nowhere to go"])
))

print()

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))

print()

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
