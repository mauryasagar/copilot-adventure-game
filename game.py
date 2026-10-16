def choice(prompt, options):
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        try:
            pick = int(input("\n> "))
            if 1 <= pick <= len(options):
                return pick
        except ValueError:
            pass
        print("Pick a valid number.")

def win(msg):
    print(f"\n✅ {msg}")
    print("="*40)
    print("       YOU WIN!")
    print("="*40)

def lose(msg):
    print(f"\n💀 {msg}")
    print("="*40)
    print("       GAME OVER")
    print("="*40)

def forest_path():
    print("\nYou follow the river downstream and find an old bridge.")
    c = choice("A troll blocks your path. What do you do?", [
        "Try to fight the troll",
        "Offer your gold coins",
        "Sneak around through the mud"
    ])
    if c == 1:
        lose("The troll was twice your size. You lasted about 4 seconds.")
    elif c == 2:
        print("\nThe troll takes your coins and steps aside, grumbling.")
        c2 = choice("Across the bridge is a village. You see smoke rising. What now?", [
            "Run toward the smoke to help",
            "Sneak around the village"
        ])
        if c2 == 1:
            win("You helped put out a fire and saved a family. They reward you with a horse and safe passage home.")
        else:
            lose("You got lost in the woods for days. Nobody found you.")
    else:
        print("\nYou slip through unnoticed but fall into the mud.")
        c2 = choice("You're soaked and cold. A farmhouse is nearby.", [
            "Knock on the door and ask for help",
            "Break into the barn to sleep"
        ])
        if c2 == 1:
            win("A kind farmer gives you dry clothes, a meal, and directions home. Made it!")
        else:
            lose("The farmer finds you, thinks you're a thief, and calls the guards. Rough day.")

def cave_path():
    print("\nThe cave is dark but you can hear water dripping inside.")
    c = choice("You see a faint glow deeper in. What do you do?", [
        "Head toward the light",
        "Stay near the entrance and call out",
        "Leave — this feels wrong"
    ])
    if c == 1:
        print("\nYou find a small dragon sleeping next to a pile of gold.")
        c2 = choice("What do you do?", [
            "Grab some gold and run quietly",
            "Back away slowly and leave",
            "Try to befriend the dragon"
        ])
        if c2 == 1:
            lose("You knocked over a coin. The dragon woke up. You know the rest.")
        elif c2 == 2:
            print("\nYou make it out safely but with nothing.")
            lose("You wandered the forest for weeks. No gold, no glory.")
        else:
            win("The dragon was lonely. You two become unlikely friends and it flies you home.")
    elif c == 2:
        lose("Something called back. You really should not have gone in after it.")
    else:
        win("Smart. You found a trail near the cave entrance that led straight back to town. Sometimes leaving is winning.")

def start():
    print("="*40)
    print("     LOST IN THE DARK FOREST")
    print("="*40)
    print("\nYou wake up alone in a forest with no memory of how you got here.")
    print("It's getting dark. You need to find a way out.")

    c = choice("You spot two paths ahead.", [
        "Take the left path toward a river",
        "Take the right path toward a cave"
    ])

    if c == 1:
        forest_path()
    else:
        cave_path()

    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again == "y":
        start()
    else:
        print("\nThanks for playing!")

start()
