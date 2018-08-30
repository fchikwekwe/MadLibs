# list of requirements:
# --get a name, country, a verb and an adjective from the user
# --insert noun, verb and adjective in order in story

name = input("What is your name? : ")
print("Your name is ", name)

adjective = input("Great! Now give me an adjective. : ")
print(adjective, "is a nice choice.")

country = input("What is your favorite country? : ")
print("Interesting! I have never been to ", country)

presentverb = input("And give me a present tense verb. : ")
print("Okay! I think we're ready.")


print("Hello {}! I hear that you live in {} {} where the sun don't {}.".format(name, adjective, country, presentverb))
