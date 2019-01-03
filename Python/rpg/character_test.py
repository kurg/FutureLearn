from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
from character import Enemy

dave.describe()
dave.talk()
dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
