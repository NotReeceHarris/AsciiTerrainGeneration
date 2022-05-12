import time
import random
import hashlib

# create a random noise map between 0 and 1 with size of (x, y) and seed
def noiseMap(seed, size):
    noise_map = []
    random.seed(seed)
    for i in range(size[1]):
        noise_map.append([])
        for j in range(size[0]):
            noise_map[i].append(random.randint(0, 6))
    return noise_map

if __name__ == "__main__":
    # Initialize the parameters
    seed = 26207806070
    coords = (100, 100)
    size = (60, 30)

    ts = time.time() # Start the timer

    map = noiseMap(seed, size)

    ts = round((time.time() - ts) * 1000, 2) # Stop the timer

    loopIndex = 0
    print(f'┏{"━" * (size[0] + 2)}┓')
    for x in map:
        loopIndex += 1
        print("┃ ", end="")
        for i in x:
            print(str(i).replace('0', '-').replace('1', '~').replace('2', '=').replace('3', '#').replace('4', '░').replace('5', '▒').replace('6', '▓'), end="")

        if loopIndex == 1:
            print(f" ┃ // Settings")
        elif loopIndex == 2:
            print(f" ┃ Seed     : {seed}")
        elif loopIndex == 3:
            print(f" ┃ Coords   : {coords}")
        elif loopIndex == 5:
            print(f" ┃ // Algorithm Info")
        elif loopIndex == 6:
            print(f" ┃ Checksum : {hashlib.sha256(str(map).encode('utf-8')).hexdigest()}")
        elif loopIndex == 7:
            print(f" ┃ Time     : {ts} /ms")
        elif loopIndex == 8:
            print(f" ┃ Size     : {size}")
        else:
            print(f" ┃")

    print(f'┗{"━" * (size[0] + 2)}┛')