'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as an image)
'''

import csv

#open the file
employee_data = open('employee_data.csv', 'r')
reader = csv.reader(employee_data)
next(reader)

#create an empty dictionary
emp_salary = {}
emp_salary_bonus = {}

#use a loop to iterate through the csv file
for row in reader:
    first_name = row[1]
    last_name = row[2]
    department = row[3]
    salary = float(row[5])

    emp_salary[f"{first_name} {last_name}"] = (f"${salary:,.2f}")
    emp_salary_bonus[f"{first_name} {last_name}"] = (f"${salary:,.2f}")
    #check if the employee fits the search criteria
    if department == 'Marketing':
        salary = salary * 1.1
        emp_salary_bonus[f"{first_name} {last_name}"] = (f"${salary:,.2f}")
    
print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
print("Original Employee File Report\n")
for name, value in emp_salary.items():
    print(f"Name: {name} Salary: {value}")
print()
print()
print("Bonuses Included Employee File Report\n")
for name, bonus_value in emp_salary_bonus.items():
    print(f"Name: {name} New Salary: {bonus_value}")

          
        

        
    
