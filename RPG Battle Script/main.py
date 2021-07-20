from classes.game import Person, Bcolors
from classes.magic import Spell

# Creating black magic!

fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Earthquake", 14, 140, "Black")

# Creating white magic!

cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 10, 200, "White")

# Instantiate people

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    print("==================================")
    player.choose_action()
    choice = input("Choose action\n")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        curr_mp = player.get_mp()

        if spell.cost > curr_mp:
            print(Bcolors.FAIL + "Not enough MP\n" + Bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "White":
            player.heal(magic_dmg)
            print(Bcolors.OKBLUE + "\n" + spell.name + " heals for ", str(magic_dmg), "HP " + Bcolors.ENDC)
        elif spell.type == "Black":
            enemy.take_damage(magic_dmg)
            print(Bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + Bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg)

    print("==================================")
    print("Enemy HP:", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")
    print("Your HP:", Bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Bcolors.ENDC + "\n")
    print("Your MP:", Bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You win!" + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + "You've been defeated!" + Bcolors.ENDC)
        running = False
