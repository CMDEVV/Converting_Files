import os
from PIL import Image
import pillow_heif

# Initialize HEIF support for Pillow
pillow_heif.register_heif_opener()

def convert_heic_to_image(input_file, output_file, output_format='png', width=None, height=None):
    """
    Converts a HEIC file to a PNG or JPEG image with optional custom dimensions.
    
    Parameters:
        input_file (str): Path to the input HEIC file.
        output_file (str): Path to save the output image file.
        output_format (str): The format of the output image ('png' or 'jpeg').
        width (int, optional): Desired width of the output image in pixels.
        height (int, optional): Desired height of the output image in pixels.
    """
    if output_format.lower() not in ['png', 'jpeg']:
        raise ValueError("Output format must be either 'png' or 'jpeg'")
    
    try:
        # Open the HEIC file directly with Pillow
        image = Image.open(input_file)

        # Resize the image if width and height are provided
        if width and height:
            image = image.resize((width, height), Image.LANCZOS)
        
        # Save the image in the desired format
        image.save(output_file, format=output_format.upper())
        print(f"Conversion successful! File saved as {output_file}")
    except Exception as e:
        print(f"An error occurred during conversion of {input_file}: {e}")

def batch_convert_heic(input_directory, output_directory, output_format='png', width=None, height=None):
    """
    Converts all HEIC files in a specified directory to PNG or JPEG format with optional custom dimensions.
    
    Parameters:
        input_directory (str): Path to the directory containing HEIC files.
        output_directory (str): Path to the directory to save converted images.
        output_format (str): The format of the output images ('png' or 'jpeg').
        width (int, optional): Desired width of the output images in pixels.
        height (int, optional): Desired height of the output images in pixels.
    """
    if not os.path.exists(input_directory):
        raise ValueError("The specified input directory does not exist.")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create output directory if it doesn't exist
    
    for filename in os.listdir(input_directory):
        if filename.lower().endswith('.heic'):
            input_path = os.path.join(input_directory, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.{output_format}"
            output_path = os.path.join(output_directory, output_filename)
            
            convert_heic_to_image(input_path, output_path, output_format, width, height)

# Example usage
if __name__ == "__main__":
    input_directory = "/Users/carlosmendez/personal/heic_dir"  # Replace with the path to your HEIC files
    output_directory = "/Users/carlosmendez/personal/converted_img"  # Replace with the path to save converted images
    output_format = 'png'  # Choose 'png' or 'jpeg'
    width = 800  # Set desired width in pixels (or None for original width)
    height = 600  # Set desired height in pixels (or None for original height)
    
    batch_convert_heic(input_directory, output_directory, output_format, width, height)

# Need to lower the dimensions (DONE)
# create a new folder for converted images (NO NEED)
# OR give path to folder to were to append images (DONE)
# Gave it a specifc path for converted images 

