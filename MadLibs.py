

import random
from termcolor import colored

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

current_words = ["plural_noun1", "plural_noun2", "adjective2"]
prompt_texts = ["please choose another plural noun. ", "...and one more plural noun please. ", "please choose one more adjective. "]
new_words = []

# need to check plural nouns and adjectives to make sure they are not the same before accepting
def check_if_same (current_word, check_word, check_word1, prompt_text):
    true_condition = True
    while true_condition:
        current_word = input(prompt_text)
        if current_word == check_word or current_word == check_word1:
            print(colored("Please make sure that your choice is unique. ", "green", attrs=["bold"]))
        else:
            true_condition = False
            new_words.append(current_word)
            return current_word

name = input("What is your name? : ")
print("Your name is", name)

adjective = input("Great! Now give me an adjective. : ")
print(adjective, "is a nice choice.")

country = input("Name a country that starts with the letter 'M' : ")
country_function()

present_verb = input("And give me a present tense verb e.g. walk, scream, remember : ")

story_word = input("Give me another word for a story e.g. fable, legend : ")

plural_noun = input("Alright, now I need a plural noun : ")

# check if this plural noun is the same as the first one input by player
check_if_same(current_words[0], plural_noun, plural_noun, prompt_texts[0])

# checking this one against both plural nouns already given
check_if_same(current_words[1], plural_noun, new_words[0], prompt_texts[1])

#checking this one against adjective already given
check_if_same(current_words[2], adjective, adjective, prompt_texts[2])

nouns = [plural_noun, new_words[0], new_words[1]]
random.shuffle(nouns)

climate_unvalidated = True
while climate_unvalidated:
    final_climate = input("Pick a number 0 - 7 : ")
    try:
        if int(final_climate) > 7 or int(final_climate) < 0:
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
        print(colored("Hello {}! I hear that you live in {} {} where the sun don't {}. From the {} of old, it seems you have {}, {} and {} {} out there. In such a {} region like that, people often eat {}! ", "cyan", attrs=["bold"]).format(name, adjective, country, present_verb, story_word, nouns[0], nouns[1], new_words[2], nouns[2], climate[int(final_climate)], final_food))
    else:
        print(colored("Hello {}! I hear that you live in {} {} where the sun don't {}. From the {} of old, it seems you have {}, {} and {} {} out there. In such a {} region like that, people often eat {}! ", "cyan", attrs=["bold"]).format(name, adjective, final_country, present_verb, story_word, nouns[0], nouns[1], new_words[2], nouns[2], climate[int(final_climate)], final_food))

final_story()

def test ():
    print(country_function)
    print(nouns)
    print(climate[0])
    print(climate[int(final_climate)])

# test()
