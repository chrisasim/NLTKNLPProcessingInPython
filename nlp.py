#spell checking, social media processing, applications of nlp
#keyword search
#infromation extraction, advertisement matching,
#sentimental analysis, speech recognition, cortana, siri, alexa AI,chat bots, machine translation
#NLP is categorized into NLU and NLG
#Mapping input to useful representations, meaninful expressions and sentences, text planning, sentences planning, text realization,
#NLU: ambiguity such as lexical ambiguity, syntactic ambiguity, referential ambiguity,
#she is looking for a match, the fisherman went to the bank.
#The chicken is ready to eat. Visiting relatives can be boring. I saw the man with the binoculars.
#Referential Ambiguity -> the boy told his father the theft. He was very upset.
#NLp -> we need to install NLP with Python NLTK.classification, tokenization, stemming, bag of words and lemmatization. 
#Tokenization -> In this sentence we have five tokens. Today we will understand tokenization. 
#Break a complex sentence into words
#Understand the importance of each.
import os
import nltk
import nltk.corpus
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import PorterStemmer
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
os.listdir(nltk.data.find("corpora"))
nltk.corpus.gutenberg.fileids()
hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
#According to the artificial intelligence, it is easy to how it works on a string. 
#nltk . tokenize the word tokenize.
#type(AI)
for word in hamlet[:500]:
 print(word, sep= ' ', end= ' ')

AI = """The term "artificial intelligence" had previously been used to describe machines that mimic and display "human" cognitive skills that are associated with the human mind, such as "learning" and "problem-solving". This definition has since been rejected by major AI researchers who now describe AI in terms of rationality and acting rationally, which does not limit how intelligence can be articulated. """
type(AI)
from nltk.tokenize import word_tokenize
AI_tokens = word_tokenize(AI)
print(AI_tokens)
print(len(AI_tokens))
from nltk.probability import FreqDist
fdist = FreqDist()
for word in AI_tokens:
 fdist[word.lower()]+=1
print(fdist)
print(fdist['artificial'])
print(len(fdist))
fdist_top10 = fdist.most_common(10)
print(fdist_top10)
from nltk.tokenize import blankline_tokenize
AI_blank = blankline_tokenize(AI)
len(AI_blank)
print(AI_blank)
from nltk.util import bigrams, trigrams, ngrams
string ="The best and the most beatiful thins in the world cannot be seen or even touched, they must be felt with the heart"
quotes_tokens = nltk.word_tokenize(string)
print(quotes_tokens)
quotes_bigrams = list(nltk.bigrams(quotes_tokens))
print(quotes_bigrams)
quotes_ngrams = list(nltk.ngrams(quotes_tokens, 5))
print(quotes_ngrams)
#we need to make some changes to the tokens. Stemming is to normalize the words into its based form or root form
#In this discriminating that is why this approach presents some limitations. 
#there are different types of stemming . Import stemming that is hy it gives us an output. 
#from nltk.stem import PorterStemmer
pst = PorterStemmer()

pst.stem("having")

print(pst.stem("having"))
words_to_stem = ["give", "giving", "given", "gave"]
for words in words_to_stem:
 print(words+ ":" + pst.stem(words))

#from ntlk.stem import lancasterStemmer
lst = LancasterStemmer()
for words in words_to_stem:
 print(words+":"+ lst.stem(words))

#lemmatization groups together different inflected forms od words, somehow similar stemming, as it masp several words into one common root
#output of lemmatization is a proper word
#For example, a lemmatiser should map gone, going and went into go.
word_lem = WordNetLemmatizer()
word_lem.lemmatize('corpora')
for words in words_to_stem:
 print(words+ ":" + word_lem.lemmatize(words))
#stop words in english words for example take said begin various recently very most they are are they helpful or not?
#a list of stop words , very useful in English language, but not in natural processing.
#print(len(stopwords.words('english')))
print(fdist_top10)
import re
#pos parts of speech. grammar, engilsh quetions, prepositions, verbs passives, worksheets, future, adjectives, tenses, relatives, affirmitive, genitive.
#pos tags and descriptions so many tags and descriptions from coordinating conjunction to nlp
#words to sentence data mining. the dot is a noun ate is a word , implement tags using nltk library. 
sent = "Timothy is a natural when it comes to drawing"
sent_tokens = word_tokenize(sent)
#for token in sent_tokens:
# print(nltk.)


#what are named entity recognition - > movie, monetary value, organization, location, quantities, person
#this step extracts all the faces parts of speech
#classification step, classified to respected category respected and more.
#sometimes it is possible, the user of knowledge graphs is also wikipedia, If we look at the examples. 
#organization, person, location and organization.
#nltk module in pyhon 
from nltk import ne_cjuck
NE_sent = "The US president stays in the WHITE HOUSE"
NE_tokens = word_tokenizing(NE_sent)
NE_tags = nltk.pos_tag(NE_tokens)
NE_NER = ne_chunk(NE_tags)
print(NE_NER)
#ner entities list we have dual location, facility, organization, geolocation entity, syntax, rules, principles and processes and constructs the language into a sentence, we have a certian rules phase structure rules, syntax tree, is a kdtree is a tree representation of syntactic structure of sentences or strings. 
#kdtree data structure is geo location queries. 
#basic consituent analysis of a sentence: sentence verb phrase prepositional phrase, chunking. 
#chunking basically means picking up individual pieces of information and grouping them into bigger pieces. 
#bigger pieces are also known as chunks. 
#we caught the pink panther. preposition, verb , data mining, jj, nnn, np and np.
new  = "The big cat ate the little mouse who was after fresh cheese"
new_tokens = nltk.post_tag(word_tokenization)
print(new_tokens)
grammar = r"NP: {<DT>?<JJ>'<NN>}"
chuck_parser = nltk.RegexParser(grammar_np)
chunk_result = chunk_parser.parse(new_tokens)
print(chunk_result)
#NLP is a natural language processing which is part og computer science and artificial intelligence which 
#deals with human languages. 
#it is a combination of artificial intelligence human anguage and computer science. 
