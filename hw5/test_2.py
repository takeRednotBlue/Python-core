import re

s = "I bought 777 nuts for 6$ and 110 bolts for 3$."

print(re.findall("(\d){3}", s)) 
print(re.findall("[\d]{3}", s)) 