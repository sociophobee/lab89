"""Завдання 3. Кількість слів і унікальних слів у тексті (Moby Dick, варіант 13)."""
import nltk
from nltk.corpus import gutenberg

for pkg in ("gutenberg", "punkt", "punkt_tab"):
    nltk.download(pkg, quiet=True)

raw = gutenberg.raw("melville-moby_dick.txt")
tokens = [t.lower() for t in nltk.word_tokenize(raw)]

total = len(tokens)
unique = len(set(tokens))
print("Текст: melville-moby_dick.txt")
print(f"Кількість слів (токенів): {total}")
print(f"Кількість унікальних слів: {unique}")
print(f"Співвідношення: унікальних слів — {unique / total:.2%} від загальної кількості")
print(f"Кожне унікальне слово вживається в середньому {total / unique:.1f} раза")