print("I dunno about you, but I could use a cup of tea...\n")

# Ascertain from input whether user has teabags.
teabags = input("Do you have teabags? (Please enter y/n)\n")
# If yes, ask if they have milk. If no, add teabags to shopping list... then ask if they have milk afterwards.
shopping_list = []
if teabags == "n":
    print("Well, how the heck are you going to make tea, doofus? Add teabags to yer shoppin' list.")
    shopping_list.append("teabags")
milk = input("What about milk, you got that?\n")
# If they don't, ask whether they take milk in their tea. If they don't, move on. If they do, it goes on the list.
if milk == "n":
    milk_pref = input("Right, so do you take milk in your tea?\n")
    if milk_pref == "y":
        print("Awright then, stick milk on the ol' shoppin' list.")
        shopping_list.append("milk")
sugar = input("Got any sugar?\n")
# Again, check preference if they don't.
if sugar == "n":
    sugar_pref = input("Right, and do you take sugar in your tea?\n")
    if sugar_pref == "y":
        print("Well, put sugar on yer shoppin' list.\n")
        shopping_list.append("sugar")
# Check if shopping list has anything on it. If it does, print out the list, then tell 'em to go shopping.
if len(shopping_list) > 0:
    print("OK, let's see how that shoppin' list is lookin' now...\n")
    for item in shopping_list:
        print(item)
    print("\nOff you pop to the shop, then. Toddle on.")
# Ask if the kettle's got water in it. Tell them to fill it, if not.
kettle = input("Have you got water in the kettle?\n")
if kettle == "n":
    print("Fill it, then, jeez. Is this like the first time you've done this or what? Don't... don't answer that.")
# Tell 'em to turn the kettle on and stick a teabag in the cup.
print("Get the kettle on, then! And stick a teabag in the cup while you're at it.")
# Tell 'em to pour water in the cup.
print("Kettle boiled? Awright then, fill yer cup. Carefully, mind, don't go splashin' it around like an eejit.")
# Check (again, potentially) if they take milk...
milk_pref = input("Milk?\n")
if milk_pref == "y":
    print("Go ahead, pour yer milk.")
# ... and/or sugar.
sugar_pref = input("Sugar?\n")
if sugar_pref == "y":
    print("Pour some sugar on it, baby.")
print("We good. Give it a minute to brew.")
print("Grab a teaspoon and give that teabag a good squeeze then take it outta the cup.")
print("You'll probably want to let that sit for a few minutes. If you don't, it ain't my fault if you burn your damn mouth.")
print("\nEnjoy!")

# Note: I personally would structure this differently to avoid double-asking the milk/sugar preference questions in the event that
# they say they don't have either or both (in which case they'll state preferences then, then again at the end of the flow).
# However, that'd kinda mess with the scope of the task set, and I've already done that a wee bit as it is by actually creating a list
# and printing it out if there's anything on it, rather than simply asking the user if they have stuff on the list.