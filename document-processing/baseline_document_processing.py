#!/usr/bin/env python3
# Load a patched ir_datasets that loads the injected data inside the TIRA sandbox
from tira.third_party_integrations import ir_datasets, get_output_directory
from pathlib import Path
import pandas as pd
import textstat as ts
from pprint import pprint 
import json

doc_ranking=dict()

def process_document(document):
    # Dummy processing of documents: classify each document as spam
    doc_ranking[document.doc_id]={'flesch_reading_formula': ts.flesch_reading_ease(document.text), 
                                  'flesch_kincaid_grade': ts.flesch_kincaid_grade(document.text), 
                                  'gunning_fog': ts.gunning_fog(document.text),
                                  'automated_readability_index': ts.automated_readability_index(document.text)}
    return {'docno': document.doc_id, 'label': 'spam'}


def process_documents(document_iter):
    return pd.DataFrame([process_document(i) for i in document_iter])

# convert the dictionary to a Dataframe, so we can visualize the result as a bar graph later
def convert_result_dict_to_df():
    df = pd.DataFrame.from_dict(doc_ranking, orient='index')
    print(df)

# Create result.json 
def create_result_json():
    with open("result.json", "w") as write_file:
        json.dump(doc_ranking, write_file, indent=4, separators=(", ", ": "), sort_keys=True)

def pretty_print_result():
    pprint(doc_ranking)

if __name__ == '__main__':
    # In the TIRA sandbox, this is the injected ir_dataset, injected via the environment variable TIRA_INPUT_DIRECTORY
    dataset = ir_datasets.load('workshop-on-open-web-search/document-processing-20231027-training')

    # The expected output directory, injected via the environment variable TIRA_OUTPUT_DIRECTORY
    output_dir = get_output_directory('.')
    
    # Document processors persist their results in a file documents.jsonl.gz in the output directory.
    output_file = Path(output_dir) / 'documents.jsonl.gz'

    # You can pass as many additional arguments to your program, e.g., via argparse, to modify the behaviour
    
    # process the documents, store results at expected location.
    processed_documents = process_documents(dataset.docs_iter())
    processed_documents.to_json(output_file, lines=True, orient='records')
    # pretty_print_result()
    # print(doc_ranking)

    create_result_json()    
