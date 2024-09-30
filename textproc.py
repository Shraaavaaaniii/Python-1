#...
# from nltk.tokenize import word_tokenize,sent_tokenize
# import nltk 
# nltk.download('punkt_tab')
# text = 'Hello world, how are you?'
# words = word_tokenize(text)
# print(words)
# sentences = sent_tokenize(text)
# print(text)

from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["running","runner","ran","runs"]
stemmed_words = [ps.stem(words) for word in words]
print(stemmed_words)