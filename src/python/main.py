from ast import Try
import time
import hashlib

class prng:
    def __init__(self, seed):
        self.s = seed
        self.m = [0 for i in range(624)]
        self.i = 0
        self.bm1 = (2 ** 32) - 1
        self.bm2 = 2 ** 31
        self.bm3 = (2 ** 31) - 1
        self.m[0] = self.s

        for x in range(1,624):
            self.m[x] = ((1812433253 * self.m[x-1]) ^ ((self.m[x-1] >> 30) + x)) & self.bm1
        if self.i == 0:
            for x in range(624):
                y = (self.m[x] & self.bm2) + (self.m[(x + 1 ) % 624] & self.bm3)
                self.m[x] = self.m[(x + 397) % 624] ^ (y >> x)
                if y % 2 != 0:
                    self.m[x] ^= 2567483615
                    
    def rand(self):
        y = self.m[self.i]
        y ^= y >> 11
        y ^= (y << 7) & 2636928640
        y ^= (y << 15) & 4022730752
        y ^= y >> 18

        self.i = (self.i + 1) % 624
        return y

def noiseMap(sd, se):
    nm = []
    rand = prng(sd)
    for i in range(se[1]):
        nm.append([])
        for j in range(se[0]):
            nm[i].append((int(str(rand.rand())[1]) / 9))
    return nm

# using interpolation make a smoother map and make it more readable for the user
def interpolate(map, size):
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

# take a noise map and round all the numbers to 1 decimal place
def roundMap(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            map[x][y] = round(map[x][y], 1)
    return map

def display(map, seed, coords, size, ts):

        dcoords = f'X: {coords[0]}, Y: {coords[1]}'
        dtime = f'{ts} /ms'
        dsize = f'{size[0]} x {size[1]}'
        dchecksum = str(hashlib.sha256(str(map).encode('utf-8')).hexdigest())
        dseed = str(seed)

        print(f'''┏{"━" * (len(hashlib.sha256(str(map).encode('utf-8')).hexdigest()) + 13)}┓\n┃ // Settings {" " * (len(dchecksum))}┃\n┃ Seed     : {dseed[:len(dchecksum) - 2]}{'..' if (len(str(dseed)) > len(dchecksum)) else '' }{" " * ((len(dchecksum) ) - len(dseed))} ┃\n┃ Coords   : {dcoords} {" " * (len(dchecksum) - len(dcoords))}┃\n┃{" " * (len(dchecksum) + 13)}┃\n┃ // Algorithm Info {" " * (len(dchecksum) - 6)}┃\n┃ Checksum : {dchecksum} ┃\n┃ Time     : {dtime} {" " * (len(dchecksum) - len(dtime))}┃\n┃ Size     : {dsize} {" " * (len(dchecksum) - len(dsize))}┃\n┗{"━" * (len(dchecksum) + 13)}┛''')

        loopIndex = 0
        print(f'┏{"━" * (size[0] + 2)}┓')
        for x in map:
            loopIndex += 1
            print("┃ ", end="")
            for i in x:
                print(str(i).replace('0.0', '-').replace('0.1', '~').replace('0.2', '=').replace('0.3', '#').replace('0.4', '░').replace('0.5', '▒').replace('0.6', '▓').replace(str(i), ' ') , end="")
            print(f" ┃")

        print(f'┗{"━" * (size[0] + 2)}┛')

if __name__ == "__main__":
    # Initialize the parameters
    seed = 101012 #random.randint(0, 1000000)
    coords = (0, 0)
    size = (80, 40)

    ts = time.time() # Start the timer

    map = noiseMap(seed, size)
    smooth = interpolate(map, size)
    rounded = roundMap(map)

    ts = round((time.time() - ts) * 1000, 2) # Stop the timer
    display(rounded, seed, coords, size, ts)