import time
import random
import hashlib

class prng:
    def __init__(self, seed):
        self.seed = seed
        self.MT = [0 for i in range(624)]
        self.index = 0
        self.bitmask_1 = (2 ** 32) - 1
        self.bitmask_2 = 2 ** 31
        self.bitmask_3 = (2 ** 31) - 1
        self.MT[0] = self.seed
        for i in range(1,624):
            self.MT[i] = ((1812433253 * self.MT[i-1]) ^ ((self.MT[i-1] >> 30) + i)) & self.bitmask_1
        if self.index == 0:
            for i in range(624):
                y = (self.MT[i] & self.bitmask_2) + (self.MT[(i + 1 ) % 624] & self.bitmask_3)
                self.MT[i] = self.MT[(i + 397) % 624] ^ (y >> 1)
                if y % 2 != 0:
                    self.MT[i] ^= 2567483615

    def rand(self, start = 0, end = 32):
        y = self.MT[self.index]
        y ^= y >> 11
        y ^= (y << 7) & 2636928640
        y ^= (y << 15) & 4022730752
        y ^= y >> 18

        self.index = (self.index + 1) % 624
        return y


def noiseMap(sd, se):
    nm = []
    rand = prng(sd)
    for i in range(se[1]):
        nm.append([])
        for j in range(se[0]):
            nm[i].append(str(rand.rand())[1])
    return nm

def display(map, seed, coords, size, ts):
        loopIndex = 0
        print(f'┏{"━" * (size[0] + 2)}┓')
        for x in map:
            loopIndex += 1
            print("┃ ", end="")
            for i in x:
                print(str(i).replace('0', '-').replace('1', '~').replace('2', '=').replace('3', '#').replace('4', '░').replace('5', '▒').replace('6', '▓').replace(str(i), ' '), end="")
            print(f" ┃")

        print(f'┗{"━" * (size[0] + 2)}┛')

        coords = f'X: {coords[0]}, Y: {coords[1]}'
        time = f'{ts} /ms'
        size = f'{size[0]} x {size[1]}'
        checksum = str(hashlib.sha256(str(map).encode('utf-8')).hexdigest())
        seed = str(seed)

        print(f'''┏{"━" * (len(hashlib.sha256(str(map).encode('utf-8')).hexdigest()) + 13)}┓\n┃ // Settings {" " * (len(checksum))}┃\n┃ Seed     : {seed[:len(checksum) - 2]}{'..' if (len(str(seed)) > len(checksum)) else '' }{" " * ((len(checksum) ) - len(seed))} ┃\n┃ Coords   : {coords} {" " * (len(checksum) - len(coords))}┃\n┃{" " * (len(checksum) + 13)}┃\n┃ // Algorithm Info {" " * (len(checksum) - 6)}┃\n┃ Checksum : {checksum} ┃\n┃ Time     : {time} {" " * (len(checksum) - len(time))}┃\n┃ Size     : {size} {" " * (len(checksum) - len(size))}┃\n┗{"━" * (len(checksum) + 13)}┛''')


if __name__ == "__main__":
    # Initialize the parameters
    seed = 101012 #random.randint(0, 1000000)
    coords = (0, 0)
    size = (60, 30)

    ts = time.time() # Start the timer

    map = noiseMap(seed, size)

    ts = round((time.time() - ts) * 1000, 2) # Stop the timer
    display(map, seed, coords, size, ts)