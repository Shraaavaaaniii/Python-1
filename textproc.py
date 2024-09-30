#...
from nltk.tokenize import word_tokenize,sent_tokenize
text = 'Hello world, how are you?'
words = word_tokenize(text)
print(words)
sentences = sent_tokenize(text)
print(text)