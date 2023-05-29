
# DeepL PDF Translation Script

  

This script allows you to translate PDF files using the DeepL API. It automatically detects the source language and translates the PDF to the specified target language.

  

## Prerequisites

  

- Python 3.x

- [DeepL API Key](https://www.deepl.com/docs-api/translating-text/)

  

## Installation

  

1. Clone or download this repository.

	`git clone https://github.com/CrocSpider/DeepLTranslator.git`

  

2. Install the required packages by running the following command:

	`pip install -r requirements.txt`

  
  

## Usage

  

1. Replace `'API_KEY'` in the script with your actual DeepL API key.

  

2. Open a terminal or command prompt and navigate to the script directory

  

3. Run the script by executing the following command:

	`py translate.py`

  

4. Follow the prompts:

- Enter the path to the PDF file you want to translate.

- Enter the target language code (e.g., 'DE' for German).

  

5. The translated PDF file will be saved in the same directory as the input file with the name appended with the target language code.

  

**Note:** *Make sure the input PDF file exists and the target language code is valid.*

  

## License

  

This script is licensed under the [MIT License](LICENSE).