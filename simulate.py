# play crow game with classes

from CrowGame import CrowGame

NUM_SIMULATIONS = 5
games = 0
wins = 0
losses = 0

for i in range(NUM_SIMULATIONS):
    game = CrowGame()
    result = game.play()
    games += 1
    if result == "crow wins":
        losses += 1
    elif result == "players win":
        wins += 1

print(f"wins: {wins}")
print(f"losses: {losses}")
print(f"win percetage: {float(wins/games) * 100}")


# play crow game with functions

import procedural_crow_game

for i in range(NUM_SIMULATIONS):
    result = procedural_crow_game.play()
    games += 1
    if result == "crow wins":
        losses += 1
    elif result == "players win":
        wins += 1

print(f"wins: {wins}")
print(f"losses: {losses}")
print(f"win percetage: {float(wins/games) * 100}")