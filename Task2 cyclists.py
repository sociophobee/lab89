"""Завдання 2. Аналіз використання велодоріжок Монреаля за 2015 рік (варіант 13)."""
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.width", 110)
pd.set_option("display.max_columns", 30)

FILE = "comptagevelo2015.csv"

# Завантаження (файл може бути в кодуванні latin-1)
try:
    df = pd.read_csv(FILE, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(FILE, encoding="latin-1")

df = df.rename(columns={"Unnamed: 1": "Time"})   # безіменний стовпець із часом
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
df = df.dropna(subset=["Date"])

# Первинний аналіз
print(df.head())
df.info()
print(df.describe())

# Оброблення: пропуски (NaN) замінюємо нулями
paths = [c for c in df.columns if c not in ("Date", "Time") and pd.api.types.is_numeric_dtype(df[c])]
print("\nПропущені значення за стовпцями:")
print(df[paths].isna().sum()[lambda x: x > 0])
df[paths] = df[paths].fillna(0)

# Загальна кількість велосипедистів за рік по всіх велодоріжках
totals = df[paths].sum().sort_values(ascending=False)
print("\nКількість велосипедистів за 2015 рік по кожній велодоріжці:")
print(totals)
print("Усього за рік:", int(totals.sum()))

# Три обрані велодоріжки: найпопулярніший місяць
chosen = list(totals.index[:3])            # три найпопулярніші; можна замінити своїми
df["Month"] = df["Date"].dt.month
monthly = df.groupby("Month")[paths].sum()
print("\nОбрані велодоріжки:", chosen)
for p in chosen:
    m = monthly[p].idxmax()
    print(f"{p}: найпопулярніший місяць — {m} ({int(monthly[p].max())} велосипедистів)")

# Групування за місяцями та динаміка однієї велодоріжки
track = chosen[0]
print(f"\nДинаміка використання велодоріжки {track} за місяцями:")
print(monthly[track])

plt.figure(figsize=(9, 5))
plt.plot(monthly.index, monthly[track], marker="o")
plt.title(f"Кількість велосипедистів на велодоріжці {track}, 2015 рік")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("cyclists_2015_monthly.png", dpi=150)
plt.show()