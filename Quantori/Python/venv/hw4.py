import re
text = input("write your line : ")
regular = r"\d+"
# если быть честным, то тут происходит магия из интернета (когда нибудь я её пойму).
filtertext = list(map(int, re.findall('-?[0-9]+', text)))
result= sum(filtertext)
print(result)
