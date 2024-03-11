# Submissions of tu-dresden-04

Welcome to the repository for the OWS Project at TU Dresden. This repository serves as the foundation for parsing and evaluating documents within the ir_datasets library, producing dictionaries containing pertinent data.

For further evaluation and exploration, utilize the Google Colab Notebook accessible through this [link](https://colab.research.google.com/drive/1anID6ZSFRkIlrz0bWfZpJt4DUGKx0Dn6?usp=sharing).

## textstat-document-processing

Contained within this subfolder is the code for evaluation using the textstat library. This library primarily focuses on readability measures, including but not limited to Flesch Reading Ease, Automated Readability Index, etc. For more detailed information on textstat, please refer to the library's documentation.

## spacy-document-processing

This subfolder contains the code for evaluation using spaCy and textdescriptives. Here, you can evaluate both readability and quality measures. Please note that installing a spaCy pipeline is necessary to execute this code locally. Use the following command to install the required pipeline:
``` bash
python3 -m spacy download en_core_web_lg
```

## Submitting Your Software

Run the github action to submit your software.

