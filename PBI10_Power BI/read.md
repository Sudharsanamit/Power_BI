# Power BI 10-Year Tech Adoption Dashboard - Project Report

## 📄 Project Title:

**"10 Years of Technology Adoption - A Global Insight Dashboard"**

## 🔍 Project Description:

This Power BI project was created as part of the #PBI10 Dataviz Contest to celebrate Power BI's 10th anniversary. The goal was to explore and visualize a decade's worth of technology adoption trends globally using clean, standardized data. We merged key datasets into a single model and developed a compelling, accessible, and story-driven dashboard that highlights insights on internet usage, mobile cellular subscriptions, and fixed landline decline over the past ten years.

## 🌐 Data Sources:

All data was sourced from **Our World in Data**, including:

* Internet Users (per 100 people)
* Mobile Cellular Subscriptions (per 100 people)
* Fixed Landline Subscriptions (per 100 people)
* Population by Country and Year

Country Code Mapping was sourced from GitHub (lukes/ISO-3166).

## 📚 Final Dataset:

A cleaned and merged dataset named `cleaned_tech_adoption.csv` was created. It includes the following columns:

* Country
* Year
* InternetUsersPer100
* MobileUsersPer100
* LandlineUsersPer100
* Population

## ⚙️ Tools Used:

* **Power BI Desktop** (latest version)
* **Power Query (M)** for data transformation
* **DAX** for calculated measures
* **Python** (optional script to merge CSVs into one file)

---

## 💡 Dashboard Structure:

The dashboard is designed as a **single-page scrollable report** with four structured sections:

### ✏️ Section 1: Header + Overview

* Title: "10 Years of Tech Adoption"
* Date/Filters: Slicers for Year and Country
* A brief intro text to give context

### 📊 Section 2: KPI Highlights

* Four KPI Cards:

  * Average Internet Users per 100
  * Average Mobile Users per 100
  * Average Landline Users per 100
  * Global Internet Growth %
* These cards provide quick, insightful trends

### 🌐 Section 3: Trend Visuals

* Line Chart: To show trend over time for Internet, Mobile, and Landline usage.

  * **Use Case:** Ideal for showing continuous trends across multiple years and categories.
* Stacked Bar Chart: To compare values across countries for a specific year.

  * **Use Case:** Helps in country-level comparison for a selected year.
* Map Visual: Colored map of countries based on Internet usage per 100 in 2023.

  * **Use Case:** Excellent for showing geographic distribution of tech adoption.
* Column + Line Combo Chart: Mobile Users (columns) and Internet Users (line) on one axis.

  * **Use Case:** Useful for comparative trend visualization using dual axes.

### 🔢 Section 4: Interpretation & Narrative

* Smart Narrative Visual: Auto-generated text to summarize trends.

  * **Use Case:** Provides immediate summary insights to make data more digestible.
* Bullet Points: Manually crafted text insights on technology changes.
* Donut Chart: Share of usage type (Internet, Mobile, Landline) in 2023.

  * **Use Case:** To visually present proportion-based summaries.

---

## 🔄 Data Preparation Process:

1. **Download all 4 CSVs** and ISO mapping.
2. **Merge them using Python** into a unified `cleaned_tech_adoption.csv`.
3. Load the final file into Power BI.
4. Perform final cleaning and transformation using Power Query.

---

## ⚖️ DAX Measures Used (Step-by-Step):

### 1. Average Internet Users per 100

```DAX
Average Internet Users per 100 = 
    AVERAGE(cleaned_tech_adoption[InternetUsersPer100])
```

### 2. Average Mobile Users per 100

```DAX
Average Mobile Users per 100 = 
    AVERAGE(cleaned_tech_adoption[MobileUsersPer100])
```

### 3. Average Landline Users per 100

```DAX
Average Landline Users per 100 = 
    AVERAGE(cleaned_tech_adoption[LandlineUsersPer100])
```

### 4. Internet Growth % Over the Decade

```DAX
Internet Growth (%) = 
VAR Initial = 
    CALCULATE([Average Internet Users per 100], 
        FILTER(cleaned_tech_adoption, cleaned_tech_adoption[Year] = MIN(cleaned_tech_adoption[Year])))
VAR Final = 
    CALCULATE([Average Internet Users per 100], 
        FILTER(cleaned_tech_adoption, cleaned_tech_adoption[Year] = MAX(cleaned_tech_adoption[Year])))
RETURN
    DIVIDE(Final - Initial, Initial) * 100
```

### 5. Internet Users in 2023

```DAX
Avg Internet 2023 = 
    CALCULATE([Average Internet Users per 100], cleaned_tech_adoption[Year] = 2023)
```

---

## 🌟 Accessibility & Design Features

* **Tab order** arranged for keyboard navigation
* **Smart Narrative** used for automated insights
* **White space** used as active design element
* **Consistent layout** with a clear visual grid
* **Color contrast** verified using Adobe Accessibility Tools
* **Alt Text** added to all visuals

---
