<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/yuandere/screenshotscribe">
    <img src="assets/logo.png" alt="Logo" width="128" height="128">
  </a>

  <h2 align="center">Screenshot Scribe</h2>

  <p align="center">
    Perform OCR on your images and screenshots, and gather the text into one convenient file with Gemini 1.5 Flash.
    <br />
    <br />
  </p>
</div>

<!-- ABOUT -->

## About

<div align="center">
  <a href="https://github.com/yuandere/screenshotscribe">
    <img src="assets/demo2.gif" alt="Logo" width="550" height="356">
  </a>
</div>

I take lots of screenshots of things that I want to reference later but almost never actually do. This tool is intended to make accessing that info much easier.

Gemini 1.5 Flash was chosen for the job since it greatly outperforms open-source OCR solutions like Tesseract and EasyOCR, but is [quicker](https://arxiv.org/abs/2403.05530) and [cheaper](https://llmpricecheck.com/) relative to many other multimodal LLMs.

<!-- FEATURES -->

## Features

- Batch OCR processing of images
- Easy to customize system prompt
- `.json` output by default, with optional formatted `.md` and `.docx` file types

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

You will need to have the following installed:

- [Python 3.12 or up](https://www.python.org/)
- [Poetry 1.8 or up](https://python-poetry.org/)


### Installation

1. Get an API Key at [Google AI Studio](https://aistudio.google.com/) \(note free usage limits\)
2. Clone the repo
   ```sh
   git clone https://github.com/yuandere/screenshotscribe
   ```
3. Install Poetry packages and start a virtual environment
   ```sh
   poetry install

   poetry shell
   ```
4. Create a `.env` file in the project directory and add your API key
   ```
   GEMINI_API_KEY = XXXXXX
   ```
5. Move any images you want processed into the folder /images_to_process
6. Run 
   ```
   screenshotscribe
   ```


<!-- CONTRIBUTING -->

## Contributing

Contributions are appreciated! If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->

## Contact

Discord - [@al_doub](https://discord.com/)

X/Twitter - [@yuandere](https://x.com/yuandere)

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments


- [Choose an Open Source License](https://choosealicense.com)
- [markdownguide](https://www.markdownguide.org/cheat-sheet/)
- [flaticon](https://www.flaticon.com/free-icon/generative-image_16649299)
- [README template](https://github.com/othneildrew/Best-README-Template)
