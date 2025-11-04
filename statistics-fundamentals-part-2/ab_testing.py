
# 1. Import noshmishmosh
import noshmishmosh

# 2. Import numpy
import numpy as np

# 3. A/B Testing at Nosh Mish Mosh - Introduction (No code here)
print("-------------------------------------------------")
print("A/B Testing at Nosh Mish Mosh")
print("-------------------------------------------------")

# 4. Get all visitors
all_visitors = noshmishmosh.customer_visits

# 5. Get paying visitors
paying_visitors = noshmishmosh.purchasing_customers

# 6. Calculate visitor counts
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

print(f"Total visitors: {total_visitor_count}")
print(f"Paying visitors: {paying_visitor_count}")

# 7. Calculate baseline conversion rate
baseline_percent = (paying_visitor_count / total_visitor_count) * 100.0

# 8. Print baseline_percent
print(f"Baseline conversion rate: {baseline_percent}%")
print("-------------------------------------------------")

# 9. Get payment history
payment_history = noshmishmosh.money_spent

# 10. Calculate average payment
average_payment = np.mean(payment_history)
print(f"Average payment per customer: ${average_payment:.2f}")

# 11. Calculate new customers needed
target_revenue = 1240
new_customers_needed = np.ceil(target_revenue / average_payment)
print(f"New customers needed to reach ${target_revenue} extra revenue: {int(new_customers_needed)}")

# 12. Calculate percentage point increase
percentage_point_increase = (new_customers_needed / total_visitor_count) * 100
print(f"Percentage point increase needed: {percentage_point_increase}%")
print("-------------------------------------------------")


# 13. Calculate Minimum Detectable Effect (MDE)
mde = (percentage_point_increase / baseline_percent) * 100.0

# 14. Print mde
print(f"Minimum Detectable Effect (MDE): {mde:.2f}%")
print("-------------------------------------------------")

# 15. Statistical significance threshold is 10%
statistical_significance = 0.10

# 16. Calculate sample size
# We will use a standard formula to calculate the required sample size per variation for an A/B test.
# We'll assume a statistical power of 80%, which is a common choice.

# Z-score for significance level (alpha = 10% -> 0.10, two-tailed test -> alpha/2 = 0.05)
Z_alpha = 1.645
# Z-score for statistical power (beta = 20% -> 0.20, for 80% power)
Z_beta = 0.84

# Baseline conversion rate (p1) and the new desired conversion rate (p2)
p1 = baseline_percent / 100.0
p2 = p1 + (percentage_point_increase / 100.0)

# Formula for sample size per group
# n = (Z_alpha * sqrt(2*p_avg*(1-p_avg)) + Z_beta * sqrt(p1*(1-p1) + p2*(1-p2)))^2 / (p2-p1)^2
# A simpler and widely used formula is:
# n = (Z_alpha/2 + Z_beta)^2 * (p1(1-p1) + p2(1-p2)) / (p1-p2)^2
# Let's use the simpler one.

numerator = (Z_alpha + Z_beta)**2 * (p1 * (1 - p1) + p2 * (1 - p2))
denominator = (p2 - p1)**2

# Sample size for each group (control and treatment)
sample_size_per_group = numerator / denominator

# Total sample size for the A/B test
ab_sample_size = sample_size_per_group * 2

print(f"Required sample size per group: {int(np.ceil(sample_size_per_group))}")
print(f"Total sample size for A/B test: {int(np.ceil(ab_sample_size))}")
print("-------------------------------------------------")
