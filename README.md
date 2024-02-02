# Machine Translation - English to Hindi

## Overview
This repository contains a machine translation project focused on converting English text to Hindi. The project is fine-tuned on the MarianMT transformer and leverages a dataset available at [HindiEnglish Corpora](https://www.kaggle.com/datasets/aiswaryaramachandran/hindienglish-corpora).
## Dataset Summary
![Screenshot 2024-02-02 154700](https://github.com/Rashid0125/Machine-Translation/assets/102589680/0fe85eb8-aa69-4739-b1de-9c9bac6ca3ab)

## Requirements
* Python 3.8 and above 
* PyTorch
* Hugging Face Transformers

* Other dependencies as listed in requirements.txt


## Installation
1. Clone this repository:
```bash
git clone https://github.com/Rashid0125/Machine-Translation.git
cd your-machine-translation-project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```


## Usage
Download the fine-tuned model weights from here and place them in the models directory.

Run the translation script:

```bash
python test.py --input_text "Your English text goes here"
```
This will output the translated text in Hindi.

## Model Fine-Tuning
Details about fine-tuning the MarianMT transformer on the specific dataset can be found in the fine-tuning.ipynb notebook.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Acknowledgments
Thanks to the creators of the MarianMT transformer and Hugging Face for providing a powerful and user-friendly interface for transformer models.
Contact
For any questions or inquiries, please contact at [EMAIL](ali996958@gmail.com).

Happy translating!
