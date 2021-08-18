import random

class CrowGame():

    def __init__(self) -> None:
        self.state = {
            "green": 4,
            "red": 4,
            "blue": 4,
            "yellow": 4,
            "crow": 4,
            "basket": 16
        }

        self.colors = ("blue", "green", "red", "yellow")

        self.available = [color for color in self.colors if self.state[color] > 0]
        
        self.die = self.colors + ("crow", "basket")
    
    def play(self) -> str:

        while self.state["crow"] > 0 and self.state["basket"] > 0:

            roll = random.choice(self.die)

            self.state[roll] -= 1

            if roll == "crow":
                print(f"oh no! the crow hopped! only {self.state['crow']} hops to go!")

            if roll in self.colors:
                if self.state[roll] == 0:
                    self.available.remove(roll)
                if self.state[roll] >= 0:
                    self.state["basket"] -= 1
                    print(f"put {roll} in basket")

                if self.state[roll] < 0:
                    print(f"out of {roll} -- keep playing")
                
            if roll == "basket":
                roll = random.choice(self.available)
                self.state[roll] -= 1
                if self.state[roll] == 0:
                    self.available.remove(roll)
                    print(f"put last {roll} in basket")
                else:
                    print(f"rolled basket and chose {roll}")
        
        if self.state["crow"] <= 0:
            return "crow wins"
        else:
            return "players win"


if __name__=="__main__":
    game = CrowGame()
    print(game.play())