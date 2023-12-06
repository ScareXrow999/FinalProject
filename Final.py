# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:26:51 2023

@author: King of the Grey
"""
"""classes are player 1-3, and monster
each class has different sets of stats and weapons
Knight - 60 health and infinity sword (max damage 20) - higher than others and 
Ninja - 40 health (disadvantage) and daggers (max damage 18) and lower hit chance (40)
Tank - 70 health (advantage) 20 armor(5 more than others) giga hammer ( max damage 25 )
The tank is slow so his hit chance is lower because the monster can dodge
Monster(S) have a starting health of 40 and it preogress by 5 each dungeon(round)
every 3 monsters defeated. you get the option of choose regenerating of health, shield, or an increase of damage
(If i have time) make the monsters names random from a list of 50

Allow input to give your character a name that will be presented throughout the game
If theres a way make an end screen, make colored text, give weapons names.
ALso give an option to block with a small chance of dealing reflecting damage.

EDITED 12/05/23
... I made several changes along the way and it  was to balance everything and add a few small details into this project.
The health,armor, and damage is all changed to help balance the game along with progressive upgrades.
"""



import random

class Character:
    def __init__(self, name="", hitPoints=10, hitChance=50, maxDamage=5, armor=5):
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.initialArmor = armor
        self.armor = armor

    def resetStats(self):
        self.hitPoints = 10
        self.hitChance = 50
        self.maxDamage = 5
        self.armor = self.initialArmor

    def printStats(self):
        print(f"{self.name}\n=================")
        print(f"Hit points: {self.hitPoints}")
        print(f"Hit chance: {self.hitChance}")
        print(f"Max damage: {self.maxDamage}")
        print(f"Armor:      {self.armor}\n")

    def takeDamage(self, damage):
        if self.armor > 0:
            absorbed_damage = min(self.armor, damage)
            self.armor -= absorbed_damage
            damage -= absorbed_damage

        self.hitPoints -= damage

        if self.hitPoints < 0:
            self.hitPoints = 0

    def hit(self, opponent):
        if random.randint(0, 100) <= self.hitChance:
            damage = random.randint(1, self.maxDamage)
            opponent.takeDamage(damage)
            return damage

        return 0

class Knight(Character):
    def __init__(self, name="", hitPoints=90, hitChance=50, maxDamage=20, armor=10):
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor

class Ninja(Character):
    def __init__(self, name="", hitPoints=70, hitChance=80, maxDamage=18, armor=10):
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor

class Tank(Character):
    def __init__(self, name="", hitPoints=110, hitChance=60, maxDamage=15, armor=10):
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor

class Monster(Character):
    def __init__(self, name="", hitPoints=50, hitChance=50, maxDamage=10, armor=5):
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor

def printHeroStats(hero):
    print("Hero Stats:")
    hero.printStats()

def printCharacterAndMonsterStats(hero, monster):
    printHeroStats(hero)
    print("\nMonster Stats:")
    monster.printStats()

def fight(hero, monster):
    while hero.hitPoints > 0 and monster.hitPoints > 0:
        user_input = input("Press 'Enter' to make your move:")

        hero_damage = hero.hit(monster)
        monster_damage = monster.hit(hero)

        print(f"{hero.name} hits {monster.name}...")
        print(f"  for {hero_damage} points of damage")
        print(f"  {monster.name}'s armor remaining: {monster.armor}")

        if monster.hitPoints <= 0:
            break

        user_input = input("Press 'Enter' to let the monster attack:")

        print(f"{monster.name} hits {hero.name}...")
        print(f"  for {monster_damage} points of damage")
        print(f"  {hero.name}'s armor remaining: {hero.armor}")

        if hero.hitPoints <= 0:
            break

        print(f"{hero.name}: {hero.hitPoints} HP")
        print(f"{monster.name}: {monster.hitPoints} HP")

    if hero.hitPoints <= 0:
        print("Game over....")

def restart_game():
    print("Restarting the game...")
    main()

def main():
    round_count = 1
    power_up_round = 1
    power_up_choices = ["1", "2", "3"]
    next_monster_health_increase = 0
    next_monster_damage_increase = 0
    
    words = ["Select a hero to begin", "press 1 for Knight", "press 2 for Ninja", "press 3 for Tank"]
    [print(word) for word in words]

    choice = input("Enter your choice: ")

    if choice == "1":
        hero = Knight()
    elif choice == "2":
        hero = Ninja()
    elif choice == "3":
        hero = Tank()
    else:
        print("Invalid choice. Exiting.")
        return

    hero.name = input("Enter your hero's name: ")

    while True:
        monster = Monster()
        monster.name = "Monster"
        monster.hitPoints += next_monster_health_increase
        monster.maxDamage += next_monster_damage_increase
        
        printCharacterAndMonsterStats(hero, monster)

        fight(hero, monster)

        if hero.hitPoints > 0:
            if round_count == power_up_round * 1:  
                print(f"Power-up Round {power_up_round}")
                decide = input(f"{hero.name}, would you like regenerating health (1), increased armor (2), or a strength spell (3)? ")

                while decide not in power_up_choices:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    decide = input(f"{hero.name}, would you like regenerating health (1), increased armor (2), or a strength spell (3)? ")

                if decide == "1":
                    hero.hitPoints += 80

                elif decide == "2":
                    hero.armor += 13

                elif decide == "3":
                    hero.maxDamage += 9

                next_monster_health_increase += 10
                next_monster_damage_increase += 7
                
                power_up_round += 1

            round_count += 1

        else:
            restart_option = input("Game over. Do you want to restart? (yes/no): ")
            if restart_option.lower() == "yes":
                restart_game()
            else:
                print("Exiting the game.")
                break

if __name__ == "__main__":
    main()
       
