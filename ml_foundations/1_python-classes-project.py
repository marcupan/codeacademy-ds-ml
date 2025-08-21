class Patient:
    # Task 1: Expand constructor with all parameters
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex  # 0 = male, 1 = female
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker  # 0 = non‑smoker, 1 = smoker

    # Task 3 & 4: Method to estimate insurance cost and print result
    def estimated_insurance_cost(self):
        estimated_cost = (
                250 * self.age
                - 128 * self.sex
                + 370 * self.bmi
                + 425 * self.num_of_children
                + 24000 * self.smoker
                - 12500
        )
        print(f"{self.name}’s estimated insurance cost is {estimated_cost} dollars.")
        return estimated_cost

    # Task 5–7: Method to update age, print and re‑estimate cost
    def update_age(self, new_age):
        self.age = new_age
        print(f"{self.name} is now {self.age} years old.")
        self.estimated_insurance_cost()

    # Task 8–11: Method to update number of children with proper grammar and re‑estimate cost
    def update_num_children(self, new_num_children):
        self.num_of_children = new_num_children
        if self.num_of_children == 1:
            print(f"{self.name} has {self.num_of_children} child.")
        else:
            print(f"{self.name} has {self.num_of_children} children.")
        self.estimated_insurance_cost()

    # Task 12–13: Method to return all patient info as a dict
    def patient_profile(self):
        patient_information = {
            "Name": self.name,
            "Age": self.age,
            "Sex": "Female" if self.sex == 1 else "Male",
            "BMI": self.bmi,
            "Number of Children": self.num_of_children,
            "Smoker": bool(self.smoker),
            "Estimated Insurance Cost": self.estimated_insurance_cost()
        }
        return patient_information


# === Testing the Patient class ===

# Task 2: Create an instance and print attributes
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.age, patient1.sex, patient1.bmi, patient1.num_of_children, patient1.smoker)

# Task 4: Estimate cost for patient1
patient1.estimated_insurance_cost()

# Task 6–7: Update age and re‑estimate
patient1.update_age(26)

# Task 9–10: Update number of children and re‑estimate
patient1.update_num_children(1)
patient1.update_num_children(2)

# Task 13: Print patient profile dict
print(patient1.patient_profile())
