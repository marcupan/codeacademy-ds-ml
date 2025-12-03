# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, binom_test

# --- 1. Load and Inspect Data ---
abdata = pd.read_csv('clicks.csv')
print("--- 1. Data Inspection (First 5 Rows) ---")
print(abdata.head())

# --- 2. Initial Analysis: Chi-Square Test for Association ---
print("\n--- 2. Contingency Table (Group vs. Purchase) ---")
# Create a contingency table (Xtab) to count purchases/non-purchases per group
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)

# --- 3. Run Chi-Square Test ---
chi2, pval, dof, expected = chi2_contingency(Xtab)
print("\n--- 3. Chi-Square Test P-value ---")
print(f"P-value: {pval:.6f}")

alpha = 0.05
if pval < alpha:
    print(
        "Conclusion: Reject Null Hypothesis. There is a SIGNIFICANT difference in purchase rates across groups A, B, and C.")
else:
    print("Conclusion: DO NOT Reject Null Hypothesis. No significant difference in purchase rates.")

# --- 4. Calculate Total Visits ---
num_visits = len(abdata)
print(f"\n--- 4. Total Weekly Visitors ---")
print(f"Total Visitors (num_visits): {num_visits}")

# --- 5, 6, 7. Calculate Required Sales and Purchase Proportions (Target) ---
target_revenue = 1000.0

print("\n--- 5, 6, 7. Sales and Proportion Targets for $1000 Revenue ---")

# Price $0.99
price_099 = 0.99
num_sales_needed_099 = target_revenue / price_099
p_sales_needed_099 = num_sales_needed_099 / num_visits
print(
    f"Price $0.99: Sales needed={num_sales_needed_099:.2f} | Target Proportion (p_sales_needed_099)={p_sales_needed_099:.4f}")

# Price $1.99
price_199 = 1.99
num_sales_needed_199 = target_revenue / price_199
p_sales_needed_199 = num_sales_needed_199 / num_visits
print(
    f"Price $1.99: Sales needed={num_sales_needed_199:.2f} | Target Proportion (p_sales_needed_199)={p_sales_needed_199:.4f}")

# Price $4.99
price_499 = 4.99
num_sales_needed_499 = target_revenue / price_499
p_sales_needed_499 = num_sales_needed_499 / num_visits
print(
    f"Price $4.99: Sales needed={num_sales_needed_499:.2f} | Target Proportion (p_sales_needed_499)={p_sales_needed_499:.4f}")

# --- 8, 9. Extract Actual Sample Sizes and Sales ---
print("\n--- 8, 9. Actual Sample Sizes and Sales ---")

# Group A ($0.99)
group_A_data = abdata[abdata.group == 'A']
samp_size_099 = len(group_A_data)
sales_099 = np.sum(group_A_data.is_purchase == 'Yes')
print(f"Group A: Sample Size={samp_size_099}, Actual Sales={sales_099}, Actual Rate={sales_099 / samp_size_099:.4f}")

# Group B ($1.99)
group_B_data = abdata[abdata.group == 'B']
samp_size_199 = len(group_B_data)
sales_199 = np.sum(group_B_data.is_purchase == 'Yes')
print(f"Group B: Sample Size={samp_size_199}, Actual Sales={sales_199}, Actual Rate={sales_199 / samp_size_199:.4f}")

# Group C ($4.99)
group_C_data = abdata[abdata.group == 'C']
samp_size_499 = len(group_C_data)
sales_499 = np.sum(group_C_data.is_purchase == 'Yes')
print(f"Group C: Sample Size={samp_size_499}, Actual Sales={sales_499}, Actual Rate={sales_499 / samp_size_499:.4f}")

# --- 10, 11, 12. Run Binomial Tests (H_a: Actual Rate > Target Rate) ---
print("\n--- 10, 11, 12. Binomial Test Results (Target Revenue Check) ---")

# Group A Test
pvalueA = binom_test(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')
print(f"P-value Group A ($0.99): {pvalueA:.4f}")

# Group B Test
pvalueB = binom_test(sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')
print(f"P-value Group B ($1.99): {pvalueB:.4f}")

# Group C Test
pvalueC = binom_test(sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')
print(f"P-value Group C ($4.99): {pvalueC:.4f}")

# --- 13. Final Business Decision ---
print("\n--- 13. Final Business Decision (Based on P-value < 0.05) ---")

if pvalueC < alpha:
    final_answer = '4.99'
    print(
        f"Conclusion: Only Group C ($4.99) has a purchase rate ({sales_499 / samp_size_499:.4f}) SIGNIFICANTLY greater than the required target ({p_sales_needed_499:.4f}).")
    print(f"Recommended Price: ${final_answer}")
else:
    # This case is highly unlikely given the calculated P-values, but included for completeness
    final_answer = 'None of the above'
    print("Conclusion: None of the groups significantly exceeded the target purchase rate needed for $1000 revenue.")
    print(f"Recommended Price: {final_answer}")
