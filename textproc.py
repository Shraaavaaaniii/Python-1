#...
# import nltk 
# from nltk.tokenize import word_tokenize,sent_tokenize
# nltk.download('punkt_tab')
# text = 'Hello world, how are you?'
# words = word_tokenize(text)
# print(words)
# sentences = sent_tokenize(text)
# print(sentences)

# Stemming
# from nltk.stem import PorterStemmer
# ps = PorterStemmer()
# words = ["running","runner","ran","runs"]
# stemmed_words = [ps.stem(word) for word in words]
# print(stemmed_words)

#Lemmatization
import nltk
from nltk.stem import WordNetlemmatizer
nltk.download('wordnet')
lemmatizer = WordNetlemmatizer()
words = ["running","runner","ran","runs"]
lemmatized_word = [lemmatizer.lemmatize(word,pos='v') for word in words]
print(lemmatized_word)