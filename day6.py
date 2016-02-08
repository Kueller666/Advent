FILE = "day6.txt"
matrix = [[0 for _ in range(1000)] for z in range(1000)]
dicta = {"on": 1, "off": -1, "toggle": 2}
count = 0


def toggle(coord1, coord2):
    for y in range(coord1[0], coord2[0]+1):
        for x in range(coord1[1], coord2[1]+1):
            if matrix[y][x]:
                matrix[y][x] = False
            else:
                matrix[y][x] = True


def turn(coord1, coord2, onoff):
    onoff = dicta[onoff]
    for y in range(coord1[0], coord2[0]+1):
        for x in range(coord1[1], coord2[1]+1):
            matrix[y][x] += onoff
            if matrix[y][x] < 0:
                matrix[y][x] = 0


def uitelkaar(tekst):
    nieuw = tekst.split(",")
    intlist = []
    for i in nieuw:
        intlist.append(int(i))
    return intlist


with open(FILE) as f:
    for line in f.readlines():
        instruction = line.split(" ")
        if instruction[0] == "toggle":
            turn(uitelkaar(instruction[1]), uitelkaar(instruction[3]), instruction[0])
        else:
            turn(uitelkaar(instruction[2]), uitelkaar(instruction[4]), instruction[1])

for y in matrix:
    for x in y:
        count += x
print(count)
