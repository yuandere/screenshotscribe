import os
import platform
import subprocess
import sys

from screenshotscribe.generate_text_gemini import generate_text_gemini
from screenshotscribe.generate_document import generate_document


# TODO: change test_data to actual folder
def scan_for_images(images_dir=os.path.abspath(os.path.join(os.curdir, 'TEST_DATA'))):
    supported_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.heic', '.heif',
                            '.PNG', '.JPG', '.JPEG', '.WEBP', '.HEIC', '.HEIF')
    image_paths = []

    for filename in os.listdir(images_dir):
        if filename.endswith(supported_extensions):
            image_paths.append(os.path.join(images_dir, filename))

    return image_paths


def main():
    image_paths = scan_for_images()
    if len(image_paths) == 0:
        print('No images found in the target directory. Exiting...')
        sys.exit()
    print(f'{len(image_paths)} images found. Working...')

    generated_data = generate_text_gemini(image_paths)
    print('RESULT:', generated_data)

    generate_document(generated_data)

    doc_path = os.path.join(os.path.curdir, 'transcribed.docx')
    if platform.system() == 'Darwin':
        subprocess.call(('open', doc_path))
    elif platform.system() == 'Windows':
        os.startfile(doc_path)
    else:
        subprocess.call(('xdg-open', doc_path))


if __name__ == "__main__":
    main()
