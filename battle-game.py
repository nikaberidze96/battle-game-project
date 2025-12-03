import random

class Player:
    def __init__(self, name, hp, attack, defense, potions):
        self.name = name
        self.hp = hp 
        self.attack = attack
        self.defense = defense
        self.potions = potions
        

    def is_alive(self):
        return self.hp > 0
        


    def show_status(self):
        print(f"Name: {self.name}" )
        print(f"HP: {self.hp}" )
        print(f"Attack: {self.attack}" )
        print(f"Defense: {self.defense}" )
        print(f"Potions: {self.potions}" ) 


        print("-" * 15)

class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp 
        self.attack = attack
        self.defense = defense
        
        

    def is_alive(self):
        return self.hp > 0
        


    def show_status(self):
        print(f"Name: {self.name}" )
        print(f"HP: {self.hp}" )
        print(f"Attack: {self.attack}" )
        print(f"Defense: {self.defense}" )
                

import random

def attack(attacker, defender):
    
    damage = random.randint(attacker.attack - 5, attacker.attack) - defender.defense
    if damage < 0:
        damage = 0
    defender.hp -= damage
    print(f"{attacker.name} attacks {defender.name} for {damage} damage")   
    
import random        

def use_potion(player):
    if player.potions > 0:
        heal_amount = random.randint(15, 25)
        player.hp += heal_amount 
        player.potions -= 1
        print(f"{player.name} used a potion and healed {heal_amount} hp")
    else:
        print(f"{player.name} is out of potions")   


def fight(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print("\n------ PLAYER ------")
        player.show_status()
        print("\n------ ENEMY ------")
        enemy.show_status()

        action = input("Choose action [1] Attack [2] Use Potion]: ")


        if action == "1":
            attack(player, enemy)
        elif action == "2":
            use_potion(player)

        if enemy.is_alive():
            attack(enemy, player)                
          
def main():
    player = Player("knight", 100, 20, 5, 3)
    enemy = Enemy("orc", 100, 20, 5)

    fight(player, enemy)

    print("\n -----WINNER-----")
    if player.hp <= 0:
        print("Orc is the winner")
    elif enemy.hp <= 0:
        print("Knight is the winner")   

    print("\n--------")

    print("Thank you for playing")
    
    print("--------")
    
    print("If you wanna replay run python again")
    
    print("--------")

if __name__ == "__main__":
    main()
