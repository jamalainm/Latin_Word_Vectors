# adapted from: https://www.shanelynn.ie/word-embeddings-in-python-with-spacy-and-gensim/

import os
import sys
import re
from gensim.models import Word2Vec
from gensim.models.phrases import Phraser, Phrases
from roman_abbreviations import abbvs
import json
from file_path import path

TEXT_DATA_DIR = path

def compile_corpus():
    texts = []         # list of text samples
    labels_index = {}  # dictionary mapping label name to numeric id
    labels = []        # list of label ids
    label_text = []    # list of label texts

    # read in texts and get rid of the excessive newlines

    for name in sorted(os.listdir(TEXT_DATA_DIR)):
        path = os.path.join(TEXT_DATA_DIR, name)
        with open(path, encoding='utf-8') as f:
            t = []
            for line in f:
                line = line.rstrip()
                t.append(line)
            t = ' '.join(t)
            texts.append(t)
        label_text.append(name)

    return texts
        
# Cleaning data - remove punctuation from every text

def add_line_breaks(texts):

    new_texts = []

    for text in texts:
        tokens = text.split(' ')
        for i,token in enumerate(tokens):
            if ".'" in token:
                tokens[i] += '\n'
            elif '."' in token:
                tokens[i] += '\n'
            elif '.' in token:
                if token not in abbvs:
                    tokens[i] += '\n'

            if len(token) > 0 and token[-1] == '-':
                tokens[i] += tokens[i+1]
                tokens.pop(i+1)

        new_text = ' '.join(tokens)
        new_texts.append(new_text)

    return new_texts

def clean_texts(texts):

    sentences = []
    # Go through each text in turn
    for ii in range(len(texts)):
        sentences = [re.sub(pattern=r'[\!"#$%&\*+,-./:;<=>?@^_`()|~=]', 
                            repl='', 
                            string=x
                        ).strip().split(' ') for x in texts[ii].split('\n') 
                        if not x.endswith('writes:')]
        sentences = [x for x in sentences if x != ['']]

        texts[ii] = sentences

    return texts

def concat_sentences(texts):

    all_sentences = []

    for text in texts:
        all_sentences += text
    
    return all_sentences

if __name__ == '__main__':
    texts = compile_corpus()
    texts = add_line_breaks(texts)
    texts = clean_texts(texts)
    all_sentences = concat_sentences(texts)
    with open('comedy_sentences.json','w') as f:
        json.dump(all_sentences,f)
