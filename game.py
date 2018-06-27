import random

players = [
  {
    "name": "",
    "score": 0
  },
  {
    "name": "",
    "score": 0
  }
]

wheel = []

# HELPER FUNCTIONS
def myround(x, base=50):
    return int(base * round(float(x)/base))

# FUNCTIONS
def wheel_elem(wheel):
  i = 0
  while i < 24:
    # Randomly choose a number between 500 - 900. Round that number by 50 then add to list.
    random_num = random.randint(500, 900)
    elem = myround(random_num)
    wheel += [elem]
    i += 1

  print(wheel)

def start_game(players):
  print("***************************************\n WHEEL OF FORTUNE\n ***************************************")
  # Add elements to the wheel
  wheel_elem(wheel)

  # Players add their name
  # TODO Move player logic to its own function
  for player in players:
      # print(player["name"])
      name = input("What is your first name? ")
      player["name"] = name

  print("Thanks for playing %s and %s!" %(players[0]["name"], players[1]["name"]))
  # TODO Randomly choose which player takes the first turn
  num = 0
  first_turn = players[num]

start_game(players)





