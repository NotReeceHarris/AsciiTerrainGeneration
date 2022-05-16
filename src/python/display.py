import hashlib
import time
from main import *

class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    LIGHT_BLUE = "\033[1;34m"
    END = "\033[0m"
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32

def asciiMap(map):
    switcher = {
        '0.0': f'{Colors.BLUE}▓{Colors.END}',
        '0.1': f'{Colors.BLUE}▓{Colors.END}',
        '0.2': f'{Colors.LIGHT_BLUE}▓{Colors.END}',
        '0.3': f'{Colors.LIGHT_GREEN}▓{Colors.END}',
        '0.4': f'{Colors.LIGHT_GREEN}▓{Colors.END}',
        '0.5': f'{Colors.GREEN}▓{Colors.END}',
        '0.6': f'{Colors.LIGHT_RED}▓{Colors.END}',
        '0.7': f'{Colors.RED}▓{Colors.END}',
        '0.8': f'{Colors.RED}▓{Colors.END}',
        '0.9': f'{Colors.RED}▓{Colors.END}',
        '1.0': f'{Colors.RED}▓{Colors.END}',
    }
    for x in range(len(map)):
        for y in range(len(map[x])):
            map[x][y] = switcher.get(str(map[x][y]), ' ')
    return map

def display(map, seed, size, ts, intensity):
        loopIndex = 0
        print(f'┏{"━" * (size[0] + 2)}┓')
        for x in map:
            loopIndex += 1
            print("┃ ", end="")
            for i in x:
                print(str(i), end="")
            print(f" ┃")
        print(f'┗{"━" * (size[0] + 2)}┛')

        dtime = f'{ts} /ms'
        dsize = f'{size[0]} x {size[1]}'
        dchecksum = str(hashlib.sha256(str(map).encode('utf-8')).hexdigest())
        dseed = str(seed)
        
        print(f'''
┏{"━" * (len(hashlib.sha256(str(map).encode('utf-8')).hexdigest()) + 14)}┓
┃ // Settings  {" " * (len(dchecksum))}┃
┃ Seed      : {dseed[:len(dchecksum) - 2]}{'..' if (len(str(dseed)) > len(dchecksum)) else '' }{" " * ((len(dchecksum) ) - len(dseed))} ┃
┃ Size      : {dsize} {" " * (len(dchecksum) - len(dsize))}┃
┃ Intensity : {intensity} {" " * (len(dchecksum) - len(str(intensity)))}┃
┃{" " * (len(dchecksum) + 14)}┃
┃ // Algorithm Info {" " * (len(dchecksum) - 5)}┃
┃ Checksum  : {dchecksum} ┃
┃ Time      : {dtime} {" " * (len(dchecksum) - len(dtime))}┃
┗{"━" * (len(dchecksum) + 14)}┛
''')


def runTerrainGeneration(seed, size, intensity):
    ts = time.time()

    map = noiseMap(seed, size)
    smooth = interpolate(map, intensity)
    rounded = roundMap(map)
    ascii = asciiMap(rounded)

    ts = round((time.time() - ts) * 1000, 2) # Stop the timer
    display(ascii, seed, size, ts, intensity)