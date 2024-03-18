import random

teams = ["Arsenal", "Bayern Munich", "Athletico Madrid", "Borussia Dortmund", "PSG", "Barcelona", "Real Madrid", "Manchester City"]

team = []
for number in range(0,8):
    selected_team = random.choice(teams)
    team.append(selected_team)
    teams.remove(selected_team)

print("The Quarter Finals are:")
print(f"QF1: {team[0]} v {team[1]}")
print(f"QF2: {team[2]} v {team[3]}")
print(f"QF3: {team[4]} v {team[5]}")
print(f"QF4: {team[6]} v {team[7]}")

""" semi_team = [[team[0],team[1]],[team[2],team[3]],[team[4],team[5]],[team[6],team[7]]] """
semi_team = [str(team[0])+"/"+str(team[1]),str(team[2])+"/"+str(team[3]),str(team[4])+"/"+str(team[5]),str(team[6])+"/"+str(team[7])]

semi_finalists = []
for number in range(0,4):
    selected_semi = random.choice(semi_team)
    semi_finalists.append(selected_semi)
    semi_team.remove(selected_semi)

print("The Semi Finals are:")
print(f"SF1: {semi_finalists[0]} v {semi_finalists[1]}")
print(f"SF2: {semi_finalists[2]} v {semi_finalists[3]}")
