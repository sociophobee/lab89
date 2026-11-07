"""Завдання 5. Видалення стоп-слів і пунктуації, 10 найуживаніших слів."""
import string
import nltk
from nltk.corpus import gutenberg, stopwords
import matplotlib.pyplot as plt

for pkg in ("gutenberg", "punkt", "punkt_tab", "stopwords"):
    nltk.download(pkg, quiet=True)

tokens = [t.lower() for t in nltk.word_tokenize(gutenberg.raw("melville-moby_dick.txt"))]
stop = set(stopwords.words("english"))
punct = set(string.punctuation) | {"--", "''", "``", "’", "‘", "“", "”", "—"}

clean = [t for t in tokens if t not in stop and t not in punct and t.isalpha()]
print(f"Було токенів: {len(tokens)}, після очищення: {len(clean)}")

top10 = nltk.FreqDist(clean).most_common(10)
print("\n10 найбільш уживаних слів після видалення стоп-слів і пунктуації:")
for word, n in top10:
    print(f"{word:10} {n}")

words, counts = zip(*top10)
plt.figure(figsize=(9, 5))
plt.bar(words, counts, color="seagreen")
plt.title("10 найбільш уживаних слів без стоп-слів і пунктуації")
plt.xlabel("Слово")
plt.ylabel("Кількість")
plt.tight_layout()
plt.savefig("top10_clean.png", dpi=150)
plt.show()