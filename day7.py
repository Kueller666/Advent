FILE = "day7.txt"
gegevens = {}


def convert(tekst):
    tekst = tekst[:-1]
    result = tekst.split(" ")
    if result[0].isdigit():
        result[0] = int(result[0])
    return result


def check_num(first, last):
    if first.isdigit() and last.isdigit():
        return 0
    elif not first.isdigit() and not last.isdigit():
        return 3
    elif first.isdigit():
        return 2
    else:
        return 1


def do_and(first, last):
    case = check_num(first, last)
    if case == 0:
        return int(first) & int(last)
    elif case == 1:
        return int(last) & gegevens[first]
    elif case == 2:
        return int(first) & gegevens[last]
    else:
        return gegevens[last] & gegevens[first]


def do_or(first, last):
    case = check_num(first, last)
    if case == 0:
        return int(first) | int(last)
    elif case == 1:
        return int(last) | gegevens[first]
    elif case == 2:
        return int(first) | gegevens[last]
    else:
        return gegevens[last] | gegevens[first]


def do_rshift(first, last):
    case = check_num(first, last)
    if case == 0:
        return int(first) >> int(last)
    elif case == 1:
        return gegevens[first] >> int(last)
    elif case == 2:
        return int(first) >> gegevens[last]
    else:
        return gegevens[first] >> gegevens[last]


def do_lshift(first, last):
    case = check_num(first, last)
    if case == 0:
        return int(first) << int(last)
    elif case == 1:
        return gegevens[first] << int(last)
    elif case == 2:
        return int(first) << gegevens[last]
    else:
        return gegevens[first] << gegevens[last]


def do_not(vari):
    if vari.isdigit():
        return 65535 - int(vari)
    else:
        return 65535 - gegevens[vari]


operators = {"AND": do_and, "OR": do_or,
             "RSHIFT": do_rshift, "LSHIFT": do_lshift,
             "NOT": do_not}

with open(FILE) as f:
    for line in f.readlines():
        instr = convert(line)
        if len(instr) == 4:
            gegevens[instr[-1]] = int(do_not(instr[1]))
        elif len(instr) > 4:
            gegevens[instr[-1]] = int(operators[instr[1]](instr[0],instr[2]))
        else:
            gegevens[instr[-1]] = int(instr[0])
        print(gegevens)




