import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

risks = [
    {"risk": "SQL Injection", "likelihood": 4, "impact": 5},
    {"risk": "Weak Password Policy", "likelihood": 5, "impact": 3},
    {"risk": "Unpatched Server OS", "likelihood": 3, "impact": 5},
    {"risk": "Misconfigured S3 Bucket", "likelihood": 2, "impact": 4},
    {"risk": "Phishing Attack", "likelihood": 4, "impact": 4},
    {"risk": "Insecure API Endpoint", "likelihood": 3, "impact": 3},
]

df = pd.DataFrame(risks)
df["risk_score"] = df["likelihood"] * df["impact"]

def classify(score):
    if score >= 20:
        return "Critical"
    elif score >= 12:
        return "High"
    elif score >= 6:
        return "Medium"
    else:
        return "Low"

df["category"] = df["risk_score"].apply(classify)
df = df.sort_values("risk_score", ascending=False).reset_index(drop=True)

print("----------------------------------")
print("Security Risk Register")
print(df.to_string(index=False))
print("----------------------------------")

matrix = np.zeros((5, 5))

for r in risks:
    matrix[r["impact"] - 1, r["likelihood"] - 1] += 1

plt.figure(figsize=(6, 5))
plt.imshow(matrix, cmap="Reds", origin="lower")
plt.xticks(range(5), range(1, 6))
plt.yticks(range(5), range(1, 6))
plt.xlabel("Likelihood")
plt.ylabel("Impact")
plt.title("Risk Matrix Heatmap")
plt.colorbar(label="Number of Risks")
plt.savefig("risk_matrix_heatmap.png")

print("Risk matrix heatmap saved as risk_matrix_heatmap.png")
