file = open('day03_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    lenght = len(temp)
    if lenght % 2 != 0:
        print("Error odd")
        exit()
    l_2 = int(lenght / 2)
    bag = [temp[:l_2], temp[l_2:]]
    source.append(bag)

def return_number(i):
    if ord(i) > 96:
        number = ord(i) - 96
    elif ord(i) > 64:
        number = ord(i) - (64 - 26)
    return(number)

resume = []
for n, bag in enumerate(source):
    for l in bag[0]:
        if l in bag[1]:
            double = [n, l, return_number(l)]
            if double not in resume:
                resume.append(double)

suma = 0
for i in resume:
    suma += i[2]
    print(i)

print(suma)

