import os
import requests
import deepl

# DeepL API credentials
API_KEY = 'API_KEY'

# Function to detect the source language of a text
def detect_language(text):
    translator = deepl.Translator(API_KEY)
    result = translator.translate(text, target_lang='EN')
    return result.detected_source_language

# Function to translate text using DeepL API
def translate_text(text, target_lang):
    translator = deepl.Translator(API_KEY)
    result = translator.translate(text, target_lang=target_lang)
    return result.text

# Function to translate a PDF file
def translate_pdf(file_path, target_lang):
    translator = deepl.Translator(API_KEY)

    # Determine the output file path
    directory = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(file_name)[0]
    output_file_path = os.path.join(directory, f"{file_name_without_ext}_{target_lang}.pdf")
    
    with open(file_path, 'rb') as in_file, open(output_file_path, "wb") as out_file:
        result = translator.translate_document(in_file, out_file, target_lang=target_lang)
    

    print(f"Translation saved to: {output_file_path}")


# Main function
def main():
    # Path to the PDF file you want to translate
    pdf_file_path = input("Enter the path to the PDF file: ")

    # Target language for translation
    target_language = input("Enter the target language code: ")

    # Output file path for translated text
    #output_file_path = r'C:\Users\iau3278\Downloads\test-en.pdf'

    # Translate the PDF file
    translate_pdf(pdf_file_path, target_language)

if __name__ == '__main__':
    main()