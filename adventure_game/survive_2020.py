import time
import random
import unicodedata


def print_pause(output):
    print(output)
    time.sleep(1)


def main_intro():
    random_catastrophe = random.choice(["bomb threats from North Korea",
                                        "volcano eruption in Taal",
                                        "floods in several countries",
                                        "vegetation in the Himalayaas"])
    for i in [3, 2, 1]:
        print_pause(f'"{i}!.."')
    print_pause('"HAPPY NEW YEAR!!" Everybody shouted with excitement.')
    print_pause("...")
    print_pause("First day of 2020:")
    print_pause('"AUSTRALIA IS BEING RAVAGED BY THE WORST WILDFIRE SEEN IN"')
    print_pause('"DECADES..."')
    print_pause("A foreboding news on TV was just the beginning...")
    print_pause(f"The catastrophic {random_catastrophe},")
    print_pause("a deadly spread of Coronavirus and world-wide lockdown,")
    print_pause("outbursts of the socially draught...")
    print_pause(" ")


def start_game(items_list, meal):
    start_response = input("HOW WILL YOU SURVIVE 2020?\n"
                           "Press 'y' to start, 'n' to exit\n").lower()
    if start_response != 'n':
        if start_response == 'y':
            game_intro(items_list, meal)

        else:
            print_pause("Please enter 'y' or 'n'")
            start_game(items_list, meal)
    else:
        print("Good bye!")


def game_intro(items_list, meal):
    your_name = input("Please type in your name:\n"
                      ">")
    print_pause(f"{your_name},")
    print_pause("You hear an unbelievable news on the radio:")
    print_pause("New virus is inducing zombie-like behaviors...")
    print_pause(" ")
    print_pause("All of a sudden,")
    print_pause("you hear a horrendous scream of death,")
    print_pause("followed by a moment of silence...")
    print_pause("Neighbors are bolting out, and you quickly get in your car.")
    choose_route(items_list, meal)


def choose_route(items_list, meal):
    print_pause("Where to?")
    zombie_choices = input("1) Speed to the groceries.\n"
                           "2) Find the underground hideout.\n"
                           "3) Gather firewood\n")
    if zombie_choices == '1':
        first_stop(items_list, meal)
    elif zombie_choices == '2':
        second_stop(items_list, meal)
    elif zombie_choices == '3':
        third_stop(items_list, meal)
    else:
        print_pause("Sorry, that's not an option.\n")
        choose_route(items_list, meal)


def first_stop(items_list, meal):

    print_pause("You speed to the nearest groceries.")

    if meal in items_list:
        if 'firewood' in items_list:
            print_pause("It's time to kill those zombies!")
        else:
            print_pause("However, there's no more room in the trunk,")
            print_pause("Zombies are approaching, Hurry!")

    else:
        print_pause("After grabbing as much food as possible,")
        print_pause("you run back to your car.")
        print_pause("Zombies are approaching, Hurry!")
        items_list.append(meal)
    choose_route(items_list, meal)


def second_stop(items_list, meal):

    print_pause("You arrive at the underground hideout,")
    print_pause("and politely ask others to help gather firewood.")
    print_pause("People are complaining.")
    print_pause("They seem hangry.")

    if meal in items_list:
        print_pause("Fortunately, you have enough {} "
                    "and {}!".format(meal[0], meal[1]))
        print_pause("Happy and satisfied,")
        print_pause("People help to gather enough firewood.")
        print_pause(" ")
        items_list.append('firewood')

    else:
        print_pause("Uh oh, you don't have anything to feed them.")
    choose_route(items_list, meal)


def third_stop(items_list, meal):

    if 'firewood' in items_list:
        print_pause("You and the others set the firewoods on fire ")
        print_pause("and throw one by one...")
        print_pause("The number of zombies are decreasing!")
        print_pause("You save your town from the zombie apocalype,")
        print_pause("and make it through the year 2020! Hooray!!"
                    "{}".format(unicodedata.lookup("white smiling face")))

    else:
        print_pause("You don't have any weapons to defeat the zombies...")
        if meal in items_list:
            print_pause("People are getting hangry...")

        choose_route(items_list, meal)


def run_game():
    items_list = []
    random_supplies = [['water', 'baked potatoes'],
                       ['milk', 'cereal'],
                       ['soda', 'pizza'],
                       ['coffee', 'bagels']]
    meal = random.choice(random_supplies)
    main_intro()
    start_game(items_list, meal)


run_game()
