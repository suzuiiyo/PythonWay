from sys import exit

def gold_room():
    next = raw_input()
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Oops, you need to learn how to type a number")

    if how_much < 50:
        print "Great, not a greedy man, you win!"
        exit(0)
    else:
        dead("You greedy bastrad!")

def bear_room():
    print "there is a bear here."
    print "the bear has a bunch of honey."
    print "the fat bear is in front of another room."
    print "how are you going to move the bear?"
    bear_move = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go throgh the door now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your legs off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "here you see the great evil cthulhu"
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee your life or eat your head?"

    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "you are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
