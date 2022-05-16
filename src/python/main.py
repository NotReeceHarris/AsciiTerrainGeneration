import time
import random
from display import *

def noiseMap(seed, size):
    nm = []
    random.seed(seed)
    for i in range(size[1]):
        nm.append([])
        for j in range(size[0]):
            nm[i].append(random.uniform(0,1))
    return nm

def interpolate(map, intensity):
    for i in range(intensity):
        for x in range(len(map)):
            for y in range(len(map[x])):
                if x == 0:
                    map[x][y] = map[x][y]
                elif x == len(map) - 1:
                    map[x][y] = map[x][y]
                else:
                    map[x][y] = (map[x - 1][y] + map[x + 1][y]) / 2
        for x in range(len(map)):
            for y in range(len(map[x])):
                if y == 0:
                    map[x][y] = map[x][y]
                elif y == len(map[x]) - 1:
                    map[x][y] = map[x][y]
                else:
                    map[x][y] = (map[x][y - 1] + map[x][y + 1]) / 2
    return map

def roundMap(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            map[x][y] = round(map[x][y], 1)
    return map

if __name__ == "__main__":
    seed = random.randint(-100000000, 100000000)
    size = (100, 50)
    intensity = 2

    runTerrainGeneration(seed, size, intensity)