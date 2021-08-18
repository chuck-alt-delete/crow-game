import random

CROW_GAME_INITIAL_STATE = {
            "green": 4,
            "red": 4,
            "blue": 4,
            "yellow": 4,
            "crow": 4,
            "basket": 16
}

COLORS = ("blue", "green", "red", "yellow")
DIE = COLORS + ("crow", "basket")


def play() -> str:
    state = CROW_GAME_INITIAL_STATE.copy()
    available = [color for color in COLORS if state[color] > 0]


    while state["crow"] > 0 and state["basket"] > 0:

        roll = random.choice(DIE)

        state[roll] -= 1

        if roll == "crow":
            print(f"oh no! the crow hopped! only {state['crow']} hops to go!")

        if roll in COLORS:
            if state[roll] == 0:
                available.remove(roll)
            if state[roll] >= 0:
                state["basket"] -= 1
                print(f"put {roll} in basket")

            if state[roll] < 0:
                print(f"out of {roll} -- keep playing")
            
        if roll == "basket":
            roll = random.choice(available)
            state[roll] -= 1
            if state[roll] == 0:
                available.remove(roll)
                print(f"put last {roll} in basket")
            else:
                print(f"rolled basket and chose {roll}")

    if state["crow"] <= 0:
        return "crow wins"
    else:
        return "players win"


if __name__ == "__main__":
    print(play())