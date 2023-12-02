import re

with open("./input.txt") as file:
    games = file.readlines()


def checkgame(game: str):
    pattern = re.compile(r'Game (\d+):')
    gamenum = (pattern.search(game)).group(1)
    gamestring = game.partition(":")[2]
    roundmap = gamestring.split(";")
    mingreen = 0
    minblue = 0
    minred = 0
    for round in roundmap:
        green = 0
        red = 0
        blue = 0
        gameturns = round.split(",")
        for turn in gameturns:
            colornum, color = turn.split()
            match color:
                case "blue":
                    blue = blue + int(colornum)
                case "red":
                    red = red + int(colornum)
                case "green":
                    green = green + int(colornum)
                case _:
                    print("error in parsing:" + turn)
        if blue > minblue:
            minblue = blue
        if red > minred:
            minred = red
        if green > mingreen:
            mingreen = green
    return minred * mingreen * minblue



total = 0
for game in games:
    total = total + checkgame(game)
print(total)