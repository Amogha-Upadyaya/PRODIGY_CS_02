# Encryption
1. Import Libraries
    - *from PIL import Image* ⇒ Imports the *Pillow* library for Image Processing
    - *import random* => Imports the *random* module for generating random numbers
    - *import os* => Imports the *os* module for potential operating system interactions. Here, it is used to open the encrypted image after processing.

2. Read the Image (with Error Handling)
    - The function *encrypt_image* takes *image_path* (string) and *key* (integer) as arguments
    - It attempts to open the image using *Image.open(image_path)*
    - If the image is not found, it raises a *FileNotFoundError* with a message and returns.
    - If successful, it converts the image to RGB mode using *.convert("RGB")*.
    - It retrieves the image dimensions (*width* and *height*) and pixel access object (pixels) for manipulation.

# Decryption