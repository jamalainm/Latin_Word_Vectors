import json
from gensim.models import Word2Vec
from gensim.models.phrases import Phraser, Phrases

def two_word_phrases(sentences):

    common_terms = ['est','quis','quid','a','ab','ex','e']

    phrases = Phrases(sentences, common_terms=common_terms)

    bigram = Phraser(phrases)

    return list(bigram[sentences])

def most_common_phrases(sentences):

    bigram = Phrases(sentences, min_count=1, delimiter=b' ')

    trigram = Phrases(bigram[sentences], min_count=1, delimiter=b' ')

    common_phrases = {}

    grams = []

    for sent in sentences:
        bigrams_ = [b for b in bigram[sent] if b.count(' ') == 1]
        grams += bigrams_
        trigrams_ = [t for t in trigram[bigram[sent]] if t.count(' ')==2]
        grams += trigrams_

    for phrase in grams:
        if phrase in common_phrases:
            common_phrases[phrase] += 1
        else:
            common_phrases.update({phrase : 1})

    return common_phrases

if __name__ == '__main__':
    with open('comedy_sentences.json','r') as f:
        sentences = json.load(f)

    common_phrases = most_common_phrases(sentences)

    print(len(common_phrases))

    sort_phrases = sorted(common_phrases.items(), key=lambda x: x[1], reverse=True)

    for i in sort_phrases[0:100]:
        print(i[0], i[1])
