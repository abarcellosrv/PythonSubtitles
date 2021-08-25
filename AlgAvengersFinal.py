import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk import FreqDist   
from nltk.corpus import stopwords
from collections import Counter

avengersraw = open('avengersplaintext.txt').read()

avengerssents = sent_tokenize(avengersraw.lower())

avengerswords = []
for s in avengerssents:
    sent = word_tokenize(s)
    avengerswords.append(sent)

avengerswords1 = [w for s in avengerswords for w in s]
stop_words = list(stopwords.words('english'))

avengersstopwords = [ w for w in avengerswords1 if not w in stop_words]

avengerspont = [w for w in avengersstopwords if w.isalnum() ]


avengersfdist = FreqDist(avengerspont)
maisfrequentes = avengersfdist.most_common()
frequentesred = []
contador = 0

for t in maisfrequentes:
    if contador >= len(avengerspont)*0.8: break
    frequentesred.append(t[0])  
    num = int(t[1])
    contador += num


for sent in avengerswords:
  summary = sent[:]
  for w in set(sent):
    if w in stop_words or w in frequentesred or not w.isalnum(): continue
    summary.remove(w)
  
  if sent != summary:
    print('Original: ' + ' '.join(sent))
    print('Reduzida: ' + ' '.join(summary))
   
    
   






