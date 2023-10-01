from PIL import Image

def convert_gif_to_png(gif_path, output_folder):
    try:
        # Open the GIF image
        gif = Image.open(gif_path)

        # Iterate through each frame in the GIF
        for frame_number in range(gif.n_frames):
            # Select the current frame
            gif.seek(frame_number)

            # Create a PNG image from the current frame
            png_image = gif.copy()
            
            # Generate the output PNG file path
            output_path = f"{output_folder}/frame_{frame_number:03d}.png"

            # Save the PNG image
            png_image.save(output_path, "PNG")

            print(f"Saved frame {frame_number:03d} as {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user for the GIF file path and output folder path
    gif_file_path = input("Enter the path to the GIF file: ")
    output_folder_path = input("Enter the path to the output folder: ")

    # Call the function to convert the GIF to PNG images
    convert_gif_to_png(gif_file_path, output_folder_path)
