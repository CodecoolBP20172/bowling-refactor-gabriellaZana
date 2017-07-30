def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for line in range(len(game)):
        if game[line] == '/':
            result += 10 - last
        else:
            result += get_value(game[line])
        if frame < 10 and get_value(game[line]) == 10:
            if game[line] == '/':
                result += get_value(game[line+1])
            elif game[line] == 'X' or game[line] == 'x':
                result += get_value(game[line+1])
                if game[line+2] == '/':
                    result += 10 - get_value(game[line+1])
                else:
                    result += get_value(game[line+2])
        last = get_value(game[line])
        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if game[line].upper() == 'X':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char.isdigit():
        return int(char)
    elif char.upper() == 'X':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
