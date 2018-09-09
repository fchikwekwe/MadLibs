# list of requirements:
# --get a name, country, a verb and an adjective from the user
# --insert noun, verb and adjective in order in story
# If country get "the" in front of it have a conditional statement that adds it
# If user inputs something that is not a country from the list of countries, then have a way to replace their input with a random name from the country list

import random

countries = ["Macedonia", "macedonia", "Madagascar", "madagascar", "malawi","Malawi", "Malaysia", "malaysia", "Maldives", "maldives", "the Maldives", "the maldives", "Mali", "mali", "Malta", "malta", "Marshall Islands", "marshall islands", "the Marshall Islands", "the marshall islands", "Mauritania", "mauritania", "Mauritius", "mauritius", "Mexico", "mexico", "Micronesia", "micronesia", "the Federated States of Micronesia", "the federated states of micronesia", "Moldova", "moldova", "Monaco", "monaco", "Mongolia", "mongolia", "Montenegro", "montenegro", "Morocco", "morocco", "Myanmar", "myanmar", "Mozambique", "mozambique"]
climate = {0 : "polar", 1 : "mediterranean", 2 : "temperate", 3 : "arid", 4 : "tundra", 5 : "swampy", 6 : "desert" , 7 : "tropical"}
food = ["buttered popcorn", "potato chips", "paella", "chicken and rice", "poutine", "tacos", "toast with marmite", "stinky tofu", "marzipan", "ketchup", "french toast", "papaya", "plantain", "chicken parm", "hummus", "maple syrup", "bananas"]

finalcountry = random.choice(countries)
finalfood = random.choice(food)

def countryfunction():
    if country in countries:
        print("Interesting! I have never been to", country)
    else:
        print("Here! Let me help you out. Let's go with", finalcountry)

name = input("What is your name? : ")
print("Your name is", name)

adjective = input("Great! Now give me an adjective. : ")
print(adjective, "is a nice choice.")

country = input("Name a country that starts with the letter 'M' : ")
countryfunction()

presentverb = input("And give me a present tense verb e.g. walk, scream, remember : ")

storyword = input("Give me another word for a story : ")

pluralnoun = input("Alright, now I need a plural noun : ")

pluralnoun1 = input("...give me another a plural noun : ")

adjective2 = input("...a final adjective : ")

pluralnoun2 = input("...and one more plural noun! : ")

nouns = [pluralnoun, pluralnoun1, pluralnoun2]
random.shuffle(nouns)

# def climate(prompt):
#     while True:
#         try:
#             climate = int(input(prompt))
#         except ValueError:
#             print("Please make sure your selection is a number.")
#             continue
#         else:
#             break
#         return climate
#
# finalclimate = climate("Pick a number 0 - 7 : ")
# print(finalclimate)

finalclimate = input("Pick a number 0 - 7 : ")

print("Okay! I think we're ready.")

def finalstory():
    if country in countries:
        print("Hello {}! I hear that you live in {} {} where the sun don't {}. From the {} of old, it seems you have {}, {} and {} {} out there. In such a {} region like that, people often eat {}! ".format(name, adjective, country, presentverb, storyword, nouns[0], nouns[1], adjective2, nouns[2], climate[int(finalclimate)], finalfood))
    else:
        print("Hello {}! I hear that you live in {} {} where the sun don't {}. From the {} of old, it seems you have {}, {} and {} {} out there. In such a {} region like that, people often eat {}! ".format(name, adjective, finalcountry, presentverb, storyword, nouns[0], nouns[1], adjective2, nouns[2], climate[int(finalclimate)], finalfood))

finalstory()

def test ():
    print(countryfunction)
    print(nouns)
    print(climate[0])
    print(climate[int(finalclimate)])

# test()
