import argparse
from transformers import pipeline

def parse_arguments():
    parser = argparse.ArgumentParser(description="Translate English text to Hindi using a fine-tuned transformer model.")
    parser.add_argument("--text", required=True, type=str, help="Input text in English to be translated.")
    return parser.parse_args()

def translate_text(text):
    model_checkpoint = "rashid996958/Machine_translation_5-10_epochs"
    translator = pipeline("translation", model=model_checkpoint)
    return translator(text)

def main():
    args = parse_arguments()
    input_text = args.text
    translated_text = translate_text(input_text)
    print(f"Input Text: {input_text}")
    print(f"Translated Text: {translated_text[0]['translation_text']}")

if __name__ == "__main__":
    main()
