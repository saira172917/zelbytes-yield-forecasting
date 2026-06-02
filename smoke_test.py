import pandas as pd

data = {
    "temperature": [24.5],
    "humidity": [88],
    "co2": [650],
    "yield_kg": [15.2]
}

df = pd.DataFrame(data)

print("Mushroom Yield Sample Data")
print(df)