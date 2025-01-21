import numpy as np
from PIL import Image


def image_to_pixel_values(image_path):

    try:
        # Open the image
        img = Image.open(image_path)
        # Convert the image to RGB format if not already in it
        img = img.convert("RGB")
        # Convert the image to a NumPy array
        img_array = np.array(img)

        # Get the height and width of the image
        height, width, _ = img_array.shape

        # Create a list to store pixel positions and color values
        pixel_values = []

        for y in range(height):
            for x in range(width):
                # Get the RGB color value at each pixel
                color = tuple(img_array[y, x])
                # Append the pixel position and color value
                pixel_values.append(((x, y), color))

        # Convert the NumPy array to bytes
        byte_data = img.tobytes()

        return pixel_values, byte_data
    except Exception as e:
        print(f"Error: {e}")
        return None, None


# Example usage
if __name__ == "__main__":
    image_path = r"D:\Deep Learning\img\ex1.png"  # Replace with your image path
    pixel_values, byte_data = image_to_pixel_values(image_path)

    if pixel_values and byte_data:
        print(f"Image has {len(pixel_values)} pixels.")
        for position, color in pixel_values[:10]:  # Display first 10 pixels for brevity
            print(f"Pixel at {position} has color {color}")

        # Display the first 100 bytes for brevity
        print("\nSample Byte Representation (first 100 bytes):")
        print(byte_data[:100])
