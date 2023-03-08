from steganography import Steganography
import cv2

if __name__ == '__main__':
    algo = Steganography(seed=2023)

    color = cv2.imread('img_1.png')
    grayscale = cv2.imread('img_2.png', flags=0)

    encrypted = algo.encrypt(grayscale, color)
    cv2.imwrite('encrypted.png', encrypted)

    decrypted = algo.decrypt(grayscale.shape, encrypted)
    cv2.imwrite('decrypted.png', decrypted)
