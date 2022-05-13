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