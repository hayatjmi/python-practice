import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
print("\nAverage Marks:", df["Marks"].mean())