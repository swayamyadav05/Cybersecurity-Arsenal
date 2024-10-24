from PIL import Image
import utils


def decrypt_image(input_image_path, output_image_path, key):
    """
    Decrypt the image by reversing the pixel value shifts.

    :param input_image_path: Path to the encrypted image file.
    :param output_image_path: Path to save the decrypted image.
    :param key: Integer key used for decryption (must be the same as the encryption key).
    """
    try:
        img = Image.open(input_image_path)
        decrypted_img = img.copy()
        pixels = decrypted_img.load()

        # Decrypt the pixels by reversing the encryption process
        for i in range(decrypted_img.size[0]):  # Width
            for j in range(decrypted_img.size[1]):  # Height
                r, g, b = pixels[i, j]

                # Reverse the encryption, ensure pixel values stay within [0, 255] using modulo
                decrypted_r = (r - key) % 256
                decrypted_g = (g - key) % 256
                decrypted_b = (b - key) % 256

                pixels[i, j] = (decrypted_r, decrypted_g, decrypted_b)

        # Save the decrypted image
        decrypted_img.save(output_image_path)
        print(f"Image decrypted and saved as {output_image_path}")

    except Exception as e:
        print(f"Error decrypting image: {e}")


if __name__ == "__main__":
    input_image_path = "encrypted_image.png"
    output_image_path = "decrypted_image.png"
    key = 42  # Same key used for encryption and decryption

    decrypt_image(input_image_path, output_image_path, key)
