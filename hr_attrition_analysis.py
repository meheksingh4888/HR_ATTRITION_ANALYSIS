import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# optimal chart styling 
plt.style.use('ggplot')
#Applies a good visual theme.

sns.set(style='whitegrid')
#Adds clean white background + grid lines.

#Load the dataset
df=pd.read_csv("data/HR_Employee_Attrition.csv")

#shows first 5 rows of the dataset
print(df.head)


# Step 3:-- CHECK DATASET SHAPE AND STRUCTURE

# Check number of rows and columns
print("Shape of the dataset:", df.shape)

# Show column names
print("column names:",df.columns.tolist())

## Basic info
print("Dataset Info: ",df.info())
#Shows:data types , non-null values, memory usage

#STEP 4: Check Missing Values

## Check missing values in each column
print("Missing values: " , df.isnull().sum())
#df.isnull() Checks each cell:True if missing , False if not missing

#.sum() Counts total missing values per column

#STEP 5: Check Duplicate Rows

## Check duplicate rows
print("duplicate rows: ",df.duplicated().sum())

#STEP 6: Create Numeric Attrition Column

## Convert Attrition into numeric flag
df["Attrition_flag"] = df["Attrition"].map({"Yes": 1, "No": 0})
## Check result
print(df[["Attrition","Attrition_flag"]].head())

#STEP 7: Overall Attrition Rate
attrition_rate=df['Attrition_flag'].mean()*100

print(f"Overall Attrition Rate :{attrition_rate:.2f}%")
# how this code of line works:

# Yes = 1
# No = 0
#Example:
# If 2 employees left out of 10:
# values = [1,0,0,1,0,0,0,0,0,0]
# mean = 0.2
#percentage = 20%

#STEP 8: KPI Summary

total_employees = len(df)
employees_left = df['Attrition_flag'].sum()
employees_stayed = total_employees - employees_left
avg_income=df["MonthlyIncome"].mean()

print("Total Employees:  ", total_employees)
print("Employees Left:  ", employees_left)
print("Employees Stayed: ", employees_stayed)
print(f"Attrition Rate: {attrition_rate:.2f}% ")
print(f"Average Monthly Income: {avg_income:.2f} ")

#STEP 9: Attrition by Department

dept_attrition = df.groupby("Department")["Attrition_flag"].mean() * 100
# groupby("Department") Groups all employees by department.
#["Attrition_Flag"].mean() Calculates attrition rate in each department.

print("Attriton rate by department:", dept_attrition)

#STEP 10: Plot Attrition by Department
plt.figure(figsize=(8, 5))
dept_attrition.sort_values(ascending=False).plot(kind="bar")
plt.title("Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
import os
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/attrition_by_department.png")
plt.show()

#STEP 11: Attrition by Job Role

# Attrition by Job Role
jobrole_attrition = df.groupby("JobRole")["Attrition_flag"].mean() * 100

print("\nAttrition by Job Role:")
print(jobrole_attrition)

#STEP 12: Plot Attrition by Job Role
plt.figure(figsize=(12, 6))
jobrole_attrition.sort_values(ascending=False).plot(kind="bar")
plt.title("Attrition Rate by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#STEP 13: Attrition by Overtime (Very Important)
# Attrition by Overtime
overtime_attrition = df.groupby("OverTime")["Attrition_flag"].mean() * 100

print("\nAttrition by Overtime:")
print(overtime_attrition)

#STEP 14: Plot Overtime vs Attrition
plt.figure(figsize=(6, 4))
sns.barplot(x=overtime_attrition.index, y=overtime_attrition.values)
plt.title("Attrition Rate by Overtime")
plt.xlabel("OverTime")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()
import os
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/overtime_attrition.png")
plt.show()

#STEP 15: Attrition by Gender
# Attrition by Gender
gender_attrition = df.groupby("Gender")["Attrition_flag"].mean() * 100

print("\nAttrition by Gender:")
print(gender_attrition)

#STEP 16: Plot Gender vs Attrition
plt.figure(figsize=(6, 4))
sns.barplot(x=gender_attrition.index, y=gender_attrition.values)
plt.title("Attrition Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()
plt.show()

#STEP 17: Monthly Income vs Attrition
plt.figure(figsize=(8, 5))
sns.boxplot(x="Attrition", y="MonthlyIncome", data=df)
plt.title("Monthly Income vs Attrition")
plt.tight_layout()
plt.savefig("outputs/income_attrition.png")
plt.show()

# Age Distribution by Attrition
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", hue="Attrition", kde=True, bins=20)
plt.title("Age Distribution by Attrition")
plt.tight_layout()
plt.show()

# Years at Company vs Attrition
plt.figure(figsize=(8, 5))
sns.boxplot(x="Attrition", y="YearsAtCompany", data=df)
plt.title("Years at Company vs Attrition")
plt.tight_layout()
plt.show()

# Work-Life Balance vs Attrition
wlb_attrition = df.groupby("WorkLifeBalance")["Attrition_flag"].mean() * 100
print("\nAttrition by WorkLifeBalance:")
print(wlb_attrition)

plt.figure(figsize=(7, 4))
sns.barplot(x=wlb_attrition.index, y=wlb_attrition.values)
plt.title("Attrition Rate by Work-Life Balance")
plt.xlabel("WorkLifeBalance Score")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()
plt.show()

# Job Satisfaction vs Attrition
job_sat_attrition = df.groupby("JobSatisfaction")["Attrition_flag"].mean() * 100
print("\nAttrition by Job Satisfaction:")
print(job_sat_attrition)

plt.figure(figsize=(7, 4))
sns.barplot(x=job_sat_attrition.index, y=job_sat_attrition.values)
plt.title("Attrition Rate by Job Satisfaction")
plt.xlabel("JobSatisfaction Score")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()
plt.show()

# Marital Status vs Attrition
marital_attrition = df.groupby("MaritalStatus")["Attrition_flag"].mean() * 100
print("\nAttrition by Marital Status:")
print(marital_attrition.sort_values(ascending=False))

# Correlation Heatmap
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()

plt.figure(figsize=(14, 10))
sns.heatmap(corr, cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/heatmap.png")
plt.show()

# Top 5 High Attrition Roles
top_5_roles = jobrole_attrition.sort_values(ascending=False).head(5)
print("\nTop 5 Job Roles with Highest Attrition:")
print(top_5_roles)

# Save cleaned data
df.to_csv("outputs/cleaned_data.csv", index=False)
print("\nCleaned dataset saved successfully!")

