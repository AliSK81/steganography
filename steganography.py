import numpy as np


class Steganography:
    def __init__(self, seed):
        self.seed = seed

    def __generate_coords(self, oh, ow, th, tw, td) -> list:
        np.random.seed(self.seed)

        points = [(i, j, k) for i in range(th) for j in range(tw) for k in range(td)]

        np.random.shuffle(points)

        return points[:oh * ow * 8]

    def encrypt(self, one: np.ndarray, two: np.ndarray) -> np.ndarray:
        oh, ow = one.shape
        th, tw, td = two.shape

        if oh * ow * 8 > th * tw * td:
            print('try smaller size for pic one.')
            exit(1)

        pts = self.__generate_coords(oh, ow, th, tw, td)

        binary = ''.join(format(one[i, j], '08b') for i in range(oh) for j in range(ow))

        three = np.copy(two)

        for i, bit in enumerate(binary):
            x, y, z = pts[i]

            if bit == '0' and three[x][y][z] % 2 == 1 or bit == '1' and three[x][y][z] % 2 == 0:
                three[x][y][z] += -1 if three[x][y][z] > 0 else 1

        return three

    def decrypt(self, one_shape: tuple, two: np.ndarray) -> np.ndarray:
        oh, ow = one_shape
        th, tw, td = two.shape

        pts = self.__generate_coords(oh, ow, th, tw, td)

        binary = ''
        for i in range(oh * ow * 8):
            x, y, z = pts[i]

            binary += '0' if two[x][y][z] % 2 == 0 else '1'

        bytes = [int(binary[i - 8:i], 2) for i in range(8, len(binary) + 8, 8)]

        one = np.reshape(bytes, (oh, ow))
        return one.astype(np.uint8)
