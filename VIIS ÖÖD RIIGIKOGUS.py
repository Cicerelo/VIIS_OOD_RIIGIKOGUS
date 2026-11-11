import random


monsters = ["Kaja", "Jürgen", "Hanno"]
super_weapons = ["Elektrimolekulid", "Odav toidukorv", "India"] # sama järjekord mis monsters
weapons = ["Tool", "Pann", "Pult"]



def player_attack(weapon, super_weapon, player_hp):
    if weapon == super_weapon and player_hp <= 30:
        damage = 100
        print("SUPER RELV!")
    elif weapon == "Tool":
        damage = random.randint(5, 10)
    elif weapon == "Pann":
        damage = random.randint(8, 15)
    else:
        damage = random.randint(0, 25) 
    print("Sa lõid", damage, "damage")
    return damage


def monster_attack(monster):
    damage = random.randint(3, 12)
    print(monster, "lõi sind", damage, "damage")
    return damage


def show_hp(player_hp, monster, monster_hp):
    print("-" * 30)
    print("Sinu elud:", player_hp)
    print(monster, "elud:", monster_hp)
    print("-" * 30)


############## MÄNG ##############

print("=" * 30)
print("   VIIS ÖÖD RIIGIKOGUS")
print("=" * 30)

name = input("Sisesta oma nimi: ")
wins = 0
play = "jah"

while play == "jah":
    nr = random.randint(0, 2) 
    monster = monsters[nr]
    super_weapon = super_weapons[nr] 
    monster_hp = 100
    player_hp = 50
    potions = 2

    print("Sinu ette ilmus", monster)

    while player_hp > 0 and monster_hp > 0:
        show_hp(player_hp, monster, monster_hp)
        action = input("1 - ründa, 2 - joo laudurit: ")
        print("-" * 30)

        if action == "1":
            print("1 -", weapons[0])
            print("2 -", weapons[1])
            print("3 -", weapons[2])
            if player_hp <= 30: 
                print("4 -", super_weapon, "(SUPER RELV!)")
            choice = input("vali relv (number): ")
            print("-" * 30)

            if choice == "1":
                weapon = weapons[0]
            elif choice == "2":
                weapon = weapons[1]
            elif choice == "3":
                weapon = weapons[2]
            elif choice == "4" and player_hp <= 30:
                weapon = super_weapon
            else:
                print("sellist relva pole")
                continue

            monster_hp = monster_hp - player_attack(weapon, super_weapon, player_hp)

        elif action == "2":
            if potions > 0:
                player_hp = player_hp + 20
                potions = potions - 1
                print("jõid laudurit, laudureid alles:", potions)
            else:
                print("laudurid otsas")
                continue

        else:
            print("vale valik")
            continue

        if monster_hp > 0:
            player_hp = player_hp - monster_attack(monster)

    if player_hp > 0:
        print(name, "Saatis koju", monster)
        wins = wins + 1
    else:
        print(monster, "võitis. Game over")

    print("võite kokku:", wins)
    play = input("kas mängid veel? (jah/ei): ")

print("Aitäh mängimast VIIS ÖÖD RIIGIKOGUS", name)