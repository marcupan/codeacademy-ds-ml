# Import the necessary libraries for data manipulation (pandas)
# and mathematical operations (numpy)
import pandas as pd
import numpy as np

# Import all required statistical tests upfront from scipy.stats for convenience
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# --- Load Datasets ---
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# --- TASK 1: Inspecting Lifespan Data ---
print("--- 1. Inspecting Lifespans Data ---")
print(lifespans.head()) # Print the first 5 rows to check the data structure

# --- TASK 2 & 3: Analyzing Vein Pack vs. 73 Years (ONE SAMPLE) ---

# 2. Extract lifespans for 'vein' pack subscribers
# Using a "pandas-style" selection for rows where 'pack' is 'vein' and selecting the 'lifespan' column
vein_pack_lifespans = lifespans[lifespans.pack == 'vein']['lifespan']
print("\n--- 3. Average Lifespan for Vein Pack ---")
avg_vein = np.mean(vein_pack_lifespans)
print(f"Average Vein Pack lifespan: {avg_vein:.2f} years") # Format for readability
print(f"Is it longer than 73 years? {avg_vein > 73}")

# 4 & 5. One-Sample T-test (ttest_1samp)
# Null Hypothesis: The average lifespan is 73 years (the comparison value)
tstat_v73, pval_v73 = ttest_1samp(vein_pack_lifespans, 73)
print("\n--- 5. T-test Result (Vein vs. 73) ---")
print(f"P-value (Vein vs 73): {pval_v73:.4f}")

# IMPROVEMENT: Making a decision based on the p-value
alpha = 0.05
if pval_v73 < alpha:
    print("Conclusion: Reject Null Hypothesis. The Vein Pack average lifespan is SIGNIFICANTLY different from 73 years.")
else:
    print("Conclusion: DO NOT Reject Null Hypothesis. There is NO SIGNIFICANT difference between the Vein Pack mean and 73 years.")


# --- TASK 6 & 7: Analyzing Artery Pack ---

# 6. Extract lifespans for 'artery' pack subscribers
artery_pack_lifespans = lifespans[lifespans.pack == 'artery']['lifespan']
print("\n--- 7. Average Lifespan for Artery Pack ---")
avg_artery = np.mean(artery_pack_lifespans)
print(f"Average Artery Pack lifespan: {avg_artery:.2f} years")
print(f"Is it longer than Vein Pack ({avg_vein:.2f} years)? {avg_artery > avg_vein}")


# --- TASK 8 & 9: Comparing Vein Pack vs. Artery Pack (TWO SAMPLES) ---

# 8 & 9. Two-Sample Independent T-test (ttest_ind)
# Null Hypothesis: The average lifespans are equal (Vein = Artery)
tstat_va, pval_va = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print("\n--- 9. T-test Result (Vein vs Artery) ---")
print(f"P-value (Vein vs Artery): {pval_va:.4f}")

# IMPROVEMENT: Making a decision based on the p-value
if pval_va < alpha:
    print("Conclusion: Reject Null Hypothesis. The average lifespan of the two packs are SIGNIFICANTLY different.")
else:
    print("Conclusion: DO NOT Reject Null Hypothesis. There is NO SIGNIFICANT difference between the means of the two packs.")


# --- TASK 10 & 11: Analyzing Association (Iron and Pack) ---

# 10. Inspecting Iron data
print("\n--- 10. Inspecting Iron Data ---")
print(iron.head())

# 11. Creating the Contingency Table
# Counts how many subscribers of each pack have low/normal/high iron levels
Xtab = pd.crosstab(iron.pack, iron.iron)
print("\n--- 11. Contingency Table (Iron) ---")
print(Xtab)

# --- TASK 12 & 13: Chi-Square Test ---

# 12 & 13. Chi-Square Test (chi2_contingency)
# Null Hypothesis: There is NO association between the pack type and iron level (they are independent)
chi2, pval_chi2, dof, exp = chi2_contingency(Xtab)
print("\n--- 13. Chi-Square Test Result ---")
print(f"P-value (Pack vs Iron): {pval_chi2:.4f}")

# IMPROVEMENT: Making a decision based on the p-value
if pval_chi2 < alpha:
    print("Conclusion: Reject Null Hypothesis. There is a SIGNIFICANT association (relationship) between the pack type and iron level.")
else:
    print("Conclusion: DO NOT Reject Null Hypothesis. There is NO SIGNIFICANT association between the pack type and iron level.")