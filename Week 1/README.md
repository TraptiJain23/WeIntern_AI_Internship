# Week 1 Assignment

## Internship Week and Task Summary

The Week 1 internship assignment focused on student performance analysis using data analytics techniques.

The assignment was divided into three tasks:

### Task 1: Dataset Analysis and Data Cleaning

* Loaded and inspected the student performance dataset.
* Examined dataset structure, data types, and feature information.
* Identified and handled missing values.
* Removed duplicate records.
* Standardized inconsistent categorical values.
* Performed data quality checks and prepared a cleaned dataset for analysis.

### Task 2: Data Visualization and Exploratory Data Analysis

* Conducted exploratory data analysis (EDA).
* Created multiple visualizations to understand data distributions and relationships.
* Analyzed attendance patterns, study habits, demographic factors, and performance indicators.
* Generated insights using charts, plots, and correlation analysis.

### Task 3: Business Insight Report

* Converted technical findings into business-oriented insights.
* Identified key performance trends.
* Developed practical recommendations for educational stakeholders.
* Documented limitations and potential areas for future improvement.

---

## Dataset Used

**Student Performance Dataset**
Dataset File- [1_student_performance_raw_dataset.csv](./week1-task1-student-performance-analysis/data/1_student_performance_raw_dataset.csv)

The dataset contains information related to student demographics, academic activities, engagement indicators, lifestyle factors, and examination performance.

#### Dataset Features

| Column Name | Description |
|------------|------------|
| Student ID | Unique identifier for each student |
| Age | Age of the student |
| Gender | Student gender |
| Hours Studied | Average study hours |
| Attendance | Attendance percentage |
| Parental Involvement | Level of parental involvement |
| Access to Resources | Availability of learning resources |
| Extracurricular Activities | Participation in extracurricular activities |
| Sleep Hours | Average daily sleep duration |
| Previous Scores | Previous academic performance scores |
| Motivation Level | Student motivation level |
| Internet Access | Availability of internet access |
| Tutoring Sessions | Number of tutoring sessions attended |
| Family Income | Family income category |
| Teacher Quality | Perceived teacher quality |
| School Type | Type of school attended |
| Peer Influence | Influence of peer group |
| Physical Activity | Physical activity level |
| Learning Disabilities | Presence of learning disabilities |
| Parental Education Level | Education level of parents |
| Distance from Home | Distance between home and school |
| Final Exam Score | Final examination score (target variable) |

#### Dataset Purpose

The dataset was analyzed to identify factors that may influence student academic performance and to generate meaningful insights through data cleaning, visualization, and business reporting.

The dataset was used to explore factors that may influence student academic performance and learning outcomes.

---

## Libraries Used

The following Python libraries were used throughout the project:

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Development Environment

- Google Colab
- Python 3.x
- Git & GitHub

---

## Steps Performed

### Task 1: Dataset Analysis & Data Cleaning

1. Loaded the student performance dataset.
2. Examined dataset structure, dimensions, and data types.
3. Analyzed numerical and categorical features.
4. Identified missing values across columns.
5. Removed duplicate records.
6. Standardized inconsistent categorical values.
7. Verified data quality and consistency.
8. Saved the cleaned dataset for further analysis.

---

### Task 2: Data Visualization & Exploratory Data Analysis

1. Generated descriptive statistics for numerical features.
2. Explored the distribution of student performance scores.
3. Analyzed attendance patterns among students.
4. Examined study hour distributions.
5. Compared performance across gender categories.
6. Evaluated the impact of extracurricular activities.
7. Investigated the relationship between attendance and final exam scores.
8. Analyzed the relationship between study hours and performance.
9. Created a correlation heatmap to identify relationships among numerical variables.
10. Documented observations and insights from each visualization.

---

### Task 3: Business Insight Report

1. Reviewed findings from data cleaning and visualization tasks.
2. Identified key patterns and trends in student performance.
3. Converted technical observations into business-oriented insights.
4. Developed actionable recommendations for educational stakeholders.
5. Documented limitations of the analysis.
6. Prepared a professional business insight report summarizing the findings.
---

## Key Findings

* Student performance varies considerably across the dataset.
* Attendance alone does not strongly predict final examination performance.
* Study hours show only a limited relationship with academic outcomes.
* Gender-based performance differences are minimal.
* Participation in extracurricular activities does not negatively impact performance.
* Internet access alone does not guarantee better academic results.
* Most variables demonstrate weak correlations with final exam scores.
* Student success appears to be influenced by multiple interconnected factors rather than a single dominant variable.

---

## Folder Structure

```text
WelIntern_AI_Internship/
│
├── README.md
│
└── Week 1/
    │
    ├── README.md
    │
    ├── week1-task1-student-performance-analysis/
    │   ├── data/
    │   ├── notebook/
    │   └── screenshots/
    │
    ├── week1-task2-data-visualization/
    │   ├── data/
    │   ├── notebook/
    │   └── visuals/
    │
    └── week1-task3-business-insight-report/
        └── report/
```

---

## Execution Instructions

1. Clone or download the repository.
2. Open the notebooks using Google Colab or Jupyter Notebook.
3. Install required libraries if necessary.
4. Run the notebooks sequentially:

   * Task 1 → Data Cleaning
   * Task 2 → Data Visualization
   * Task 3 → Business Insight Report

5. Ensure that the dataset files are available in the appropriate **data** folders before running the notebooks.

6. Review generated outputs, visualizations, and findings.

6. Generated charts and outputs can be viewed in the corresponding **screenshots** and **visuals** folders.

7. Refer to the Task 3 report notebook for the final business insights and recommendations.

---
## Quick Access

### Project Notebooks

- [Task 1 – Dataset Analysis & Data Cleaning](./week1-task1-student-performance-analysis/notebook/week1_task1_dataset_analysis.ipynb)
- [Task 2 – Data Visualization & EDA](./week1-task2-data-visualization/notebook/week1_task2_data_visualization.ipynb)
- [Task 3 – Business Insight Report](./week1-task3-business-insight-report/week1_task3_business_insight_report.ipynb)
Quick links to the primary project notebooks and important outputs.

## Screenshots / Preview Images
### Featured Previews

- [Dataset Preview](./week1-task1-student-performance-analysis/screenshots/dataset-preview.png)
- [Correlation Heatmap](./week1-task2-data-visualization/visuals/visualization_8_correlation_heatmap.png)

Additional screenshots and visualizations are available in:

- `week1-task1-student-performance-analysis/screenshots/`
- `week1-task2-data-visualization/visuals/`

---

## Author Details

**Name:** Trapti Jain

**Internship Week:** Week 1

**Project:** Student Performance Analysis

---

## Conclusion

This project demonstrates the complete data analytics workflow, including data cleaning, exploratory analysis, visualization, and business reporting. The findings provide useful insights into student performance patterns and highlight the importance of using multiple indicators when evaluating academic success.
