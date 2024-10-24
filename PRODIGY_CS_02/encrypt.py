from PIL import Image
import utils


def encrypt_image(input_image_path, output_image_path, key):
    """
    Encrypt the image using pixel manipulation by shifting pixel values.

    :param input_image_path: Path to the input image file.
    :param output_image_path: Path to save the encrypted image.
    :param key: Integer key for encryption (used for shifting pixel values).
    """
    try:
        img = Image.open(input_image_path)
        encrypted_img = img.copy()
        pixels = encrypted_img.load()

        # Encrypt the pixels by modifying their values
        for i in range(encrypted_img.size[0]):  # Width
            for j in range(encrypted_img.size[1]):  # Height
                r, g, b = pixels[i, j]

                # Ensure the pixel values remain in the range [0, 255] with modulo
                encrypted_r = (r + key) % 256
                encrypted_g = (g + key) % 256
                encrypted_b = (b + key) % 256

                pixels[i, j] = (encrypted_r, encrypted_g, encrypted_b)

        # Save the encrypted image
        encrypted_img.save(output_image_path)
        print(f"Image encrypted and saved as {output_image_path}")

    except Exception as e:
        print(f"Error encrypting image: {e}")


if __name__ == "__main__":
    input_image_path = "test_image.jpg"
    output_image_path = "encrypted_image.png"
    key = 42  # Use an integer as the encryption key

    encrypt_image(input_image_path, output_image_path, key)
