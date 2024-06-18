from Encrypt import encrypt_image
from Decrypt import decrypt_image

def main():
    while True:
        print("\nIMAGE ENCRYPTION TOOL")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        opt = int(input("Enter your choice (1-3): "))
        
        if opt == 1:
            image_path = input("Enter image path: ")
            key = int(input("Enter encryption key (integer): "))
            encrypt_image(image_path, key)
        
        elif opt == 2:
            image_path = input("Enter image path: ")
            key = int(input("Enter decryption key (integer): "))
            decrypt_image(image_path, key)
        
        elif opt == 3:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()