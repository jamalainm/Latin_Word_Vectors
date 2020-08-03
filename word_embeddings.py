import json
from gensim.models import Word2Vec
from gensim.models.phrases import Phraser, Phrases

def define_model(sentences):

    model = Word2Vec(sentences,
            min_count = 3,
            size = 300,
            workers = 2,
            window = 5,
            iter = 100)

    return model

if __name__ == "__main__":
    with open('comedy_sentences.json','r') as f:
        sentences = json.load(f)

    model = define_model(sentences)

    print(model)

    print(model.vector_size)

    print(len(model.wv.vocab))

    model.save('comedy_word2vec.model')
