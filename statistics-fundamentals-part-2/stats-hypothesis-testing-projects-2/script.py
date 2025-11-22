# Import libraries
import numpy as np
import pandas as pd
from scipy.stats import binomtest, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Import data
dogs = pd.read_csv('dog_data.csv')

# 1. Inspect the first few rows of data
print("--- Data Head ---")
print(dogs.head())

# 2. Save the is_rescue column for whippets
whippet_rescue = dogs.is_rescue[dogs.breed == 'whippet']

# 3. Calculate and print the number of whippet rescues
num_whippet_rescues = np.sum(whippet_rescue == 1)
print(f"\nNumber of whippet rescues: {num_whippet_rescues}")

# 4. Calculate and print the number of whippets
num_whippets = len(whippet_rescue)
print(f"Total number of whippets: {num_whippets}")

# 5. Run a binomial test
# Null Hypothesis: 8% of whippets are rescues
# Alternative Hypothesis: The proportion is different from 8%
# Note: Using binomtest as binom_test is deprecated/removed in modern Scipy
result = binomtest(num_whippet_rescues, num_whippets, p=0.08)
pval = result.pvalue
print(f"Binomial Test P-value: {pval}")

if pval < 0.05:
    print("Result: Significant difference from 8% (Reject Null)")
else:
    print("Result: No significant difference from 8% (Fail to Reject Null)")

# 6. Save the weights of whippets, terriers, and pitbulls
wt_whippets = dogs.weight[dogs.breed == 'whippet']
wt_terriers = dogs.weight[dogs.breed == 'terrier']
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']

# 7. Run an ANOVA
# Null Hypothesis: All breeds weigh the same amount on average
# Alternative Hypothesis: At least one pair of breeds has differing average weights
Fstat, pval = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print(f"\nANOVA P-value: {pval}")

if pval < 0.05:
    print("Result: Significant difference in average weights (Reject Null)")
else:
    print("Result: No significant difference in weights (Fail to Reject Null)")

# 8. Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Run Tukey's Range Test to find which specific pairs differ
output = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed)
print("\n--- Tukey's Range Test Results ---")
print(output)

# 9. Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

# Create a contingency table of color vs. breed
Xtab = pd.crosstab(dogs_ps.color, dogs_ps.breed)
print("\n--- Contingency Table (Color vs Breed) ---")
print(Xtab)

# 10. Run a Chi-Square Test
# Null Hypothesis: Breed and Color are an independent
# Alternative Hypothesis: There is an association between Breed and Color
chi2, pval, dof, exp = chi2_contingency(Xtab)
print(f"\nChi-Square P-value: {pval}")

if pval < 0.05:
    print("Result: Significant association between breed and color (Reject Null)")
else:
    print("Result: No significant association (Fail to Reject Null)")