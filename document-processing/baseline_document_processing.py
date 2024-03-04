#!/usr/bin/env python3
# Load a patched ir_datasets that loads the injected data inside the TIRA sandbox
from tira.third_party_integrations import ir_datasets, get_output_directory
from pathlib import Path
import pandas as pd
import textstat as ts
from pprint import pprint 
import matplotlib.pyplot as plt
import json
from datetime import datetime

fake_now=datetime.now()
now=fake_now.isoformat()

doc_ranking=dict()

def process_document(document):
    # Dummy processing of documents: classify each document as spam
    doc_ranking[document.doc_id]={'flesch_reading_formula': ts.flesch_reading_ease(document.text), 
                                  'flesch_kincaid_grade': ts.flesch_kincaid_grade(document.text), 
                                  'gunning_fog': ts.gunning_fog(document.text),
                                  'automated_readability_index': ts.automated_readability_index(document.text),
                                  'coleman_liau_index': ts.coleman_liau_index(document.text),
                                  'linsear_write_formula': ts.linsear_write_formula(document.text),
                                  'dale_chall_readability_score': ts.dale_chall_readability_score(document.text),
                                  'text_standard': ts.text_standard(document.text, float_output=True),
                                  'spache_readability': ts.spache_readability(document.text),
                                  'mcalpine_eflaw': ts.mcalpine_eflaw(document.text)}
    return {'docno': document.doc_id, 'label': 'spam'}


def process_documents(document_iter):
    return pd.DataFrame([process_document(i) for i in document_iter])

# convert the dictionary to a Dataframe, so we can visualize the result as a bar graph later
def convert_result_dict_to_df():
    df = pd.DataFrame.from_dict(doc_ranking, orient='index')
    print(df)
    return df

# plot the data in an easy bar plot
def plot_data_easy(df):
    fig = df.plot(kind='bar',  
        figsize=(20, 16), fontsize=26).get_figure()
    fig.savefig(now+'__test.pdf')
    
# Create result.json 
def create_result_json():
    with open(now+"__result.json", "w") as write_file:
        json.dump(doc_ranking, write_file, indent=4, separators=(", ", ": "), sort_keys=True)


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
    pprint(doc_ranking)
    df = convert_result_dict_to_df() 
    plot_data_easy(df)  
    create_result_json()    
