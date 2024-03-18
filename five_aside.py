import random

player_list = ["Cech","Cole","Terry","Azpilicueta","Ivanovic","Lampard","Makelele","Zola","Hazard","Drogba"]
team_one = []
team_two = []
player_selection = ""

if (len(player_list) % 2 != 0):
    print("Warning - you have entered an uneven number of players, please add or remove a player")
else:
    while len(player_list) > 0:
        player_selection = random.choice(player_list)
        team_one.append(player_selection)
        player_list.remove(player_selection)
        player_selection = random.choice(player_list)
        team_two.append(player_selection)
        player_list.remove(player_selection)

print("Team One:")
print(*team_one, sep=", ")
print("Team Two:")
print(", ".join(team_two))



