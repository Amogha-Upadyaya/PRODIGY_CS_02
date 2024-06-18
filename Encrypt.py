from PIL import Image
import random
import os

def encrypt_image(image_path: str, key: int) -> None:
    """
    Encrypts an image using a custom pseudo-random pixel swapping and color shifting approach.

    Args:
        image_path (str): Path to the image file to encrypt.
        key (int): Encryption key used for generating the pseudo-random sequence.

    Raises:
        ValueError: If the provided key is not an integer.
        FileNotFoundError: If the image file cannot be found at the specified path.
    """

    if not isinstance(key, int):
        raise ValueError("Key must be an integer.")

    try:
        image = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return

    width, height = image.size
    pixels = image.load()

    # Generate a custom pseudo-random sequence based on the key
    swap_sequence = []
    for i in range(256):
        swap_sequence.append((i + key) % width)
        swap_sequence.append((i - key) % height)

    swap_chance = 0.2
    for x in range(width):
        for y in range(height):
            # Perform pixel swap with a chance based on swap_chance
            if len(swap_sequence) > 0 and random.random() < swap_chance:
                swap_index = 0
                swap_x = swap_sequence[swap_index]  # Use element from sequence
                swap_y = swap_sequence[swap_index + 1]  # Use next element from sequence
                swap_sequence = swap_sequence[2:]  # Remove used elements

                temp_pixel = pixels[x, y]
                pixels[x, y] = pixels[swap_x, swap_y]
                pixels[swap_x, swap_y] = temp_pixel

    shift_value = key % 256
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Shift each color channel value by the key
            pixels[x, y] = (r + shift_value) % 256, (g + shift_value) % 256, (b + shift_value) % 256

    image.save("encrypted.png")
    print("Image Encryption Successful!")

    if os.name == 'nt':
        os.startfile("encrypted.png")
    else:
        subprocess.call(["open", "encrypted.png"])