from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog


def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = np.array(img)

    np.random.seed(sum(ord(char) for char in str(key)))

    rand_sequence = np.random.permutation(pixels.size)
    flat_pixels = pixels.flatten()

    encrypted_pixels = flat_pixels[rand_sequence]

    encrypted_image = Image.fromarray(encrypted_pixels.reshape(pixels.shape), img.mode)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = np.array(img)

    np.random.seed(sum(ord(char) for char in str(key)))

    rand_sequence = np.random.permutation(pixels.size)
    inverse_sequence = np.argsort(rand_sequence)

    flat_pixels = pixels.flatten()
    decrypted_pixels = flat_pixels[inverse_sequence]

    decrypted_image = Image.fromarray(decrypted_pixels.reshape(pixels.shape), img.mode)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")


def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("All Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff"),  # Allow multiple formats
        ("PNG Images", "*.png"),
        ("JPEG Images", "*.jpg;*.jpeg"),
        ("Bitmap Images", "*.bmp"),
        ("TIFF Images", "*.tiff")],
    )
    return file_path


def save_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        title="Save File As",
        defaultextension=".png",
        filetypes=[("All Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff"),  # Allow multiple formats
        ("PNG Images", "*.png"),
        ("JPEG Images", "*.jpg;*.jpeg"),
        ("Bitmap Images", "*.bmp"),
        ("TIFF Images", "*.tiff")],
    )
    return file_path


if __name__ == "__main__":
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        input_image = select_file()
        if not input_image:
            print("No file selected.")
            exit()

        output_image = save_file()
        if not output_image:
            print("No output path specified.")
            exit()

        key = input("Enter a secret key for encryption: ").strip()
        encrypt_image(input_image, output_image, key)

    elif choice == "2":
        input_image = select_file()
        if not input_image:
            print("No file selected.")
            exit()

        output_image = save_file()
        if not output_image:
            print("No output path specified.")
            exit()

        key = input("Enter the secret key for decryption: ").strip()
        decrypt_image(input_image, output_image, key)

    else:
        print("Invalid choice. Exiting.")
