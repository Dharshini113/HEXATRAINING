import csv

# 1 
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    players = list(reader)

# # 2
# for player in players:
#     print(player)

# # 3
# print("Total Players:", len(players))

# 4
tot_runs = sum(int(player[4]) for player in players)
print("Total runs:", tot_runs)

# 5 
highest = 0
for player in players:
    if int(player[4]) > highest:
        highest = int(player[4])
print("Highest runs:", highest)

# 6 
lowest = int(players[0][4])
for player in players:
    if int(player[4]) < lowest:
        lowest = int(player[4])
print("Lowest runs:", lowest)

# 7
print("Average Runs:", tot_runs / len(players))

# 8
# teams = set()
# for player in players:
#     teams.add(player[2])
# print(teams)

# # 9 
# print("Total Teams:", len(teams))

# 10
top_player = ""
highest = 0
for player in players:
    if int(player[4]) > highest:
        highest = int(player[4])
        top_player = player[1]
print("Top scorer:", top_player)

# 11
tot_fours = 0
for player in players:
    tot_fours += int(player[5])
print("Total fours:", tot_fours)

# 12
tot_sixes = 0
for player in players:
    tot_sixes += int(player[6])
print("Total sixes:", tot_sixes)

# 13
fours = 0
player_fours = ""
for player in players:
    if int(player[5]) > fours:
        fours = int(player[5])
        player_fours = player[1]
print("Most fours:", player_fours)

# 14 
sixes = 0
player_sixes = ""
for player in players:
    if int(player[6]) > sixes:
        sixes = int(player[6])
        player_sixes = player[1]
print("Most sixes:", player_sixes)

# 15 
team_runs = {}

for player in players:
    team = player[2]
    runs = int(player[4])
    if team in team_runs:
        team_runs[team] += runs
    else:
        team_runs[team] = runs
print(team_runs)

# 16
best = max(team_runs, key=team_runs.get)
print("Best team:", best)

# 17 
player_runs = {}
for player in players:
    player_runs[player[1]] = int(player[4])
print(player_runs)

# 18 
# sorted_players = sorted(player_runs.items(),key=lambda x: x[1],reverse=True)
# print(sorted_players)

# # 19 
# for player in players:
#     if int(player[4]) > 600:
#         print(player)

# 20 
boundary = tot_fours + tot_sixes
print("Total boundaries:", boundary)

# 21
def top_scorer():
    return max(player_runs, key=player_runs.get)
print(top_scorer())

# 22
def average_runs():
    return tot_runs / len(players)
print(average_runs())

# 23
def best_team():
    return max(team_runs, key=team_runs.get)
print(best_team())

# 24
def boundaries():
    return tot_fours + tot_sixes
print(boundaries())

# # 25
# try:
#     with open("players.csv", "r") as file:
#         reader = csv.reader(file)
# except FileNotFoundError:
#     print("File not found!")

# # 26
# for player in players:
#     try:
#         runs = int(player[4])
#     except ValueError:
#         print("Invalid runs:", player)

# # 27
# for player in players:
#     try:
#         matches = int(player[3])
#     except ValueError:
#         print("Invalid matches:", player)

import numpy as np

# runs_arr = []
# for player in players:
#     runs_arr.append(int(player[4]))
# runs_arr = np.array(runs_arr)

# print("Total runs:", np.sum(runs_arr))
# print("Average runs:", np.mean(runs_arr))
# print("Maximum runs:", np.max(runs_arr))
# print("Minimum runs:", np.min(runs_arr))
# print("Standard deviation:", np.std(runs_arr))
# print("Median:", np.median(runs_arr))

import pandas as pd

# 29
df = pd.read_csv("players.csv")
print(df)

# 30
top5 = df.sort_values(by="runs",ascending=False)
print(top5.head())

# # 31
# players_sorted = df.sort_values(by="runs",ascending=False)
# print(players_sorted)

# # 32
# team_runs_pd = df.groupby("team")["runs"].sum()
# print(team_runs_pd)

# # 33
# team_avg = df.groupby("team")["runs"].mean()
# print(team_avg)

# # 34
# above = df[df["runs"] > 600]
# print(above)

# # 35
# print(team_runs_pd.idxmax())

with open("cricket_report.txt", "w") as file:

    file.write("CRICKET REPORT\n\n")

    file.write(f"Total Players: {len(players)}\n")
    file.write(f"Total Runs: {tot_runs}\n")
    file.write(f"Average Runs: {average_runs()}\n")
    file.write(f"Highest Scorer: {top_scorer()}\n")
    file.write(f"Lowest Runs: {lowest}\n")

    file.write("\nTeam Wise Runs\n")
    file.write(str(team_runs))

    file.write("\n\nTop 5 Players\n")
    file.write(str(top5.head()))

    file.write("\n\nMost Fours\n")
    file.write(player_fours)

    file.write("\n\nMost Sixes\n")
    file.write(player_sixes)
print("Report Generated")

# 36
top_players = df[df["runs"] > 600]
top_players.to_csv("top_players.csv",index=False)
print("top_players.csv created")

# 37
team_summary = df.groupby("team").agg(
{
    "runs": ["sum", "mean"],
    "player_name": "count"
})
team_summary.to_csv("team_summary.csv")
print("team_summary.csv created")

# 38
while True:

    print("\n1. Player Analysis")
    print("2. Team Analysis")
    print("3. Boundary Analysis")
    print("4. Export Reports")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Top Scorer:", top_scorer())
        print("Average Runs:", average_runs())

    elif choice == "2":
        print("Best Team:", best_team())
        print(team_runs)

    elif choice == "3":
        print("Total Fours:", tot_fours)
        print("Total Sixes:", tot_sixes)
        print("Boundaries:", boundaries())

    elif choice == "4":
        top_players.to_csv("top_players.csv",index=False)
        team_summary.to_csv("team_summary.csv")
        print("Reports Exported")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")