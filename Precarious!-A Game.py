from sys import exit
from random import randint
from textwrap import dedent
import time

class Scene(object):

    """An abstract base class"""

    def enter():
        print("Not yet implemented!")
        exit(1)

class Health(object):

    """A simple player HP system"""

    hp = 6

    def hpcheck(self):
        time.sleep(2)
        print("")
        print("-" * 10)
        print(f"Your current health point is: {Health.hp}.")
        print("-" * 10)

        if Health.hp <= 0:
            print("\nYou have suffered too much to be saved.")
            print("Play again!")
            exit(0)

        else:
            pass

    def hpplus(self, val):
        Health.hp += val
        time.sleep(2)
        print(f"\nYou gained {val} hp!")

    def hpminus(self, val):
        Health.hp -= val
        time.sleep(2)
        print(f"\nYou lost {val} hp!")

player = Health()


class Inventory(object):

    """A simple inventory system. Can add or remove multiple items at a time."""

    gear = []

    def show_gears(self):
        print(Inventory.gear)

    def add_item(self, *args):
        self.args = args
        for item in self.args:
            Inventory.gear.append(item)

    def remove_item(self, *args):
        self.args = args
        for item in self.args:
            Inventory.gear.remove(item)

    def item_stat(self, item):
        self.item = item

        if item in Inventory.gear:
            return True

        else:
            return False

    def potion(self):
        time.sleep(2)
        print("\nHuh? There's a vial of *night vision potion* lying on the ground. Take it?")
        time.sleep(2)
        potion_answer = input("\nType y or n: ")

        if potion_answer == "y":
            backpack.add_item("night vision potion")
            time.sleep(2)
            print("\nYou got a *night vison potion*! Is it what it claims to be?")
        else:
            time.sleep(2)
            print("\nOkay. You leave the potion alone.")


backpack = Inventory()

# class Debugger(Scene):
#
#     """Used for debugging new features"""
#
#     def enter(self):
#         print("Check hp:")
#         player.hpcheck()
#         print("Add 5 hp:")
#         player.hpplus(5)
#         player.hpcheck()
#         print("Remove 2 hp:")
#         player.hpminus(2)
#         player.hpcheck()
#         print("Inventory stat:")
#         backpack.show_gears()
#         print("Add torch and rifle to inventory:")
#         backpack.add_item("torch", "rifle")
#         backpack.show_gears()
#         print("Remove torch:")
#         backpack.remove_item("torch")
#         print("Is torch in inventory?")
#         print(backpack.item_stat("torch"))
#         print("Is rifle in inventory?")
#         print(backpack.item_stat("rifle"))

class Death(Scene):

    why = [
        " because, alas, the chances were so against you.",
        ". You really should think before you act. Try again.",
        ". Don't be so rash!",
        ". You were sooo close...Try again."
    ]

    def enter(self):
        print("-" * 10)
        print("\n\nYou died{}".format(Death.why[randint(0, len(self.why)-1)]))
        print("-" * 10)
        exit(0)

class Dungeon_ent(Scene):

    def enter(self):
        time.sleep(1)
        print("\nYou are about to enter the ancient ruins.")
        time.sleep(1.5)
        reply = input("\nAre you prepared? Type yes or no: ")
        if reply == "yes":
            print("\nThen go in!")
            return 'hallway'
        else:
            return 'dungeon_ent'

class Hallway(Scene):

    def enter(self):
        time.sleep(2)
        print("\nYou enter a hallway. There are three gates.")
        time.sleep(2)
        print("\nWhich one do you want to enter?")
        time.sleep(2)
        response = input("\nType left, right, or forward: ")
        if response == "left":
            time.sleep(2)
            print("\nYou go through the gate to your left. Good luck!")
            return 'room1'

        elif response == "right":
            time.sleep(2)
            print("\nYou go through the gate to your right. Good luck!")
            return 'room2'

        else:
            return 'hallway'

class Room1(Scene):

    def enter(self):
        time.sleep(2)
        print("\nThe room is eeriely quiet.")
        time.sleep(2)
        print("\nSuddenly a dim, blue figure lights! It is a hologram.")
        time.sleep(2)
        print("\nThe hologram speaks:")
        time.sleep(2)
        print("\nI am Th...e..might..y...emperor...Jha...gz..emynnn [indistinguishable]...")
        time.sleep(2)
        print("\nTrespasser...")
        time.sleep(2)
        print("\nI charge...thee...")
        time.sleep(2)
        print("\nAnswer...thi...s...rid..dle...")
        time.sleep(2)
        print("\nOr run...for thy life...")
        time.sleep(2)
        print("\nMark...")
        time.sleep(2)
        print("\n\"What..is..fast..er...than...war...rp..drive?..Rea..per, ranger, or..r, reporters fr..rom..Houuhg..Koumg [indistinguishable]?...\"")
        time.sleep(2)
        answer_riddle = input("\nType reaper, ranger, or reporters from Houuhg-Koumg: ")


        if answer_riddle == "reporters from Houuhg-Koumg":
            time.sleep(2)
            print("\nThe hologram nods, and gives you 1 HP. You recognize this as the ancient practice of +1s.")
            player.hpplus(1)
            player.hpcheck()
            backpack.potion()
            time.sleep(2)
            print("\nYou proceed to the next room.")

            return 'trap_hallway'

        else:
            time.sleep(2)
            print("\nThe emperor gets mad at you. He shouts:\"Naive!\";\"You are still too young!\";\"I'm angry.\" And suddenly you feel life taken away from you.")
            time.sleep(2)
            print("\nYou have a bad feeling about this.")
            player.hpminus(2)
            player.hpcheck()
            backpack.potion()
            time.sleep(2)
            print("\nYou proceed to the next room.")

            return 'trap_hallway'

class Room2(Scene):

    def enter(self):
        time.sleep(2)
        print("\nThe room shakes no sooner than you enter it!")
        time.sleep(2)
        print("\nA huge mechanical guardian rose shakily, shaking off millenia of dust. It looks like a crab with a turret on top.")
        time.sleep(2)
        print("\nIt has started locking on you with a laser beam! It's now or never! Defend yourself!")
        time.sleep(2)
        print("\nA rusty railgun to your right was just activated. You find with great relief that it can be manually controlled; bad news is it probably can only fire once.")
        time.sleep(2)
        print("\nThe mechanical chimera is slowly rising. It's legs looks fragile, but there a many of them. It's \"eye\" is worth a shot, but it is protected well with multiple lenses. It's neck was just exposed to you, but the armor is probably thick.")
        time.sleep(2)
        print("\nDecide where to fire at!")
        time.sleep(2)
        fire_answer = input("\nType leg, eye or neck: ")

        if fire_answer == "neck":
            time.sleep(2)
            print("\nThe guardian's head falls clear off! The entire beast crumbles. Then there was silence. You defeated it!")
            time.sleep(2)
            print("\nYou even manage to scavenge a *droid service port*! Try use it on droids.")
            time.sleep(2)
            backpack.add_item("droid service port")
            time.sleep(2)
            print("\nYou proceed to the next room intact.")
            player.hpcheck()
            return 'room3'

        elif fire_answer == "eye":
            time.sleep(2)
            print("\nThe projectile pierces through many lenses but the eye is still largely intact.")
            time.sleep(2)
            print("\nThe guardian goes berserk at you and shot blue plasma. But its aim is affected so you are not too badly hurt. Then it exploded.")
            player.hpminus(1)
            player.hpcheck()
            time.sleep(2)
            print("\nYou even manage to scavenge a *droid service port*! Try use it on droids.")
            time.sleep(2)
            backpack.add_item("droid service port")
            time.sleep(2)
            print("\nYou are hurt but you proceed to the next room.")
            return 'room3'

        elif fire_answer == "leg":
            time.sleep(2)
            print("\nYou shoot off 2 legs, but 8 remain.")
            time.sleep(2)
            print("\nStill, the guardian temporarily loses balance and its shot does hit you squarely.")
            player.hpminus(2)
            player.hpcheck()
            time.sleep(2)
            print("\nYou are hurt, but you hide yourself and proceed to the next room while the beast recovers.")
            return 'room3'

        else:
            print("DOES NOT COMPUTE!")
            time.sleep(2)
            return 'room2'

class Room3(Scene):

    def enter(self):
        time.sleep(2)
        print("\nYou have entered an ancient edifice. It appears to be a library or database.")
        time.sleep(2)
        print("\nNow it has turned into a complete maze. Fortunately you have a map of it.")
        time.sleep(2)
        print(dedent("""
        ______  _____
        | 7|  _____ 4|
        |   1|_______|
        |  |_|  ___2 |
        |  |8 ____|  |
        |____|  _____|
        """))
        time.sleep(2)
        print("\nType the numbers on the beacons you encounter along the way to pass!")
        time.sleep(2)
        answer = input("\nBeacon sequence: ")

        if answer.isdigit():
            beacon = int(answer)
            if beacon == 281:
                time.sleep(2)
                print("\nYou walk out of the maze!")
                time.sleep(2)
                print("\nYou see dim light behind a wall. Investigate?")
                time.sleep(2)
                inves_answer = input("\nType y or n: ")
                if inves_answer == "y":
                    if randint(0, 3) < 2:
                        time.sleep(2)
                        print("\nHey, you see a disabled droid. Maybe it holds important information.")
                        time.sleep(2)
                        hack_answer = input("\nTry hacking droid? Type y or n: ")
                        if hack_answer == "y":
                            if backpack.item_stat("droid service port"):
                                time.sleep(2)
                                print("\n10001010101001010111001010101010101111101010" * 1000)
                                time.sleep(2)
                                print('\nAccessing encrypted files...')
                                time.sleep(2)
                                print('\nDecrypting....')
                                if randint(0,3) < 4:
                                    time.sleep(2)
                                    print("\n\n[SEN281 LOG-]")
                                    time.sleep(2)
                                    print("\n\n OVERRIDE CODE -- BUILTIN")
                                    time.sleep(2)
                                    print('\n\n-KRG - 4d7ve9o')
                                    time.sleep(2)
                                    print('\n\n SEN - rgt643i')
                                    time.sleep(2)
                                    print('\n\n-Impervious Grace - r58f7ti')
                                    time.sleep(2)
                                    print('\n\n-EliteCMD - tx39hdi')
                                    time.sleep(2)
                                    print('\n\n-TX9r99i..dkdf Drfds - ts++]?%')
                                    time.sleep(1)
                                    print("10001010101001010111001010101010101111101010" * 10)
                                    print("\n\n[System Report] Corrupt data. Further access failed.")
                                    backpack.add_item("code1")
                                    print("\nCool! This might come in handy.")
                                else:
                                    time.sleep(2)
                                    print("\nDecryption failed!")
                            else:
                                time.sleep(2)
                                print("\nYou do not have a *droid service port* to access droid memory bank.")
                        else:
                            time.sleep(2)
                            print("\nOkay. It's probably safer not to mess around.")
                    else:
                        time.sleep(2)
                        print("\nDodge! It's a sentry droid and it fired at you. You are hurt but fortunately it's set to stun.")
                        player.hpminus(1)
                        player.hpcheck()
                else:
                    time.sleep(2)
                    print("\nOkay. It's probably safer not to mess around.")
            else:
                time.sleep(2)
                print("\nYou stumble inside the building, get lost and eventually starved to death.")
                return 'death'
        else:
            time.sleep(2)
            print("\nYou did not type a number and the system locked you in.")
            return 'death'

        backpack.potion()
        player.hpcheck()
        time.sleep(2)
        print("\nYou proceed to the next room.")
        return 'trap_hallway'

class Trap_hallway(Scene):

    def enter(self):
        time.sleep(2)
        print("\nThis hallway is pitch dark.")
        time.sleep(2)
        print("\nYou unconsiously step backwards and step on a disconnected tripwire. Ancient technology haunts your path.")
        time.sleep(2)
        print("\nIt's a trap! You need to be able to see to get through.")
        time.sleep(2)

        if backpack.item_stat("night vision potion"):
            print("\nWhat do you do? Drink the suspicious *night vision potion*, or turn on the millenia old lighting system?")
            time.sleep(2)
            decision = input("\nType drink potion or turn on lighting: ")

            if decision == "drink potion":
                time.sleep(2)
                print("\nYou certainly feel nauseous...But you can see the hallway as in broad daylight.")
                time.sleep(2)
                print("\nOh! The agony! You are in pain, but you manage to get past all the hidden dangers and proceed to the next room.")
                player.hpminus(1)
                player.hpcheck()
                return 'combat_room'
            elif decision == "turn on lighting":
                time.sleep(2)
                print("\nYou turn on the lighting. You look at the hideous traps for one split second before alarms go off!")
                time.sleep(2)
                print("\nThe defense mechanisms spring to life! You try to take cover, but there's none.")
                time.sleep(2)
                print("\nThree energy blasts shoot you squarely in the chest. Fortunately they are set to stun, and after millenia the wattage is low.")
                time.sleep(2)
                print("\nYou survive but is hurt badly. You proceed to the next room.")
                player.hpminus(3)
                player.hpcheck()
                return 'combat_room'
            else:
                print("DOES NOT COMPUTE!")
                time.sleep(2)
                return 'trap_hallway'
        else:
            print("\nI am afraid you have to turn on the millenia old lighting system.")
            decision = input("\nType turn on lighting: ")

            if decision == "turn on lighting":
                time.sleep(2)
                print("\nYou turn on the lighting. You look at the hideous traps for one split second before alarms go off!")
                time.sleep(2)
                print("\nThe defense mechanisms spring to life! You try to take cover, but there's none.")
                time.sleep(2)
                print("\nThree energy blasts shoot you squarely in the chest. Fortunately they are set to stun, and after millenia the wattage is low.")
                time.sleep(2)
                print("\nYou survive but is hurt badly. You proceed to the next room.")
                player.hpminus(3)
                player.hpcheck()
                return 'combat_room'
            else:
                print("DOES NOT COMPUTE!")
                time.sleep(2)
                return 'trap_hallway'


class Combat_room(Scene):

    def enter(self):
        time.sleep(2)
        print("\nYou enter what seems to be a control room.")
        time.sleep(2)
        print("\nAn elite command droid is posted here! It sustains itself on energy pumped from fusion reactors below.")
        time.sleep(2)
        print("\nThis droid is very powerful.")
        time.sleep(2)
        print("\nDo you try sneak past it quietly, or duel with it?")
        time.sleep(2)
        combat_answer = input("\nType sneak or duel: ")

        if combat_answer == "sneak":
            if randint(0, 3) < 2:
                time.sleep(2)
                print("\nYou successfully sneak past it. What luck!")
                return 'boss'
            else:
                time.sleep(2)
                print("\nThe droid spots you! You hear the screeching sound of a target lock. A fusillade then followed.")
                player.hpminus(3)
                player.hpcheck()
                time.sleep(2)
                print("\nWhat a miracle! You survive and proceed to the next room.")
                return 'boss'

        elif combat_answer == "duel":
            time.sleep(2)
            print("\nYou hop onto the droid's neck and assault it with a monkey wrench.")
            if player.hp >= 3:
                time.sleep(2)
                print("\nIt's more effective than you previously think! You are strong enough that the droid cannot shake you off.")
                time.sleep(2)
                print("\nThe droid crumpled. Would you like to look at its memory banks?")
                time.sleep(2)
                hack_answer = input("\nType y or n: ")
                if hack_answer == "y":
                    if backpack.item_stat("droid service port"):
                        print("")
                        print("10001010101111001010001101111101010" * 1000)
                        time.sleep(2)
                        print('\nAccessing encrypted files...')
                        time.sleep(2)
                        print('\nDecrypting....')
                        if randint(0,3) < 4:
                            time.sleep(2)
                            print("\n\n[CMD479 LOG-]")
                            time.sleep(2)
                            print("\n\n -Impervious Grace Maintenance -- CLASSIFIED")
                            time.sleep(2)
                            print('\n\n[ADMIN OVERRIDE]-Impervious Grace - r58f7ti')
                            time.sleep(2)
                            print('\n\nMaintenance port located on plate 13, {the back}.')
                            time.sleep(2)
                            print('\n\n-StsdaRd pr0ceDur53 - ts84hfbidn++]?%')
                            time.sleep(1)
                            print("")
                            print("1000101011110100101001010111001010101010101111101010" * 10)
                            time.sleep(2)
                            print("\n\n[System Report] Corrupt data. Further access failed.")
                            backpack.add_item("code2")
                            print("Cool! This might come in handy.")
                        else:
                            time.sleep(2)
                            print("\nDecryption failed!")
                    else:
                        time.sleep(2)
                        print("\nYou do not have a *droid service port* to access droid memory bank.")
                else:
                    time.sleep(2)
                    print("\nOkay. It's probably safer not to mess around.")

            else:
                time.sleep(2)
                print("\nYou are too weak to do much serious damage. The droid shook you off and...")
                return 'death'

        else:
            time.sleep(2)
            print("DOES NOT COMPUTE!")
            return "combat_room"

        player.hpcheck()
        time.sleep(2)
        print("\nYou proceed to the next room.")
        return 'boss'

class Boss(Scene):

    def enter(self):
        time.sleep(2)
        print("\nYou look into the room and immediately realize that you have arrived at last.")
        time.sleep(2)
        print("\nAn obsidian tablet stands in the middle of the room, on a triangular pedestal.")
        time.sleep(2)
        print("\nYou slowly approach the sacred object, awe-struck.")
        time.sleep(2)
        print("\nYou reach out to it...")
        time.sleep(2)
        print("\nNo! A cracking sound boomed in the room. A guardian automaton rose. It is white, scorpion-like, dust-covered but emanating soft light.")
        time.sleep(2)
        print("\nIt looks hideous, and also invincible. It's totally covered in porcelain armour, and you cannot find even one weak point.")
        time.sleep(2)
        print("\nHaving no mood to marvel at ancient technology, you run to arm yourself.")
        time.sleep(2)
        print("\nYou find a railgun that shoots deadly projectiles, and a plasma cutter. Which one will stand against the beast?")
        time.sleep(2)
        print("\nWhich weapon will you use?")
        time.sleep(2)
        weapon = input("\nType railgun, plasma cutter, or something else: ")

        if weapon == "railgun":
            time.sleep(2)
            print("\nYou manage to knock the automaton over!")
            time.sleep(2)
            print("\nIt manages to fire a shot at you, but you are not too badly hurt.")
            player.hpminus(2)
            player.hpcheck()
            time.sleep(2)
            print("\nIt tries to get up, and in the commotion grab the obsidian tablet and ran away.")
            return 'win'

        elif weapon == "plasma cutter":
            time.sleep(2)
            print("\nYou cut its tail off. It loses it primary weapon!")
            time.sleep(2)
            print("\nBut it still manages to hit you with one of its mechanical legs. Fortunately the damage is relatively light.")
            player.hpminus(1)
            player.hpcheck()
            time.sleep(2)
            print("\nYou then swiftly maim the beast more and more. Eventually it crumbles. You grab the obsidian tablet and walk away.")
            return 'win'

        elif weapon == "something else":

            if backpack.item_stat("code1") or backpack.item_stat("code2") and backpack.item_stat("droid service port"):
                time.sleep(2)
                print("\nWhat do you do? Manual override? This suddenly occured to you.")
                time.sleep(2)
                answer = input("\nType override: ")

                if answer == "override":
                    time.sleep(2)
                    print("\nYou swiftly circle the automaton, searching for the service port.")
                    time.sleep(2)
                    print("\nThere it is! You plug in your console and try to hack.")
                    time.sleep(2)
                    print("100101010001010101010111010101" * 1000)
                    print("\n\n")
                    time.sleep(2)
                    print("-" * 40)
                    time.sleep(2)
                    print("-Impervious Grace Maintenance Interface-")
                    time.sleep(2)
                    print("\n[You are not the administrator of this system]")
                    time.sleep(2)
                    print("\nCurrent automaton action: Neutralize all intruders.")
                    time.sleep(2)
                    print("\nWith shakey fingers you type:")
                    time.sleep(2)
                    print("\n[User]Type sudo override\n")
                    time.sleep(1.5)
                    password = input("Admin override password: ")

                    if password == "r58f7ti":
                        time.sleep(2)
                        print("\nAdmin action override...")
                        time.sleep(2)
                        print("100101010001010101010111010101" * 1000)
                        time.sleep(2.56)
                        print("\n\n Command complete in 2.56 sec")
                        print("-" * 10)
                        time.sleep(2)
                        print("\nThe automaton settles down. You just casually grab the obsidian tablet and go away!")
                        player.hpcheck()
                        return 'win'
                    else:
                        print("\nIncorrect password. Access denied.")
                        time.sleep(2)
                        print("\nThe automaton roars and sends you crashing into the floor.")
                        return 'death'
            else:
                print("You really can't try anything else.")
                return 'boss'

        else:
            time.sleep(2)
            print("\nDOES NOT COMPUTE!")
            return "boss"

class Win(Scene):

    def enter(self):
        time.sleep(2)
        print("\nYou obatined the obsidian tablet, the sacred artifact from the deadly ruins! You won!")
        time.sleep(2)
        print("\nThank you for playing this game. Copyright Calvin Xu.")
        time.sleep(2)
        print("\n2017.7.24")
        time.sleep(2)
        exit(0)

class SceneDirector(object):

    scenes = {
        'dungeon_ent': Dungeon_ent(),
        'hallway': Hallway(),
        'room1': Room1(),
        'room2': Room2(),
        'room3': Room3(),
        'trap_hallway': Trap_hallway(),
        'combat_room': Combat_room(),
        'boss': Boss(),
        'death': Death(),
        'win': Win()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        scene_instance = SceneDirector.scenes.get(scene_name)
        return scene_instance

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):

        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('win')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

print("\n")
print("-" * 33)
print("Precarious! - A Game by Calvin Xu")
print("-" * 33)

time.sleep(2)

Scene_instances = SceneDirector('dungeon_ent')

game = Engine(Scene_instances)

game.play()
