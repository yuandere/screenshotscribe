import json
import os
import sys

from screenshotscribe.generate_text_gemini import generate_text_gemini
from screenshotscribe.output_document import output_document
from screenshotscribe.output_markdown import output_markdown


def scan_for_images(images_dir=os.path.abspath(os.path.join(os.curdir, 'images_to_process'))):
    supported_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.heic', '.heif',
                            '.PNG', '.JPG', '.JPEG', '.WEBP', '.HEIC', '.HEIF')
    image_paths = []

    for root, dirs, files in os.walk(images_dir):
        for file in files:
            if file.endswith(supported_extensions):
                image_paths.append(os.path.join(root, file))

    return image_paths


def get_output_type():
    valid_commands = {'n', 'm', 'd'}

    while True:
        command = input(
            "Would you like a formatted output file? Enter: 'm' for markdown, or 'd' for docx, or 'n' for no\n").strip().lower()

        if command in valid_commands:
            return command
        else:
            print(
                "Invalid input. Please enter 'm' for markdown, or 'd' for docx, or 'n' for no\n")


def main():
    image_paths = scan_for_images()
    if len(image_paths) == 0:
        print('No images found in the target directory. Exiting...')
        sys.exit()
    print(f'{len(image_paths)} images found. Working...\n')

    generated_data = generate_text_gemini(image_paths)

    filename = 'transcribed.json'
    with open(filename, 'w') as json_file:
        json.dump(generated_data, json_file, indent=4)
        print(f'json file created at {filename}')

    output_type = get_output_type()

    if output_type == 'm':
        output_markdown(generated_data)
    elif output_type == 'd':
        output_document(generated_data)


if __name__ == "__main__":
    main()
