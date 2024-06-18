# Image Encryption
- Processing of transforming an original image into an unintelligible format using cryptographic techniques.
- The encrypted image appears scrambled and meaningless to anyone with the necessary key.

**Benefits of Image Encryption**
- *Confidentiality* ⇒ Ensures only authorized individuals can view sensitive visual data
- *Data Integrity* ⇒ Protects images from unauthorised modification during transmission or storage
- *Non-Repudiation* ⇒ Provides a layer of proof that the image originated from a trusted source

**Applications of Image Encryption**
- Securing sensitive medical images
- Protecting financial documents
- Safeguarding confidential military data
- Enhnancing the security of digital rights management

# Pixel Manipulation
- Involves modifying the properties of individual pixels within a digital image to scramble the original information and achieve confidentiality.

**Pixels & Big Picture**
- An image is composed of tiny squares called pixels. Each pixel holds information about its color and position.
- By manipulating these pixel values, we can alter the overall appearance of the image.

**Encryption Techniques Using Pixel Manipulation**
1. **_Swapping Pixel Values_** ⇒ It rearranges the positions of pixels within the image. Simple implementations might involve swapping adjacent pixels, rows or columns based on a secret key. The key dictates the specific swapping pattern, making the original image unrecognizable

2. **_Modifying Pixel Values_** ⇒ Directly altering the color information stored within each pixel
    1. *Bit-Shift Operations* ⇒ Shifting the individual bits within a pixel's value by a specific amount determined by the key. This scrambles the original data without drastically changing the overall image brightness
    2. *Simple XOR Operation* ⇒ Performing a bitwise XOR operation on each pixel value with a key. It flips corresponding bits, resulting in a scrambled image. Decryption involves another XOR with the same key
    3. *Additive Cipher* ⇒ Adding a constant value to each pixel value. This mathematically alters the image data, requiring subtraction of the same value for decryption.

3. **_Advanced Manipulation_**
    1. *Permutation Techniques* ⇒ Rearranging pixels based on complex mathematical functions derived from the secret key
    2. *Substitution Techniques* ⇒ Replacing pixel values with new values based on a key-driven lookup table.

# ALgorithm
## Encryption
1. Import Libraries
2. Read Image
3. Key Generation
4. Pixel Swapping
5. Mathematical Operations
6. Combine Operations
7. Write Encrypted Image

## Decryption
1. Import Libraries
2. Read Encrypted Image
3. Key Input
4. Reverse Pixel Swapping
5. Reverse Mathematical Operations
6. Write Decrypted Image