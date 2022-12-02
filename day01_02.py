file = open('day01_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
set_ = []
for line in lines:
    if line !="\n":
        temp = line.strip("\n")
        set_.append(int(temp))
    else:
        source.append(set_)
        set_ = []

result = []
for i, set_ in enumerate(source):
    suma = sum(set_)
    result.append([i,suma])

result.sort(key=lambda x: x[1])

suma = 0
for s in result[-3:]:
    print(s)
    suma += s[1]

print("Result of part 2:", suma)