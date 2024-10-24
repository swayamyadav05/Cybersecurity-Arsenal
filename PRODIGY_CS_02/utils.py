def swap_pixels(pixel1, pixel2):
    """
    Swap two pixels.

    Args:
        pixel1: The first pixel (tuple of RGB values).
        pixel2: The second pixel (tuple of RGB values).
    """
    return pixel2, pixel1


def shift_pixel_value(value, key):
    """
    Shift a pixel value by a key (for encryption or decryption).

    Args:
        value: The pixel value (0-255).
        key: The key to shift the value by.
        return: New shifted value.
    """
    return (value + key) % 256
