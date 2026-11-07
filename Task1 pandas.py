"""Завдання 1. Аналіз CSV-файлу з практичної роботи 5 (тривалість життя, Світовий банк)."""
import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)

# Завантаження даних у DataFrame
df = pd.read_csv("world_bank_le_us_ua.csv", sep=";", encoding="utf-8-sig")

print("Вміст DataFrame")
print(df)
print("\nПерші 3 рядки: df.head(3)")
print(df.head(3))
print("\nТипи даних: df.dtypes")
print(df.dtypes)
print("\nКількість рядків і стовпців: df.shape")
print(df.shape)
print("\nОписова статистика: df.describe()")
print(df.describe())

# Попереднє оброблення
df["Year"] = df["Year"].astype(int)
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df = df.sort_values(["Country Name", "Year"])
# новий розрахунковий стовпець: річна зміна показника всередині кожної країни
df["Change"] = df.groupby("Country Name")["Value"].diff().round(3)
print("\nПісля оброблення (додано стовпець Change)")
print(df[["Country Name", "Year", "Value", "Change"]].head(12))

# Фільтрація
filtered = df[(df["Year"] >= 2015) & (df["Value"] > 75)]
print("\nФільтрація: Year >= 2015 і Value > 75")
print(filtered[["Country Name", "Year", "Value"]])

# Сортування
sorted_df = df.sort_values("Value", ascending=False)
print("\nСортування за Value (за спаданням), топ-5")
print(sorted_df[["Country Name", "Year", "Value"]].head(5))

# Групування
grouped = df.groupby("Country Name")["Value"].agg(["mean", "max", "min"]).round(3)
print("\nГрупування за країною: середнє, максимум, мінімум")
print(grouped)
print("\nКількість унікальних значень")
print("Країн:", df["Country Name"].nunique())
print("Років:", df["Year"].nunique())

# Збереження результатів у новий CSV
df.to_csv("life_expectancy_processed.csv", sep=";", index=False, encoding="utf-8-sig")
grouped.to_csv("life_expectancy_grouped.csv", sep=";", encoding="utf-8-sig")
print("\nРезультати збережено: life_expectancy_processed.csv, life_expectancy_grouped.csv")