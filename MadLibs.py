# list of requirements:
# --get a name, country, a verb and an adjective from the user
# --insert noun, verb and adjective in order in story
# If country get "the" in front of it have a conditional statement that adds it
# If user inputs something that is not a country from the list of countries, then have a way to replace their input with a random name from the country list

import random

countries = ["Macedonia", "macedonia", "Madagascar", "madagascar", "malawi","Malawi", "Malaysia", "malaysia", "Maldives", "maldives", "the Maldives", "the maldives", "Mali", "mali", "Malta", "malta", "Marshall Islands", "marshall islands", "the Marshall Islands", "the marshall islands", "Mauritania", "mauritania", "Mauritius", "mauritius", "Mexico", "mexico", "Micronesia", "micronesia", "the Federated States of Micronesia", "the federated states of micronesia", "Moldova", "moldova", "Monaco", "monaco", "Mongolia", "mongolia", "Montenegro", "montenegro", "Morocco", "morocco", "Myanmar", "myanmar", "Mozambique", "mozambique"]
climate = {0 : "polar", 1 : "mediterranean", 2 : "temperate", 3 : "arid", 4 : "tundra", 5 : "swampy", 6 : "desert" , 7 : "tropical"}
food = ["buttered popcorn", "potato chips", "paella", "chicken and rice", "poutine", "tacos", "toast with marmite", "stinky tofu", "marzipan", "ketchup", "french toast", "papaya", "plantain", "chicken parm", "hummus", "maple syrup", "bananas"]

final_country = random.choice(countries)
final_food = random.choice(food)

def country_function():
    if country in countries:
        print("Interesting! I have never been to", country)
    else:
        print("Here! Let me help you out. Let's go with", final_country)

name = input("What is your name? : ")
print("Your name is", name)

adjective = input("Great! Now give me an adjective. : ")
print(adjective, "is a nice choice.")

country = input("Name a country that starts with the letter 'M' : ")
country_function()

present_verb = input("And give me a present tense verb e.g. walk, scream, remember : ")

story_word = input("Give me another word for a story e.g. fable, legend : ")

plural_noun = input("Alright, now I need a plural noun : ")

check_plurals_same = True
while check_plurals_same:
    plural_noun1 = input("...give me another a plural noun : ")
    if plural_noun1 == plural_noun:
        print("Please make sure your plural nouns are different! ")
    else:
        check_plurals_same = False

check_adjectives_same = True
while check_adjectives_same:
    adjective2 = input("...a final adjective : ")
    if adjective2 == adjective:
        print("Please choose a different adjective this time. ")
    else:
        check_adjectives_same = False

check_plurals_same_again = True
while check_plurals_same_again:
    plural_noun2 = input("...and one more plural noun! : ")
    if plural_noun2 == plural_noun or plural_noun2 == plural_noun1:
        print("Please make sure your plural nouns are different!")
    else:
        check_plurals_same_again = False


nouns = [plural_noun, plural_noun1, plural_noun2]
random.shuffle(nouns)

climate_unvalidated = True
while climate_unvalidated:
    final_climate = input("Pick a number 0 - 7 : ")
    try:
        if int(final_climate) > 7 or int(final_climate) < 1:
            print("Your selection has to be between 0 and 7 to be valid.")
        elif final_climate.isdigit() == True:
            climate_unvalidated = False
        else:
            print("Please make sure that your selection is a number between 0 and 7")
    except ValueError:
        print("Your selection has to be a whole number between 0 and 7 to be valid.")

print("Okay! I think we're ready.")

def final_story():
    if country in countries:
        print("Hello {}! I hear that you live in {} {} where the sun don't {}. From the {} of old, it seems you have {}, {} and {} {} out there. In such a {} region like that, people often eat {}! ".format(name, adjective, country, present_verb, story_word, nouns[0], nouns[1], adjective2, nouns[2], climate[int(final_climate)], final_food))
    else:
        print("Hello {}! I hear that you live in {} {} where the sun don't {}. From the {} of old, it seems you have {}, {} and {} {} out there. In such a {} region like that, people often eat {}! ".format(name, adjective, final_country, present_verb, story_word, nouns[0], nouns[1], adjective2, nouns[2], climate[int(final_climate)], final_food))

final_story()

def test ():
    print(country_function)
    print(nouns)
    print(climate[0])
    print(climate[int(final_climate)])

# test()
