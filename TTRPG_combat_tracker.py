from operator import attrgetter


class Monster:
    def __init__(self, name, ancestry):
        self.name = name
        self.initiative = 0
        self.health = 0
        self.ancestry = ancestry
    def show(self):
        print(self.name + " : " + str(self.initiative))

class legendary_monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.initiative = 0
    def show(self):
        print(self.name + " : " + str(self.initiative))

class Monster_type:
    def __init__(self, name, health):
        self.name = name
        self.initiative = 0
        self.health = health
    def show(self):
        print(self.name + " : " + str(self.initiative))

class Player:
  def __init__(self, name):
    self.name = name
    self.initiative = 0
  def show(self):
    print(self.name + " : " + str(self.initiative))

class Combat:
    players = []
    monsters = []
    player_characters = []
    monster_races = []
    legendary_monsters = []
    monster_names = []
    players_out_of_turn_order = []
    def show(self):
        print()
        print("initiative order")
        print("----------------")
        for player in self.players:
            player.show()
        print("----------------")
    def get_initiatives(self):
        for player in self.players:
            if player.initiative == 0:
                while True:
                    try:
                        player.initiative = int(input(f"what did {player.name} roll: "))
                        break
                    except ValueError:
                        print("Please enter a number")

        self.players.sort(key=attrgetter('initiative'), reverse=True)
    def add_monster(self, ancestry = ""):
        end = False
        while end != True:
            if ancestry == "":
                while True:
                    try:
                        ancestry = input("Enter the monsters race: ").title()
                        break
                    except ValueError:
                        print("Please enter a valid race")

            for race in self.monster_races:
                if ancestry == race.name:
                    end = True
            if end == False:
                print("The avalable races are", end = " ")
                for i in self.monster_races:
                    print(f"{i.name},", end = " ")
                ancestry = ""
                print(" ")
        #reset the number if the ancestry changes
        if (other_vareables.last_ancestry != ancestry) and (other_vareables.number != 1):
            other_vareables.reset_number()
        #automaticly name the monsters
        name = f"{ancestry} {other_vareables.number}"
        #make sure the name doesent already exsist
        for taken_name in self.monster_names:
            if taken_name == name:
                other_vareables.add_number()
        #re-manke the name in case it already exsisted
        name = f"{ancestry} {other_vareables.number}"   
        other_vareables.add_number()
        monster = Monster(name, ancestry)
        #update lists
        self.monsters.append(monster)
        self.monster_names.append(monster.name)
        other_vareables.update_ancestry(ancestry)
    def add_legend(self):
        while True:
            try:
                name = input("Enter the legendary monsters name: ").title()

                break
            except ValueError:
                print("Enter a name")
        while True:
            try:
                while True:
                    health = int(input(f"How much health does {name} have: "))
                    if health > 0:
                        break
                    else:
                        print("Enter a positive number")
                break
            except ValueError:
                print("Enter a number")
        legend = legendary_monster(name, health)
        self.players.append(legend)
        self.legendary_monsters.append(legend)
        self.monster_names.append(legend.name)
    def add_monster_type(self):
        while True:
            try:
                name = input("Enter a race for the monsters: ").title().strip()
                break
            except ValueError:
                print("Try again, you need a string")
        while True:
            try:
                health = 0
                while health <= 0:
                    health = int(input("What is the races health: "))
                break
            except ValueError:
                print("Try again, you need an int")
        monster = Monster_type(name, health)
        self.monster_races.append(monster)
        self.players.append(monster)
    def set_monster_health(self):
        for monster_race in self.monster_races:
            for monster in self.monsters:
                if monster.ancestry == monster_race.name:
                    monster.health = monster_race.health

    def play(self):
        for num, player in enumerate(self.players):
            print(f"Its {player.name}'s turn")
            if player in self.player_characters:
                self.turn_menu(num)
            else:
                while True:
                    damage = input("Was this creature damaged during its turn (y/n): ").lower()
                    if damage == "y":
                        self.damage(player)
                        break
                    elif damage == "n":
                        break
                    else:
                        print("enter \"y\" or \"n\"")
                        print()
            if len(self.players_out_of_turn_order) != 0:
                for i, object in enumerate(self.players_out_of_turn_order):
                    while True:
                        out_of_turn = input(f"{object.name} held their turn, are they returning (y/n): ").lower()
                        if out_of_turn == "y" or out_of_turn == "n":
                            break
                        else:
                            print("Enter \"y\" or \"n\"")
                    print()
                    if out_of_turn == "y":
                        self.players.insert(num + 1, self.players_out_of_turn_order.pop(i))
                        out_of_turn = ""




    def turn_menu(self, turn_num):
        action = ""
        print("Enter \"damage\", \"add\", \"change initiative\",\"show\" or \"end\" when done")
        while (action != "end"):
            while True:
                try:
                    action = input("What happend this turn (type end when done) ").lower()
                    break
                except ValueError:
                    print("Please enter a string")
            if action == "damage":
                self.damage()
            elif action == "add":
                self.add_monster_to_initiative()
            elif action == "change initiative":
                action = self.change_initiative(turn_num)
            elif action == "show":
                self.show()
            else:
                print("Enter \"damage\", \"add\", \"change initiative\" or end when done")
    def damage(self, name = ""):
        if (name == "") or (name not in self.monsters):
            for monsters in self.monsters:
                print({monsters.name}, end=" ")
            for monsters in self.legendary_monsters:
                print({monsters.name}, end = " ")
            print(" ")
            creature_damaged = ""
    
            while creature_damaged not in self.monster_names:
                creature_damaged = input("What creature was damaged: ").title()
        else:
            creature_damaged = name
        while True:
            try:
                damage_amount = int(input("How much damage was taken: "))
                break
            except ValueError:
                print("Please enter a number")
        for monster in self.monsters:
            if monster.name == creature_damaged:
                monster.health -= damage_amount
                creature_damaged = ""
                print(f"{monster.health} hp left")
                if monster.health <= 0:
                    print(f"{monster.name} is dead")
                    self.monsters.remove(monster)
        for monster in self.legendary_monsters:
            if monster.name == creature_damaged:
                monster.health -= damage_amount
                creature_damaged = ""
                print(monster.health)
                if monster.health <= 0:
                    print(f"{monster.name} is dead")
                    self.players.remove(monster)
                    self.legendary_monsters.remove(monster)
        if len(self.monsters) == 0 and len(self.legendary_monsters) == 0:
            print("Combat is over")
            quit()
    def add_monster_to_initiative(self):
        while True:
            try:
                new_race = ""
                while True:
                    new_race = input("Is a new race entering combat? (y/n) ").lower()
                    if new_race == "y" or new_race == "n":
                        break
                break
            except ValueError:
                print("Please enter a string")
        while True:
            try:
                number_of_monsters = int(input("How many new monsters: "))
                break
            except ValueError:
                print("Please enter a number")
        if new_race == "y":
            self.add_monster_type()
        elif new_race == "n":
            while True:
                try:
                    race = input("Enter the race of the creatures: ").title()
                    break
                except ValueError:
                    print("Please enter a string")

        for _ in range(number_of_monsters):
            self.add_monster(race)
        self.get_initiatives()
    def change_initiative(self, num):
        self.players_out_of_turn_order.append(self.players.pop(num))
        return "end"

class Other_vareables:
    number = 1
    last_ancestry = ""
    def add_number(self):
        self.number += 1
    def reset_number(self):
        self.number = 1
    def update_ancestry(self, ancestry):
        self.last_ancestry = ancestry
combat = Combat()

other_vareables = Other_vareables()

def main():

    while True:
        try:
            number_of_legends = int(input("How many legendary creatures are there (counts seprate from monsters): "))
            break
        except ValueError:
            print("Please enter a number")


    while True:
        try:
            number_of_monsters = -1
            while number_of_monsters < 0:
                number_of_monsters = int(input("How many monsters are there (counts seprate from legendary creatures): "))
                if number_of_monsters < 0:
                    print("Enter a positive number")
            break
        except ValueError:
            print("Please enter a number")
    if number_of_monsters != 0:
        min_monster_types = 1
    else:
        min_monster_types = 0


    while True:
        try:
            if number_of_monsters != 0:
                number_of_monster_types = -1
            else:
                number_of_monster_types = 0
            while number_of_monster_types < min_monster_types:
                number_of_monster_types = int(input("How many monster races are there: "))

                if number_of_monster_types < min_monster_types:
                    print(f"Enter a value greater than or equal to {min_monster_types}")
            break
        except ValueError:
            print("Please enter a number")


    for _ in range(number_of_monster_types):
        combat.add_monster_type()
    if number_of_monster_types == 1:
        for _ in range(number_of_monsters):
            combat.add_monster(combat.monster_races[0].name)
    else:
        for _ in range(number_of_monsters):
            combat.add_monster()
    for _ in range(number_of_legends):
        combat.add_legend()

    with open("PC names.txt") as file:
        file_contents = file.read()
        names = file_contents.split(",")
        for name in names:
            name = name.strip()
            player = Player(name.title())
            combat.players.append(player)
            combat.player_characters.append(player)

    combat.set_monster_health()
    combat.get_initiatives()
    combat.show()

    while len(combat.monsters) > 0:
        combat.play() 
    while len(combat.legendary_monsters) >0:
        combat.play()
    print("Combat is done")


main()