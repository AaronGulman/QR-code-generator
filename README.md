# QR Code Generator

A simple Python script to generate QR codes from URLs and save them as image files.

## Technologies

- **Python**: Programming language used for the script.
- **qrcode**: Library for generating QR codes.
- **Pillow (PIL)**: Python Imaging Library used to handle image operations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

This project provides a straightforward way to generate QR codes from URLs using Python. The generated QR code is saved as an image file (`new_qr_code.png`).

## Features

- Generates QR codes from any URL.
- Saves the generated QR code as an image file.
- Customizable QR code settings such as version, error correction, box size, and border size.

## Installation

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/yourusername/qrcode-generator.git
    cd qrcode-generator
    ```

2. Install the required Python libraries using pip:
    ```sh
    pip install qrcode[pil]
    ```

## Usage

1. Run the `app.py` script:
    ```sh
    python app.py
    ```

2. When prompted, enter the URL you want to generate a QR code for.

3. The script will generate a QR code and save it as `new_qr_code.png` in the current directory.

## Example

```sh
$ python app.py
Enter your url: https://www.example.com
```

This will generate a QR code for https://www.example.com and save it as new_qr_code.png.


License This project is licensed under the MIT License. See the LICENSE file for more details.
