
# TASK: You will be passed a string and you must return that
# string in an array where an uppercase letter is a person standing up.
#


def wave(people):
    waves = []
    for p in range(len(people)):
        if people[p] == ' ':
            continue
        waves.append(people[:p] + people[p].upper() + people[p + 1:])
    return waves
