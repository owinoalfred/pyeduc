thing = "alfred is the loonnggeest"


longest = ""
splitted = thing.split()

for thing in splitted:
    if len(thing) > len(longest):
        longest = thing
print(longest)