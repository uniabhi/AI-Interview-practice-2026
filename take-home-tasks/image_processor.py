from pathlib import Path
import argparse
from PIL import image, UnidentifiedImageError

def process_images(input_folder, output_folder, width, height):
    if not input_folder.exists() or not input_folder.is_dir():
        print(f"Error: Input folder not found: {input_folder}")
        return

    output_folder.mkdir(parents=True, exist_ok=True)

    valid_extensions = {".jpg", ".jpeg", ".png", ".webp"}
    image_files = [
        file for file in input_folder.iterdir()
        if file.is_file() and file.suffix.lower() in valid_extensions
    ]

    if not image_files:
        print("No supported image files found.")
        return

    total_images = len(image_files)
    success_count = 0
    failed_count = 0

    for number, image_path in enumerate(image_files, start = 1):
        try:
            with Image.open(image_path) as image:
                resized_image = image.resize((width, height))

                output_path = output_folder/ image_path.name
                resized_image.save(output_path)

                