# 🧑‍💼 HR Analytics Dashboard – Absenteeism Data

**Project Type:** SQL + Power BI
**Objective:** Analyze employee absenteeism data to generate insights on health, compensation, and behavior patterns using SQL and Power BI.

---

## 📁 Datasets Used

* `Absenteeism_at_work.csv`
* `compensation.csv`
* `Reasons.csv`

These files were imported into **Microsoft SQL Server** for data preparation and later connected to **Power BI** for dashboard visualization.

---

## 🛠️ SQL Operations & Logic

### 🔗 Table Joins

We connected all relevant tables using LEFT JOINs:

```sql
SELECT * 
FROM Absenteeism_at_work a
LEFT JOIN compensation b ON a.ID = b.ID
LEFT JOIN Reasons r ON a.Reason_for_absence = r.number;
```

---

### 🧠 Business Logic: Healthiest Employee Bonus

To find the most eligible employee for a health-based bonus:

```sql
SELECT * 
FROM Absenteeism_at_work 
WHERE Social_drinker = 0 AND Social_smoker = 0
AND Body_mass_index < 25
AND Absenteeism_time_in_hours < (
  SELECT AVG(Absenteeism_time_in_hours) 
  FROM Absenteeism_at_work
);
```

---

### 💰 Budgeting Logic: Non-Smoker Bonus Plan

Calculate eligible non-smokers for a compensation increase based on budget:

```sql
SELECT COUNT(*) AS nonsmoker 
FROM Absenteeism_at_work 
WHERE Social_smoker = 0;
```

> 📝 Budget Assumptions:
>
> * Total budget = \$983,221
> * \$0.68/hour ≈ \$1,414.4/year/employee

---

### ⚡ Optimized Query with CASE Statements & Derived Metrics

This query enhances readability and generates categorized fields like BMI category and Season of absence:

```sql
SELECT 
  a.ID,
  r.Reason,
  Month_of_absence,
  Body_mass_index,
  
  CASE 
    WHEN Body_mass_index < 18.5 THEN 'Underweight'
    WHEN Body_mass_index BETWEEN 18.5 AND 25 THEN 'Healthy'
    WHEN Body_mass_index BETWEEN 25 AND 30 THEN 'Overweight'
    WHEN Body_mass_index > 30 THEN 'Obese'
    ELSE 'Unknown'
  END AS BMI_Category,

  CASE 
    WHEN Month_of_absence IN (12, 1, 2) THEN 'Winter'
    WHEN Month_of_absence IN (3, 4, 5) THEN 'Spring'
    WHEN Month_of_absence IN (6, 7, 8) THEN 'Summer'
    WHEN Month_of_absence IN (9, 10, 11) THEN 'Fall'
    ELSE 'Unknown'
  END AS Season_Names,

  Day_of_the_week,
  Transportation_expense,
  Education,
  Son,
  Social_drinker,
  Social_smoker,
  Pet,
  Disciplinary_failure,
  Age,
  Work_load_Average_day,
  Absenteeism_time_in_hours

FROM Absenteeism_at_work a
LEFT JOIN compensation b ON a.ID = b.ID
LEFT JOIN Reasons r ON a.Reason_for_absence = r.number;
```

---

## 📊 Power BI Dashboard

* **Connected directly to SQL Server**
* Built wireframe and final layout
* Visualized KPIs like average absenteeism, high-risk groups, and seasonal trends
* Used slicers and filters for dynamic analysis
* Final report provides actionable insights for HR & Compensation teams

---

## 📌 Key Skills Demonstrated

* SQL Joins & Filters
* CASE Statements & Conditional Logic
* Query Optimization
* Data Modeling
* Power BI Visualization
* Real-world business scenario analysis

---

## 💡 Outcome

This project provided hands-on experience in **data analysis, visualization**, and **HR-related decision making**. It shows how SQL + Power BI can work together to solve business problems efficiently.

---

Let me know if you’d like a matching LinkedIn post summary or a logo/banner for your GitHub project!
