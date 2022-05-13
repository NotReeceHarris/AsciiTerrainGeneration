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

if __name__ == '__main__':
    rd = prng(123457)
    for x in range(10):
        print(rd.rand())