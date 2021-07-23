flatliste= []
def flatten(l):
    for n in l:
        if type(n) == list:
                flatten(n)
        else:
                flatliste.append(n)
    return flatliste
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
