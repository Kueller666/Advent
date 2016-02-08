import hashlib
answer = False
start = 0
key = "yzbqklnj"
while not answer:
    start += 1
    myString = key + str(start)
    antw = (hashlib.md5(myString.encode('utf-8')).hexdigest())
    antw =  str(antw)
    if antw[:6] == "000000":
        answer = True
        print(start)
    else:
        answer = False

