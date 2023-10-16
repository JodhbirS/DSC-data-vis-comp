import matplotlib.pyplot as plt

# Graph 1: Races won in the 2023 F1 Season

raceWinners2023 = ["Max Verstappen", "Sergio Perez", "Carlos Sainz"]

racesWon = [14, 2, 1]

plt.pie(racesWon, labels= raceWinners2023, autopct=lambda p:f'{int(p*sum(racesWon)/100)}')
plt.title("F1 2023 Race Winners", fontsize= 16, fontweight= "bold")

plt.savefig('fig1.png')
plt.show()


# Graph 2: F1 2023 Season Team standings but Max is a team

teams = [
    "MAX VERSTAPPEN", # one driver, vs two per team
    "MERCEDES",
    "FERRARI",
    "ASTON MARTIN",
    "MCLAREN",
    "ALPINE",
    "WILLIAMS",
    "ALFA ROMEO",
    "HAAS",
    "ALPHATAURI"
]

points = [433, 326, 298, 230, 219, 90, 23, 16, 12, 5]

plt.figure(figsize=(9, 4))

plt.barh(teams, points, color= "red")
plt.xlabel("Points")
plt.title("F1 2023 Team Standings", fontsize= 16, fontweight= "bold")

plt.xticks(fontsize= 8)
plt.yticks(fontsize= 8)

plt.gca().invert_yaxis()
plt.savefig('fig2.png')
plt.show()

# Graph 3: F1 2023 Laps led (in first)

drivers = ["VERSTAPPEN",
           "PEREZ",
           "SAINZ",
           "LECLERC",
           "HAMILTON",
           "NORRIS",
           "RUSSELL",
           "ALONSO",
           "PIASTRI"
]

laps_led = [769, 138, 77, 12, 7, 6, 6, 3, 1]

plt.figure(figsize=(9, 4))
plt.barh(drivers, laps_led, color= "red")
plt.xlabel("Laps Led in 2023")
plt.title("Laps Led by Drivers in F1 2023 Season", fontsize= 16, fontweight= "bold")

plt.gca().invert_yaxis()
plt.tight_layout()

plt.savefig('fig3.png')
plt.show()