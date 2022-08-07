# String concatenation
# Suppose we want to create a string that says "subscribe to _____"
# youtuber = "Ryan James"  # some string variable

# 3 ways to do this:
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because " \
         f"I live to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
