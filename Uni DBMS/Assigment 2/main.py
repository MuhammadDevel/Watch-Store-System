import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

df["Health_Score"] = (
    df["Quality of Sleep"] +
    (df["Sleep Duration"] * 2) -
    df["Stress Level"] +
    (df["Physical Activity Level"] / 30)
)

df["Performance"] = df["Health_Score"].apply(lambda x:
    "Good" if x > 15 else ("Average" if x >= 10 else "Poor"))

df["Healthy"] = df.apply(lambda row:
    "Yes" if (row["Sleep Duration"] >= 7 and
              row["Stress Level"] <= 5 and
              row["Physical Activity Level"] >= 30)
    else "No", axis=1)

def risk(row):
    if row["Stress Level"] > 7 and row["Sleep Duration"] < 6:
        return "High Risk"
    elif 5 <= row["Stress Level"] <= 7:
        return "Medium Risk"
    else:
        return "Low Risk"

df["Risk_Level"] = df.apply(risk, axis=1)

df.to_csv("updated_dataset.csv", index=False)

print(df.head())



# Performance
df["Performance"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.title("Performance Distribution")
plt.ylabel("")
plt.show()


# Healthy Lifestyle
df["Healthy"].value_counts().plot(kind="barh")
plt.title("Healthy Lifestyle")
plt.xlabel("Count")
plt.show()


# Risk Level
risk_counts = df["Risk_Level"].value_counts()

plt.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Sleep Risk Levels")
plt.show()


# Sleep vs Quality
avg_data = df.groupby("Sleep Duration")["Quality of Sleep"].mean()

plt.plot(avg_data.index, avg_data.values, marker='o')
plt.title("Sleep vs Quality (Average)")
plt.xlabel("Sleep Duration")
plt.ylabel("Quality")
plt.grid()
plt.show()


# Sleep Disorder
df["Sleep Disorder"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.title("Sleep Disorder Distribution")
plt.ylabel("")
plt.show()


# Occupation vs Sleep
plt.figure(figsize=(10,6))
avg_sleep = df.groupby("Occupation")["Sleep Duration"].mean()
avg_sleep.plot(kind="bar")

plt.title("Average Sleep by Occupation")
plt.xlabel("Occupation")
plt.ylabel("Sleep Duration")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')

plt.tight_layout()
plt.show()