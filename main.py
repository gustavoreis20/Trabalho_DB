from collections import defaultdict
from gensim import models
from gensim import corpora
import database1 as db
import extract_dataset


dataset = extract_dataset.Dataset()
documents = dataset.extract_content()

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [
    [word for word in document.lower().split() if word not in stoplist]
    for document in documents
]

# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
'''
for x,y in zip(frequency, frequency.values()):
    print(x+"  -  "+str(y))
'''

texts = [
    [token for token in text if frequency[token] > 1]
    for text in texts
]
'''
for item in texts:
    print(item)
'''

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]



lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

doc = "comedy"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]  # convert the query to LSI space
print(vec_lsi)

from gensim import similarities
index = similarities.MatrixSimilarity(lsi[corpus])  # transform corpus to LSI space and index it

sims = index[vec_lsi]  # perform a similarity query against the corpus
print(list(enumerate(sims)))  # print (document_number, document_similarity) 2-tuples


db_mysql = db.Database()

sims = sorted(enumerate(sims), key=lambda item: -item[1])
for i, s in enumerate(sims):
    print(s, documents[i])
    value = str(documents[i])
    db_mysql.insert_values(f'"{value}"')

