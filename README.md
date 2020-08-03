# Latin_Word_Vectors

A repository to create word vectors and create lists of frequent 2-3 word phrases

* <clean_texts.py> creates a list of sentences from PHI-like texts.
* <roman_abbreviations.py> is a list of common Roman abbreviations with '.' in them; included in text cleaning so that we don't accidentally end sentences too early.
* <word_embeddings.py> will create a Word2Vec model for the specified list of tokenized sentences.
* <phrase_detection.py> outputs the most common 2-3 word phrases from the list of tokenized sentences.
* <all_sentences.json> is a tokenized list of sentences from PHI-like data
* <latin_word2vec.model> is a vector model based on a PHI-like corpus
* <comedy_sentences.json> is a subset based on Plautus and Terence
* <comedy_word2vec.model> is a vector model based on Plautus and Terence
