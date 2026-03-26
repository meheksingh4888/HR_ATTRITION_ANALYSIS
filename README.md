# HR Employee Attrition Analysis

## 📌 Project Overview
This project analyzes employee attrition data to understand the key factors that lead employees to leave a company.  
The analysis is performed using **Python**, **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.

The goal of this project is to:
- Identify patterns behind employee attrition
- Analyze attrition across departments, job roles, overtime, salary, and satisfaction levels
- Generate business insights for HR teams
- Recommend strategies to improve employee retention

---

## 🎯 Problem Statement
Employee attrition is a major challenge for organizations because it impacts:
- Productivity
- Hiring costs
- Training costs
- Team stability
- Overall business performance

This project helps answer important HR questions such as:
- Which employees are more likely to leave?
- Does overtime increase attrition?
- Does salary affect employee retention?
- Which departments or job roles have the highest attrition?
- How do work-life balance and job satisfaction impact attrition?

---

## 📂 Dataset Information
The dataset used in this project is based on **IBM HR Employee Attrition data**.

### Important Columns Used:
- `Age`
- `Attrition`
- `BusinessTravel`
- `Department`
- `DistanceFromHome`
- `Education`
- `EducationField`
- `EnvironmentSatisfaction`
- `Gender`
- `JobRole`
- `JobSatisfaction`
- `MaritalStatus`
- `MonthlyIncome`
- `OverTime`
- `PercentSalaryHike`
- `PerformanceRating`
- `RelationshipSatisfaction`
- `StockOptionLevel`
- `TotalWorkingYears`
- `WorkLifeBalance`
- `YearsAtCompany`
- `YearsInCurrentRole`
- `YearsSinceLastPromotion`
- `YearsWithCurrManager`

---

## 🛠️ Tools & Technologies Used
- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook**

---

## 📁 Project Structure

```bash
hr_attrition_analysis/
│
├── data/
│   └── HR_Employee_Attrition.csv
│
├── notebooks/
│   └── hr_attrition_analysis.ipynb
│
├── outputs/
│   ├── cleaned_data.csv
│   ├── attrition_by_department.png
│   ├── overtime_attrition.png
│   ├── income_attrition.png
│   └── heatmap.png
│
└── README.md

1. Data Collection
Loaded the HR employee attrition dataset from CSV file
2. Data Understanding
Checked dataset shape
Reviewed column names
Inspected data types and null values
3. Data Cleaning
Removed duplicate records
Verified missing values
Created a new numeric column:
Attrition_Flag
Yes = 1, No = 0
4. Exploratory Data Analysis (EDA)

Performed analysis on:

Overall attrition rate
Attrition by department
Attrition by job role
Attrition by overtime
Attrition by gender
Monthly income vs attrition
Age distribution by attrition
Years at company vs attrition
Work-life balance vs attrition
Job satisfaction vs attrition
Marital status vs attrition
5. Visualization

Created charts such as:

Bar charts
Boxplots
Histograms
Correlation heatmap
6. Business Insights

Generated HR-focused recommendations to reduce attrition and improve employee retention.

✅ KPI Metrics
Total Employees
Employees Left
Employees Stayed
Attrition Rate
Average Monthly Income
✅ Department Analysis
Compared attrition rates across different departments
✅ Job Role Analysis
Identified top job roles with the highest attrition
✅ Overtime Analysis
Measured how overtime impacts attrition
✅ Salary Analysis
Compared monthly income of employees who stayed vs employees who left
✅ Satisfaction Analysis
Evaluated impact of:
Work-life balance
Job satisfaction
Environment satisfaction
✅ Correlation Analysis
Built a heatmap to understand relationships between numeric variables
📈 Sample Insights

Some common insights observed from this analysis include:

Employees working overtime tend to have higher attrition
Employees with lower monthly income are more likely to leave
Certain departments and job roles show higher attrition rates
Lower job satisfaction is associated with increased attrition
Poor work-life balance can contribute to employee turnover
Employees with fewer years at company may leave more frequently

Note: Final insights may vary slightly depending on the dataset version used.

💻 Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/hr-employee-attrition-analysis.git
2. Move into the project folder
cd hr-employee-attrition-analysis
3. Install required libraries
pip install pandas numpy matplotlib seaborn
4. Run Jupyter Notebook
jupyter notebook

Open:

notebooks/hr_attrition_analysis.ipynb
▶️ How to Run the Project
Place the dataset file inside the data/ folder:
data/HR_Employee_Attrition.csv
Open the notebook:
notebooks/hr_attrition_analysis.ipynb
Run all cells step by step
Check generated outputs inside:
outputs/
📷 Output Visualizations

This project generates visualizations such as:

Attrition Rate by Department
Attrition Rate by Job Role
Attrition Rate by Overtime
Monthly Income vs Attrition
Age Distribution by Attrition
Work-Life Balance vs Attrition
Job Satisfaction vs Attrition
Correlation Heatmap
🧠 Business Recommendations

Based on the analysis, HR teams can consider:

Reducing excessive overtime for employees
Improving compensation strategies for lower-income roles
Monitoring high-risk departments and job roles
Increasing employee engagement and job satisfaction initiatives
Strengthening work-life balance policies
Improving retention plans for early-tenure employees
📌 Future Improvements

This project can be extended further by adding:

Power BI Dashboard
Tableau Dashboard
Machine Learning model to predict attrition
Interactive web dashboard using Streamlit
Advanced statistical analysis
🏆 Skills Demonstrated

This project demonstrates the following skills:

Data Cleaning
Exploratory Data Analysis (EDA)
Data Visualization
Business Insight Generation
HR Analytics
Python Programming
Problem Solving
📜 Conclusion

This project provides a complete analysis of employee attrition and highlights the major factors influencing employee turnover.
It helps HR teams understand workforce behavior and supports data-driven decision-making for improving employee retention.