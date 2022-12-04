file = open('day03_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    bag = line.strip("\n")
    source.append(bag)

def return_number(i):
    if ord(i) > 96:
        number = ord(i) - 96
    elif ord(i) > 64:
        number = ord(i) - (64 - 26)
    return(number)

if len(source) % 3 != 0:
    print("Error, indivisible by three")
    exit()

resume = []
for i3 in range(0, len(source), 3):
    for l in source[i3]:
        if l in source[i3 + 1] and l in source[i3 + 2]:
            marker = [int(i3 / 3 + 1), l, return_number(l)]
            if marker not in resume:
                resume.append(marker)

suma = 0
for i in resume:
    suma += i[2]
    print(i)

print(suma)
