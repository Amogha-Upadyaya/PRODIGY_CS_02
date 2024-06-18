# Encryption
#### Import Libraries
- *from PIL import Image* ⇒ Imports the *Pillow* library for Image Processing
- *import random* => Imports the *random* module for generating random numbers
- *import os* => Imports the *os* module for potential operating system interactions. Here, it is used to open the encrypted image after processing.

#### Read the Image (with Error Handling)
- The function *encrypt_image* takes *image_path* (string) and *key* (integer) as arguments
- It attempts to open the image using *Image.open(image_path)*
- If the image is not found, it raises a *FileNotFoundError* with a message and returns.
- If successful, it converts the image to RGB mode using *.convert("RGB")*.
- It retrieves the image dimensions (*width* and *height*) and pixel access object (*pixels*) for manipulation.

#### Key Generation (Pseudo-Random Sequence)
- An empty list *swap_sequence* is initialized to store the pseudo-random sequence.
- A loop iterates through 256 values (*i in range(256)*).
- For each value *i*
  - It calculates two offsets based on the key and modulo operations
    - *(i + key) % width*
    - *(i - key) % height*)
  - These offsets are appended to the *swap_sequence* list.

#### Pixel Swapping (Conditional)
- A _swap_chance_ variable is set to 0.2 (probability of swapping a pixel).
- The code iterates through each pixel in the image:
  - For each pixel location (_x, y_):
    - It checks if the _swap_sequence_ has elements and a random number is less than _swap_chance_.
      - If the conditions are met, it performs a pixel swap:
        - It retrieves the first two elements from the _swap_sequence_ as _swap_x_ and _swap_y_ (these represent the offsets for swapping).
        - It removes the used elements from the _swap_sequence_ using slicing (_swap_sequence[2:]_).
        - It stores the current pixel value in a temporary variable _temp_pixel_.
        - It swaps the values of the current pixel (_x, y_) with the pixel at the offset location (_swap_x, swap_y_) using the temporary variable.

#### Mathematical Operations (Color Shifting)
- A _shift_value_ is calculated by taking the key modulo 256.
- The code iterates through each pixel in the image again:
  - For each pixel location (_x, y_):
    - It retrieves the red, green, and blue channel values (_r, g, b_) of the pixel.
    - It performs a color shift on each channel by adding the _shift_value_ and applying the modulo 256 operation to keep the values within the valid range (0-255).
    - The modified color values are assigned back to the pixel

#### Combine Operations
The pixel swapping and color shifting operations are applied sequentially within the same loop, effectively combining them into the encryption process.

#### Write Encrypted Image
- The modified image data is saved using _image.save("encrypted.png")_.
- A success message is printed.
- The program attempts to open the encrypted image using the operating system's default application based on the platform (_os.name_).

# Decryption
#### Import Libraries
- _from PIL import Image_: Imports the Pillow library for image processing.
- _import random_: Imports the _random_ module for generating random numbers.
- _import os_: Imports the _os_ module for interacting with the operating system (used for opening the decrypted image).

#### Key Input
The decryption function doesn't explicitly prompt for user input for the key. It assumes the key used for decryption is provided as an argument (_key_) to the _decrypt_image_ function.

#### Read Encrypted Image
- Opens the encrypted image file specified by the _image_path_ argument using _Image.open()_.
- Converts the image to RGB mode (if necessary) using _convert("RGB")_.
- Stores the image size (width and height) in _width_ and _height_ variables.
- Loads the image pixel access object into _pixels_.

#### Reverse Pixel Swapping
- Generates the same "pseudo-random" swap sequence based on the key using a loop. This sequence is crucial for reversing the pixel swaps performed during encryption.
- Iterates through each pixel:
  - Checks if the swap condition is met (based on _swap_chance_ and remaining elements in the sequence).
  - If the condition is met, retrieves the swap offsets from the last two elements of the _swap_sequence_ (since encryption used the sequence in a forward manner).
  - Removes the used elements from the _swap_sequence_ to maintain order.
  - Performs the pixel swap using a temporary variable (_temp_pixel_).

#### Reverse Mathematical Operations
- Defines the _shift_value_ based on the _key_ modulo 256 (same as encryption).
- Iterates through each pixel:
  - Extracts the red (r), green (g), and blue (b) color channel values.
  - Performs the decryption for each channel by subtracting the _shift_value_ modulo 256 (reversing the encryption step).
  - Ensures the new color values are within the valid range (0-255) using _max(0, new_value)_.

#### Write Decrypted Image
- Saves the modified image data back to the image object using _image.save("decrypted.png")_.
- Prints a success message "Image Decryption Successful!".
- Opens the decrypted image using platform-specific commands (_os.startfile_ for Windows, _subprocess.call_ for others).
