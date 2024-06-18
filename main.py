from Encrypt import encrypt_image  # Import encryption function
from Decrypt import decrypt_image  # Import decryption function

def main():
  """
  This function serves as the main entry point for the program,
  providing a user interface for image encryption and decryption.
  """
  while True:
    print("\nIMAGE ENCRYPTION TOOL")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")

    try:
      # Get user input with error handling
      opt = int(input("Enter your choice (1-3): "))
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 3.")
      continue  # Skip to the next iteration of the loop

    if opt == 1:
      # Encryption option
      image_path = input("Enter image path: ")
      key = int(input("Enter encryption key (integer): "))
      encrypt_image(image_path, key)

    elif opt == 2:
      # Decryption option
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