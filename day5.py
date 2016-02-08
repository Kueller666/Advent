FILE = "input 2.txt"
count = 0

with open(FILE) as f:
    for line in f.readlines():
        Dubbel = False
        sprong = False
        for pos in range(len(line)-3):
            if line[pos:(pos+2)] in line[(pos+2):]: Dubbel = True
            if line[pos] == line[pos+2]: sprong = True

        if Dubbel and sprong:
            count+=1

print(count)