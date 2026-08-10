import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

n = 30

devops_data = pd.DataFrame({
    "deployment_frequency_per_week": np.random.normal(8, 1.5, n),
    "vulnerabilities_found": np.random.poisson(6, n),
    "mean_time_to_recover_hrs": np.random.normal(5, 1, n)
})

devsecops_data = pd.DataFrame({
    "deployment_frequency_per_week": np.random.normal(7, 1.2, n),
    "vulnerabilities_found": np.random.poisson(2, n),
    "mean_time_to_recover_hrs": np.random.normal(2.5, 0.7, n)
})

summary = pd.DataFrame({
    "DevOps_Mean": devops_data.mean(),
    "DevSecOps_Mean": devsecops_data.mean()
})

print("----------------------------------")
print("Comparative Summary: DevOps vs DevSecOps")
print(summary.round(2))
print("----------------------------------")

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
metrics = summary.index

for i, metric in enumerate(metrics):
    axes[i].bar(["DevOps", "DevSecOps"], summary.loc[metric])
    axes[i].set_title(metric)

plt.tight_layout()
plt.savefig("devops_vs_devsecops_comparison.png")

devops_data.to_csv("devops_synthetic_data.csv", index=False)
devsecops_data.to_csv("devsecops_synthetic_data.csv", index=False)

print("Charts and datasets saved successfully")
