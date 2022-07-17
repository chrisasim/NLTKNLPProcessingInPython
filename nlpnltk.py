#what is nlp. automatic manipulation for language understading and semtimental analysis.
#extraction of information, data cleaning, token manipulation and feature a pipeline where the output of a command 
#cleaning the text data, tokenization, stop words removal, stemming.
#the process of converting words into numbers are called vectorization.
#text classification is the process of assigning tags or categories to text according to its content. 
#what is nltk? Natural language toolkit is a platform used for building python programs tat work with human language data for applying in statistical natural language. 
#google colab klasika.
from sklearn.datasets import fetch_20newsgroups
text_data = fetch_20newsgroups()
import numpy as np
print(type(text_data))
raw_text = text_data.data
print(raw_text)
clear_text_1 = []
def to_lower_case(data):
 for words in raw_text:
  clear_text_1.append(str.lower(words))
to_lower_case(raw_text)

clear_text_2 = []
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')
sent_tok = []
for sent in clear_text_1:
 sent = sent_tokenize(sent)
 sent_tok.append(sent)
print(sent_tok)

#word tokenize
clear_text_2 = [word_tokenize(i) for i in clear_text_1]
clear_text_3 = []
print(clear_text_2)
import re
clear_text_3 = []
for words in clear_text_3:
 clear = []
 for w in words:
  res = re.sub(r'[^\w\s]', "", w)
  if (res != ""):
     clear.append(res)
  clear_text_3.append(clear)
clear_text_3 = []
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

clear_text_4 = []
for words in clear_text_4:
 w = []
 for word in words:
  if not word in stopwords.words('english'):
    w.append(word)
  clear_text_4.append(w)
#stage 5 stemming
from nltk.stem.porter import PorterStemmer
port = PorterStemmer()
a = [port.stem(i) for i in ["reading", "washing", "wash", "Diving"]]
print(a)

clear_text_5 = []
for words in clear_text_4:
 w = []
 for word in words:
  w.append(word)
 clear_text_5.append(w)
print(clear_text_5)

from nltk.stem.wordnet import WordNetLemmatizer
wnet = WordNetLemmatizer()
import nltk
nltk.download('wordnet')
#lemmatizer
lem = []

