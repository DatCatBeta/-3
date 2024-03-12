import time


class IdleGame:
    def __init__(self):
        self.gold = 0
        self.gold_per_second = 1


    def play(self):
        while True:
            print(f"You have {self.gold} gold.")
            print("Options:")
            print("1. Mine gold")
            print("2. Upgrade pickaxe (cost: 10 gold)")
            print("3. Exit")
            choice = input("Enter your choice: ")


            if choice == "1":
                self.mine_gold()
            elif choice == "2":
                self.upgrade_pickaxe()
            elif choice == "3":
                print("Exiting game.")
                break
            else:
                print("Invalid choice.")


            time.sleep(1)


    def mine_gold(self):
        self.gold += self.gold_per_second
        print("Mining gold...")


    def upgrade_pickaxe(self):
        if self.gold >= 10:
            self.gold -= 10
            self.gold_per_second *= 2
            print("Pickaxe upgraded!")
        else:
            print("Not enough gold to upgrade pickaxe.")


if __name__ == "__main__":
    game = IdleGame()
    game.play()