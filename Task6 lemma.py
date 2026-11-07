"""Завдання 6. Лематизація та стемінг, 10 найуживаніших слів."""
import string
import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

for pkg in ("gutenberg", "punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4"):
    nltk.download(pkg, quiet=True)

tokens = [t.lower() for t in nltk.word_tokenize(gutenberg.raw("melville-moby_dick.txt"))]
stop = set(stopwords.words("english"))
clean = [t for t in tokens if t.isalpha() and t not in stop and t not in string.punctuation]

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(t) for t in clean]
print("10 найбільш уживаних слів після лематизації:")
for word, n in nltk.FreqDist(lemmas).most_common(10):
    print(f"{word:10} {n}")

stemmer = PorterStemmer()
stems = [stemmer.stem(t) for t in clean]
print("\n10 найбільш уживаних основ після стемінгу (Porter):")
for word, n in nltk.FreqDist(stems).most_common(10):
    print(f"{word:10} {n}")