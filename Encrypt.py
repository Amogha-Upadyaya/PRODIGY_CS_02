from PIL import Image
import random
import os

def encrypt_image(image_path: str, key: int) -> None:
    if not isinstance(key, int):
        raise ValueError("Key must be an integer.")
    
    try:
        image = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return
    
    width, height = image.size
    pixels = image.load()

    random.seed(key)

    swap_chance = 0.2
    for x in range(width):
        for y in range(height):
            if random.random() < swap_chance:
                swap_x = (x + random.randint(-5, 5)) % width
                swap_y = (y + random.randint(-5, 5)) % height

                temp_pixel = pixels[x, y]
                pixels[x, y] = pixels[swap_x, swap_y]
                pixels[swap_x, swap_y] = temp_pixel
    
    shift_value = key % 256
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r + shift_value) % 256, (g + shift_value) % 256, (b + shift_value) % 256
    
    image.save("encrypted.png")
    print("Image Encryption Successful!")

    if os.name == 'nt':
        os.startfile("encrypted.png")
    else:
        subprocess.call(["open", "encrypted.png"])