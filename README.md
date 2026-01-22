# Retail-sale 

**The Retail-sale** project is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualisation. The tool supports multiple data formats and provides an intuitive interface for both novice and expert data scientists.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
* The dataset consists of retail sales data from a major retailer, including three main CSV files:

- Sales data (421,570 records): Contains weekly sales figures, store and department identifiers, dates, and holiday indicators.
- Store data (45 records): Includes store types (A, B, C) and sizes.
- Features data (8,190 records): Contains external factors like temperature, fuel prices, promotional markdowns (5 types), CPI, unemployment rates, and holiday flags.

* The combined dataset after merging has approximately 421,570 rows with 17 columns. The data spans multiple years and covers 45 stores across different types and sizes. The total size is reasonable (under 100MB) and fits within repository limits.


## Business Requirements
* The business requirements focus on retail analytics to support strategic decision-making:

- Identify and analyze sales trends over time to understand seasonal patterns and growth.
- Evaluate the impact of promotional markdowns on sales performance.
- Compare sales performance during holiday periods versus non-holiday periods.
- Analyze store-level performance variations by type and size.
- Understand correlations between external factors (temperature, fuel prices, unemployment) and sales.


## Hypothesis and how to validate?
* Hypothesis 1: Promotional markdowns significantly increase weekly sales.

Validation: Compare average sales during weeks with markdowns vs. weeks without, using statistical tests (t-test) and correlation analysis between Total_MarkDown and Weekly_Sales.

* Hypothesis 2: Holiday periods result in higher sales compared to non-holiday periods.

Validation: Use box plots and statistical comparisons of sales distributions for holiday vs. non-holiday weeks, calculating percentage differences.

* Hypothesis 3: Store type and size influence sales performance.

Validation: Group sales by store type and size, use bar charts and ANOVA tests to identify significant differences.

* Hypothesis 4: External factors like temperature and unemployment correlate with sales.

Validation: Create correlation heatmaps and scatter plots with regression lines to quantify relationships. 

## Project Plan
* High-level steps:

Data Collection: Gather raw CSV files (sales, stores, features).
ETL Process: Extract data, merge datasets, clean missing values, engineer features (Total_MarkDown), load cleaned data.
Exploratory Data Analysis: Generate descriptive statistics and initial visualizations.
Advanced Analysis: Create correlation analysis and comparative visualizations.
Insights and Reporting: Document findings and create interactive dashboards.

* Data management: Raw data stored is in raw-data folder, processed through ETL pipeline in the notebook, cleaned data is saved to cleaned_sales_data.csv. All transformations documented in code cells for reproducibility.

* Research methodologies: Exploratory data analysis (EDA) using descriptive statistics, correlation analysis, and visualization techniques. Quantitative approach with statistical comparisons rather than qualitative methods, chosen for its objectivity in analyzing numerical sales data.

## The rationale to map the business requirements to the Data Visualisations
* Sales trends over time (Requirement 1): Line plots show temporal patterns, enabling identification of seasonal trends and growth.

* Promotional markdown impact (Requirement 2): Scatter plots with regression lines and correlation heatmaps quantify markdown-sales relationships.

* Holiday vs non-holiday comparison (Requirement 3): Box plots and bar charts highlight performance differences between periods.

* Store performance variations (Requirement 4): Bar charts by store type/size provide comparative insights.

* External factor correlations (Requirement 5): Heatmaps and scatter plots reveal relationships between variables like temperature and sales.

Interactive Plotly visualizations were chosen for stakeholder exploration, while static Matplotlib/Seaborn plots ensure reproducibility in reports.

## Analysis techniques used
* Data analysis methods: Descriptive statistics (means, correlations), data visualization (line plots, bar charts, scatter plots, box plots, heatmaps), feature engineering (Total_MarkDown aggregation).

Limitations: Correlation doesn't imply causation; large dataset requires sampling for some plots to maintain performance. Alternative approaches could include time series forecasting models or machine learning regression for predictive insights.


* Structured as: ETL → Basic visualizations → Advanced statistical visualizations → Interactive dashboards. This logical flow ensures data quality before analysis and builds complexity gradually.

* Large dataset (421K+ rows) caused performance issues with full scatter plots, addressed by random sampling (5K-10K points). No missing data issues after cleaning, but markdown columns had many NAs filled with zeros.

* Generative AI (GitHub Copilot) assisted in:
- Ideation: Generating initial code structures for ETL pipelines and visualization templates.
- Design thinking: Suggesting appropriate plot types and color schemes for different data relationships.
- Code optimization: Refactoring repetitive visualization code into functions and improving pandas operations for efficiency.
Without AI assistance, the project would have required more manual research for visualization best practices and debugging common pandas errors.


## Ethical considerations
* The dataset contains aggregated retail sales data without personally identifiable information, so no significant data privacy concerns exist. However, potential bias issues include regional representation (data primarily from US stores) and temporal bias (limited to certain years). Fairness considerations involve ensuring analyses don't disadvantage certain store types or regions.
* Legal and societal issues were addressed by using publicly available retail data and ensuring compliance with data usage terms. Societal issues like economic inequality were acknowledged but not directly addressed, as the focus was on sales analytics rather than social impact.

## Dashboard Design
* The project uses a Jupyter Notebook as the primary interactive "dashboard" with multiple sections:
  - **ETL Section**: Code cells for data loading, merging, and cleaning with output displays.
  - **Matplotlib Section**: Static plots including line charts for sales trends, bar charts for store types, and scatter plots for temperature vs sales.
  - **Seaborn Section**: Enhanced static visualizations with regression lines, box plots for holiday analysis, and correlation heatmaps.
  - **Plotly Section**: Interactive widgets including hover-enabled scatter plots, dynamic bar charts, box plots, histograms, and interactive heatmaps.
* No major revisions were needed, as the initial plan aligned with the data insights. Interactive Plotly charts were added later for better stakeholder engagement.
* Data insights are communicated through visual storytelling: technical audiences see code and statistical outputs, while non-technical users interact with intuitive plots and hover tooltips.
* The dashboard uses progressive complexity - static plots for reports, interactive elements for exploration. Color coding (e.g., red for holidays) and clear labels ensure accessibility. Technical users can view code cells, while executives focus on key visualizations with explanatory markdown.

## Unfixed Bugs
* The Jupyter Notebook cells remain unexecuted, which could be considered a "bug" as it prevents immediate verification of results. This is due to the template nature of the notebook - it's designed as a reproducible script rather than a live session.
* Framework shortcomings: Plotly interactive plots may not render in all environments without proper kernel setup; Matplotlib static plots are reliable but less engaging.
* Gaps in knowledge were recognized in advanced statistical testing (e.g., ANOVA for store type comparisons) and addressed through documentation research and simplified approaches using correlation and visualization.
* No peer or instructor feedback was received during development, but self-review identified the need for more robust error handling in ETL processes.

## Development Roadmap
* Challenges included handling large datasets (421K+ rows) causing memory and performance issues in visualizations, overcome by implementing random sampling and optimizing pandas operations.
* Data merging complexities with multiple keys were addressed by careful validation and step-by-step debugging.
* Strategies: Used GitHub Copilot for code suggestions, modularized code into sections, and tested incrementally.
* Next skills/tools: Advanced time series analysis (ARIMA models), machine learning for sales prediction (scikit-learn pipelines), and cloud deployment (AWS/Docker) for scalable dashboards.

## Deployment
### Heroku

* The App live link is: https://retail-sales-analysis.herokuapp.com/ (placeholder - actual deployment pending app.py creation)
* Set the runtime.txt Python version to a Heroku-20 stack currently supported version (e.g., python-3.9.17).
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis Libraries
* **pandas**: Used for data manipulation and ETL operations, e.g., `pd.merge()` to combine sales, stores, and features datasets.
* **numpy**: Provided numerical operations and array handling, e.g., `np.nan` for missing value detection.
* **matplotlib**: Created static visualizations, e.g., `plt.plot()` for sales trend lines.
* **seaborn**: Enhanced statistical plots, e.g., `sns.heatmap()` for correlation matrices.
* **plotly**: Built interactive dashboards, e.g., `px.scatter()` with hover data for exploratory analysis.
* **scikit-learn**: Planned for future ML models, currently used for basic data preprocessing.

## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- Dataset sourced from public retail sales data (similar to Walmart Kaggle dataset).
- ETL and visualization patterns inspired by pandas documentation and Matplotlib/Seaborn tutorials.
- Deployment instructions adapted from Heroku official documentation.

### Media

- No external media used; all visualizations generated from data.



## Acknowledgements (optional)
* Special thanks to Vasi, Mark who provided support through this project.