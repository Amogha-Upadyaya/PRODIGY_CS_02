# PRODIGY_CS_02
The following repository documents the Task-02 of assigned during my Cybersecurity Internship at Prodigy InfoTech

## Description
**Aim**
- Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

**Features**
- Encrypts images using a custom key and a combination of pixel swapping and color shifting techniques
- Decrypts previously encrypted images using the same key
- User-friendly interface for selecting encryption/decryption and providing image paths and keys
- Supports various image formats handled by Pillow Library of Python.

## Installation
**Dependencies**
- Pillow (PIL) - Used for image manipulation tasks

**Installation Commands**
- Open your terminal or command prompt and navigate to your project directory.
- Run the following bash command to install the Pillow Library
``` bash
pip install Pillow
```

**Environment Setup**
- The program is designed to run on various operating systems with Python 3 installed.
- No additional environment setup is required beyond installing the dependencies

## Usage
**How to Run the Program**
1. Download the project from GitHub
2. Open your terminal or command promppt and use the *cd* command to navigate to the directory containing the project files
3. Execute the following bash command to start the program:
``` bash
python main.py
```

**What to expect?**
- The program will launch a user interface where you can choose between encrypting or decrypting an image.
- You will be prompted to provide the image path and an encryption/decryption key (integer value)
- *Encryption*
  - Program will encrypt the specified image using the provided key and save the encrypted version as "encrypted.png"
- *Decryption*
  - Program will decrypt the specified encrypted image using the provided key and save the decrypted version as "decrypted.org"

## Sample Use

![image](https://github.com/Amogha-Upadyaya/PRODIGY_CS_02/assets/120311753/302b7db9-1d4e-4c3a-a8d5-cd713accf734)

**Original Image**

![Sample_Original_Image](https://github.com/Amogha-Upadyaya/PRODIGY_CS_02/assets/120311753/a49fb5d5-5ed6-4f3d-a1dc-7a0e9ed90d36)

**Encrypted Image**

![encrypted](https://github.com/Amogha-Upadyaya/PRODIGY_CS_02/assets/120311753/c58591c1-b11f-4e81-9baa-a90a7a50ab1f)


**Decrypted Image**

![decrypted](https://github.com/Amogha-Upadyaya/PRODIGY_CS_02/assets/120311753/49e4fe0d-a07c-47de-ad44-bef288e93402)

