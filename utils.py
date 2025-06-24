from PIL import Image
import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def hide_data(image, message):
    img = image.convert('RGB')
    data = np.array(img)

    binary_msg = text_to_binary(message) + '1111111111111110'  # 16-bit delimiter
    idx = 0

    for row in data:
        for pixel in row:
            for n in range(3):  # R, G, B
                if idx < len(binary_msg):
                    pixel[n] = (pixel[n] & 0xFE) | int(binary_msg[idx])
                    idx += 1

    return Image.fromarray(data)

def extract_data(image):
    img = image.convert('RGB')
    data = np.array(img)

    binary_msg = ''
    for row in data:
        for pixel in row:
            for n in range(3):
                binary_msg += str(pixel[n] & 1)
                if binary_msg[-16:] == '1111111111111110':
                    return binary_to_text(binary_msg[:-16])
    return "No hidden message found."
