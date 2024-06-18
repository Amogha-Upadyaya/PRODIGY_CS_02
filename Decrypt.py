from PIL import Image
import random
import os

def decrypt_image(image_path: str, key: int) -> None:
    if not isinstance(key, int):
        raise ValueError("Key must be an integer")
    
    try:
        image = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return
    
    width, height = image.size
    pixels = image.load()

    swap_sequence = []
    for i in range(256):
        swap_sequence.append((i + key) % width)
        swap_sequence.append((i - key) % height)

    swap_chance = 0.2
    for x in range(width):
        for y in range(height):
            #if random.random() < swap_chance:
            if len(swap_sequence) > 0 and random.random() < swap_chance:
                swap_index = len(swap_sequence) - 2
                #swap_x = (x - random.randint(-5, 5)) % width
                swap_x = swap_sequence[swap_index]
                #swap_y = (y - random.randint(-5, 5)) % height
                swap_y = swap_sequence[swap_index - 1]
                swap_sequence = swap_sequence[:-2]

                temp_pixel = pixels[swap_x, swap_y]
                pixels[x, y] = pixels[swap_x, swap_y]
                pixels[swap_x, swap_y] = temp_pixel
    
    shift_value = key % 256
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            new_r = (r - shift_value) % 256
            new_g = (g - shift_value) % 256
            new_b = (b - shift_value) % 256
            pixels[x, y] = max(0, new_r), max(0, new_g), max(0, new_b)
    
    image.save("decrypted.png")
    print("Image Decryption Successful!")

    if os.name == 'nt':
        os.startfile("decrypted.png")
    else:
        subprocess.call(["open", "decrypted.png"])