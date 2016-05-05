from sys import exit

def gold_room():
    print("this room if full of gold. how much do you take?")
    next = input("> ")

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("nice, you're not greedy, you win")
        exit(0)
    else:
        dead("you greedy bastard")

def bear_room():

    print("""there is a bear here
          the bear has a bunch of honey
          and the bear is in front of the door
          how are you going to move the bear""")

    bear_moved = False

    while True:

        next = input("> ")

        if next == "take honey":
            dead("the bear looks at you and then slaps your face off")

        elif next == "taunt bear" and not bear_moved:
            print("the bear has moved from the door. you shall pass")
            bear_moved = True

        elif next == "taunt bear" and bear_moved:
            dead("the bear goes pissed off and chews your leg off")

        elif next == "open door" and bear_moved:
            gold_room()

        else:
            print("i got no idea what that means.")

def cthulhu_room():
    print("""here you see the great evil
    it stares at you
    do you Flee for you life you eat your Head?
    """)

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("WELL, that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "good job")
    exit(0)

def start():
    print("""you are in a dark room
    there is a door to your RIGHT and LEFT
    which one you take?
    """)

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room untill you starve.")

start()