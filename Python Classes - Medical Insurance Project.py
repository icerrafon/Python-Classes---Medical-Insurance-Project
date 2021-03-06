#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print(f"{self.name}'s estimated insurance costs is {estimated_cost} dollars.")

  def update_age(self, new_age):
    self.age = new_age
    print(f"{self.name} is now {self.age} years old.")
    self.estimated_insurance_cost()

  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print(self.name + " has " + str(self.num_of_children) + " child.")
    else:
      print(self.name + " has " + str(self.num_of_children) + " children.")
    self.estimated_insurance_cost()

  def update_smoker(self, new_smoker):
    self.smoker = new_smoker
    
    if new_smoker == 0: 
      print(f"{self.name} is a non-smoker.")
    else:
      print(f"{self.name} is a smoker.")
    self.estimated_insurance_cost()

  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print(f"{self.name}'s bmi is now {self.bmi}")
    self.estimated_insurance_cost()

  def patient_profile(self):
    patient_information = {}
    patient_information["name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information




# In[2]:


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)


# In[3]:


print(patient1.name)

patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)
patient1.update_bmi(26.3)
patient1.update_smoker(1)
print(patient1.patient_profile())

