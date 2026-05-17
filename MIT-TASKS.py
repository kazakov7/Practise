# MIT TASK-J
def getMax(str):
    str = str.split()
    max = str[0]
    for x in str:
        if len(x) > len(max):
            max = x
    return max


print(getMax("I come from uzbekistan"))
