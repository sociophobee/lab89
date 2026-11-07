"""Завдання 4. 10 найбільш уживаних слів і стовпчаста діаграма."""
import nltk
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt

for pkg in ("gutenberg", "punkt", "punkt_tab"):
    nltk.download(pkg, quiet=True)

tokens = [t.lower() for t in nltk.word_tokenize(gutenberg.raw("melville-moby_dick.txt"))]
top10 = nltk.FreqDist(tokens).most_common(10)

print("10 найбільш уживаних слів:")
for word, n in top10:
    print(f"{word!r:10} {n}")

words, counts = zip(*top10)
plt.figure(figsize=(9, 5))
plt.bar(words, counts, color="steelblue")
plt.title("10 найбільш уживаних слів (з пунктуацією та стоп-словами)")
plt.xlabel("Слово")
plt.ylabel("Кількість")
plt.tight_layout()
plt.savefig("top10_raw.png", dpi=150)
plt.show()