# Your task is to construct a building which will be a pile of n cubes.
# The cube at the bottom will have a volume of n^3, the cube above will
# have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.


def find_nb(m):
    current_volume = 0
    level = 0
    while current_volume != m:
        current_volume += level ** 3
        level += 1
        if current_volume > m:
            return -1
    return level



