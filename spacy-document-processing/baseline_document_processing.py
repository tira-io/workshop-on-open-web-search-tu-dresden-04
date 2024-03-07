#!/usr/bin/env python3
# Load a patched ir_datasets that loads the injected data inside the TIRA sandbox
from tira.third_party_integrations import ir_datasets, get_output_directory
from pathlib import Path
import pandas as pd
import textstat as ts
import spacy
import textdescriptives as td
import matplotlib.pyplot as plt
import json
import gzip
from tqdm import tqdm

nlp=spacy.load("en_core_web_sm")

def process_dataset(document_iter):
    result=pd.DataFrame([{'docno': i.doc_id} for i in tqdm(document_iter)])
    return result


def process_metrics(document_iter):
    nlp.add_pipe("textdescriptives/readability", "textdescriptives/descriptive_stats")
    docs = nlp.pipe([doc.text[:5000] for doc in tqdm(document_iter)])
    metrics = td.extract_df(docs, include_text = False)
    return metrics


def plot_data_easy(df):
    fig = df.plot(kind='bar',  
        figsize=(20, 16), fontsize=26).get_figure()
    fig.savefig('test.pdf')

if __name__ == '__main__':
    # In the TIRA sandbox, this is the injected ir_dataset, injected via the environment variable TIRA_INPUT_DIRECTORY
    dataset = ir_datasets.load('workshop-on-open-web-search/document-processing-20231027-training')

    # The expected output directory, injected via the environment variable TIRA_OUTPUT_DIRECTORY
    output_dir = get_output_directory('.')
    
    # Document processors persist their results in a file documents.jsonl.gz in the output directory.
    output_file = Path(output_dir) / 'documents.jsonl.gz'
    
    # You can pass as many additional arguments to your program, e.g., via argparse, to modify the behaviour
    
    # process the documents, store results at expected location.
    processed_dataset=process_dataset(dataset.docs_iter())
    processed_metrics = process_metrics(dataset.docs_iter())
    processed_documents = pd.concat([processed_dataset, processed_metrics], axis=1)
    plot_data_easy(processed_documents)
    processed_documents.to_json(output_file, lines=True, orient='records')
    