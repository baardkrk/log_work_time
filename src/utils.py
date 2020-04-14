def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def print_underline(length, character="="):
    li = []
    for _ in range(length):
        li.append(character)
    underline = ''.join(li)
    
    print(underline, '\n')
