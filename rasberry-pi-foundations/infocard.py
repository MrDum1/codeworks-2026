name = "Walter"
age = 17
adult = False
interests = ["programming", "robotics", "gaming"]
why_here = "I want to learn more about Raspberry Pi and how to create innovative projects with it."
goals = "My goal is to become proficient in using Raspberry Pi for various applications and to contribute to the maker community."
personality = "I am curious, creative, and enjoy problem-solving. I like to explore new technologies and find ways to apply them in practical scenarios."

if age < 18:
    adult = False
else:
    adult = True

print("Name:", name)
print("Age:", age)
print("Interests:", ", ".join(interests))
print("Why I'm here:", why_here)
print("Goals:", goals)
print("Personality:", personality)

if adult:
    print("I am an adult.")


