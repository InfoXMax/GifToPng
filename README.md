# GIF to PNG Converter

This Python script allows you to convert a GIF file into a series of PNG images, effectively splitting the GIF into its individual frames.

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- The Pillow (PIL) library installed. You can install it using `pip`:
        ```bash
        pip install pillow
        ```


## Usage

1. Clone this repository to your local machine or download the `gif_to_png_converter.py` script.

2. Open your terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the script by entering the following command:


python gif_to_png_converter.py


5. Follow the prompts to provide the path to the GIF file you want to convert and the output folder where the PNG images will be saved.

6. The script will process the GIF file and generate individual PNG images for each frame. The PNG images will be saved in the specified output folder.

7. You can find the converted PNG images in the output folder, named as "frame_000.png," "frame_001.png," and so on.

## Example

Suppose you have a GIF file named `example.gif` and you want to convert it into PNG images. Here's how you would use the script:

Enter the path to the GIF file: path/to/example.gif
Enter the path to the output folder: path/to/output


The script will convert `example.gif` into a sequence of PNG images in the `output` folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/): The Python Imaging Library used for image processing.

Feel free to use and modify this script according to your needs. If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/yourusername/gif-to-png-converter/issues) on GitHub.
