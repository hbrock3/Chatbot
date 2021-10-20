import re

# Can use (\w+?)(?=ly|es|(?<!s)s|y) to stem, but didn't feel the need to? I think?

print("Welcome to my chatbot! Feel free to answer in sentences, single words, or with nothing at all. The chatbot will respond to any of these inputs.")

answer = input("Hello! I'm a chatbot, what's your name?\n")
if re.match(r'\A[\w-]+\Z', answer):
    name = answer
elif answer == "" or answer == None:
    name = input("TELL ME YOUR NAME! NOW!\n")
else:
    name = re.search(r"name is\s*(\w*)\b", answer).group(1)

# This means they didn't respond to "TELL ME YOUR NAME! NOW!"
if name == "":
    name = "stranger"

answer = input("Hey " + name + ", nice to meet you. How are you?\n")

if re.match(r'\A[\w-]+\Z', answer):
    print("I am also feeling " + answer + ", " + name + "!")
elif answer == "" or answer == None:
    print("That's ok, you don't have to tell me. :)")
else:
    feeling = re.search(r"(?:feeling|I am|I'm|i am|i'm)\s*(\w*)\b", answer).group(1)
    print("I am also feeling " + feeling + ", " + name + "!")

answer = input("So what's your favorite animal?\n")

if re.match(r'\A[\w-]+\Z', answer):
    print(answer + "'s are my favorite animal too!")
elif answer == "" or answer == None:
    print("Don't have one? Ok...")
else:
    animal = re.search(r"(?:is|are)\s*(\w*)\b", answer).group(1)
    print(animal + "'s are my favorite animal too!")

answer = input("Favorite vegetable?\n")

if re.match(r'\A[\w-]+\Z', answer):
    print(answer + "?! Gross. I won't talk to someone who likes " + answer + ". Bye, " + name + "!")
elif answer == "" or answer == None:
    print("Don't have one? Ok...")
else:
    veggie = re.search(r"is\s*(\w*)\b", answer).group(1)
    print(veggie + "?! Gross. I won't talk to someone who likes " + answer + ". Bye!" + name + "!")
