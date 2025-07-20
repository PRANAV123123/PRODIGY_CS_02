from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    encrypted_array = img_array ^ key
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"🔒 Encrypted image saved to: {output_path}")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    decrypted_array = img_array ^ key
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"🔓 Decrypted image saved to: {output_path}")

def main():
    print("=== 🖼️ Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1/2): ")

    if choice not in ['1', '2']:
        print("❌ Invalid choice.")
        return

    image_path = input("Enter path to the image file: ")
    if not os.path.exists(image_path):
        print("❌ Image file not found.")
        return

    try:
        key = int(input("Enter an integer key (1-255): "))
        if not (0 < key < 256):
            raise ValueError
    except ValueError:
        print("❌ Key must be an integer between 1 and 255.")
        return

    output_path = input("Enter output file path (e.g., encrypted.png): ")

    if choice == '1':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
