import re

dane = open('dane.txt').readline().strip()

#Zadanie 7.1.
print(len(list(filter(lambda x: x.startswith('50'), re.findall(r'\d+', dane)))))

#Zadanie 7.2.
print('\n'.join(list(filter(lambda x: x.startswith('5') and len(x) == 9, re.findall(r'\d+', dane)))))