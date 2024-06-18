from PIL import Image
import random
import os

def decrypt_image(image_path: str, key: int) -> None:
    """
    Decrypts an image file that was previously encrypted using the same key.

    Args:
        image_path (str): The path to the encrypted image file.
        key (int): The integer key used for encryption (must be the same key used for encryption).

    Raises:
        ValueError: If the provided key is not an integer.
        FileNotFoundError: If the image file cannot be found at the specified path.
    """

    if not isinstance(key, int):
        raise ValueError("Key must be an integer")

    try:
        # Open the image and convert it to RGB mode (if necessary)
        image = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return

    width, height = image.size
    pixels = image.load()

    # Generate the same "pseudo-random" swap sequence based on the key
    swap_sequence = []
    for i in range(256):
        swap_sequence.append((i + key) % width)
        swap_sequence.append((i - key) % height)

    swap_chance = 0.2
    for x in range(width):
        for y in range(height):
            # Check if swap condition is met and sequence has elements remaining
            if len(swap_sequence) > 0 and random.random() < swap_chance:
                # Use the last two elements of the sequence for swap offsets
                swap_index = len(swap_sequence) - 2
                swap_x = swap_sequence[swap_index]
                swap_y = swap_sequence[swap_index - 1]
                swap_sequence = swap_sequence[:-2]  # Remove used elements

                # Perform pixel swap
                temp_pixel = pixels[x, y]
                pixels[x, y] = pixels[swap_x, swap_y]
                pixels[swap_x, swap_y] = temp_pixel

    shift_value = key % 256
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Decrypt the color channels by subtracting the shift value
            new_r = (r - shift_value) % 256
            new_g = (g - shift_value) % 256
            new_b = (b - shift_value) % 256
            # Ensure color values stay within valid range (0-255)
            pixels[x, y] = max(0, new_r), max(0, new_g), max(0, new_b)

    # Save the decrypted image and display success message
    image.save("decrypted.png")
    print("Image Decryption Successful!")

    if os.name == 'nt':
        os.startfile("decrypted.png")
    else:
        subprocess.call(["open", "decrypted.png"])