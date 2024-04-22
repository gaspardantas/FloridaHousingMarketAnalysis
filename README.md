# Florida Housing Market Analysis

## Table of Contents
1. [Overview](#overview)
2. [Objectives](#objectives)
3. [Data Source](#data-source)
4. [Tools](#tools)
5. [Exploratory Data Analysis (EDA)](#eda)
6. [Data Cleaning Preparation](#data-cleaning-preparation)
7. [Results and Findings](#results-and-findings)
8. [Recommendations](#recommendations)
9. [Limitations](#limitations)
10. [References](#references)

## Overview
The "Florida Housing Market Analysis" project aims to investigate the influence of mortgage rates on housing inventory and prices in the state of Florida. By analyzing datasets obtained from the Federal Reserve Economic Data (FRED), including Florida Median Listing Price, US Mortgage Average, and Housing Inventory in Florida, the project seeks to uncover insights into the dynamics of the Florida housing market.

## Objectives
The objectives of the project are as follows:
- **Trend Analysis**: Understand trends and patterns in Florida's housing market over time.
- **Relationship Exploration**: Explore the relationship between mortgage rates, housing inventory, and median listing prices in Florida.
- **Factor Identification**: Identify factors influencing fluctuations in housing inventory and prices in the state.
- **Recommendation Generation**: Provide recommendations for stakeholders based on analysis findings.

By achieving these objectives, the project aims to contribute to a better understanding of the dynamics driving the Florida housing market and provide valuable insights for decision-making in the real estate sector.

## Data Sources
The data sources include datasets obtained from the Federal Reserve Economic Data (FRED), including:
- **Florida Median Listing Price**: Information on the median listing price of homes in Florida from 2016 to present.
- **US Mortgage Average**: Data on average mortgage rates in the United States from 2016 to present.
- **Housing Inventory in Florida**: Information on the inventory of homes available for sale in Florida from 2016 to present.

These datasets are available in digital format and it was accessed through the FRED website, using  API (Application Programming Interface).

## Tools
The tools and technologies used in the project include:
- **Python**: Programming language for data manipulation, analysis, and visualization.
- **Microsoft Visual Studio Code (VS Code)**: Integrated development environment (IDE) for Python development.
- **Plotly**: Library for creating interactive visualizations.
- **Requests**: Library for interacting with the FRED API.
- **GitHub**: Version control and collaboration platform for storing project code and documentation.

By leveraging these tools and technologies, the project successfully conducted exploratory data analysis and created interactive visualizations to gain insights into the dynamics of the Florida housing market and the influence of mortgage rates on housing inventory and prices.

## Data Cleaning Preparation Before analysis, data cleaning steps are performed to ensure data integrity and consistency. This involves data retrieval, conversion to Pandas DataFrames, data cleaning, and organization.

- **Data Retrieval:** The first step involved retrieving the necessary datasets from the FRED API using Python's requests library. We fetched data for the Florida Median Listing Price, US Mortgage Average, and Housing Inventory in Florida for the period from 2016 to 2024.

- **Data Conversion:** Once the data was retrieved, we converted it into Pandas DataFrames for ease of manipulation and analysis. Each dataset was structured into a DataFrame with two columns: 'Date' and 'Value', representing the observation date and the corresponding data value, respectively.

- **Data Cleaning:** The next step was to clean the data to ensure its integrity and consistency. This involved several tasks:
Handling Missing Values: We checked each dataset for missing values using the .isnull().sum() method to identify any gaps in the data. Fortunately, there were no missing values in any of the datasets, simplifying the cleaning process.

- **Data Type Validation:** We verified the data types of each column in the DataFrames using the .dtypes attribute. This allowed us to confirm that the 'Date' column was in the datetime format and the 'Value' column contained numeric data, ensuring compatibility with subsequent analyses.

- **Data Organization:** Finally, we organized the cleaned datasets for further analysis. Each DataFrame was ready for exploratory data analysis (EDA) and statistical modeling, with the 'Date' column serving as the index for temporal analysis.

By completing these data cleaning and preparation steps, we ensured that the datasets were accurate, consistent, and ready for in-depth analysis. These efforts set the stage for uncovering insights into the dynamics of the Florida housing market and the relationship between mortgage rates, housing inventory, and median listing prices.

## Exploratory Data Analysis (EDA) Exploratory Data Analysis (EDA) is conducted to understand trends, patterns, and relationships within the datasets. This includes data loading, summary statistics, data visualization, and key findings.

- **Loading and Inspection of Datasets:** The first step involved loading the datasets obtained from the Federal Reserve Economic Data (FRED) into our analysis environment. Each dataset was loaded into a Pandas DataFrame, allowing for efficient manipulation and exploration. We inspected the structure of the datasets, including column names, data types, and missing values, to ensure data integrity and consistency.

- **Summary Statistics:** Summary statistics were computed for each dataset to gain insights into the central tendencies and distributions of the variables. Measures such as mean, median, standard deviation, minimum, and maximum values were calculated. Summary statistics provided a concise overview of the dataset characteristics and helped identify any outliers or anomalies that required further investigation.

- **Data Visualization:** Visualization played a pivotal role in uncovering patterns and trends within the datasets. Various plots, including time series plots, histograms, and scatter plots, were created to visualize the relationships between variables and identify potential trends over time. Visualization allowed for a comprehensive exploration of the data and facilitated the identification of significant insights.

- **Key Findings:** The EDA revealed several key findings regarding the Florida housing market and the influence of mortgage rates on housing inventory and median listing prices:

Temporal Trends - Time series analysis showed temporal trends in median listing prices, mortgage rates, and housing inventory levels over the study period. Fluctuations and potential seasonal patterns were observed, providing insights into the cyclical nature of the Florida housing market.

Insights and Implications - Overall, the EDA provided valuable insights into the Florida housing market's dynamics and the relationships between key variables. 

By understanding the patterns and trends within the data, we gained a deeper understanding of the factors driving changes in median listing prices, housing inventory levels, and mortgage rates. These insights laid the foundation for further analysis and informed decision-making for stakeholders in the real estate market.

## Results and Findings
The analysis uncovers insights into the relationship between mortgage rates, housing inventory, and median listing prices in Florida. Key findings include temporal trends, impacts of mortgage rates on housing inventory and prices, and seasonal patterns.

- **Relationship Between Mortgage Rates and Housing Inventory:** Our analysis revealed a significant direct relationship between mortgage rates and housing inventory levels in Florida. As mortgage rates decrease, we observe a corresponding decrease in housing inventory, indicating a loweer supply of homes available for sale. Conversely, when mortgage rates rise, housing inventory tends to increase as potential homebuyers face higher borrowing costs and may be less inclined to enter the market.

- **Impact of Mortgage Rates on Median Listing Prices:** We found that changes in mortgage rates have a noticeable impact on median listing prices in Florida. When mortgage rates are low, we observe an uptick in median listing prices, as lower borrowing costs make homeownership more affordable and stimulate demand for homes. Conversely, when mortgage rates rise, median listing prices tend to stabilize or decline, reflecting reduced demand and affordability constraints for potential homebuyers.  Additionally, we noted a significant impact on median listing prices in Florida during periods of low housing inventory, particularly when mortgage rates are declining. The scarcity of available homes intensifies competition among buyers, leading to heightened demand and upward pressure on prices. This highlights the interplay between housing inventory levels and mortgage rates, emphasizing the importance of considering both factors in understanding fluctuations in median listing prices.

- **Seasonal Patterns and Market Dynamics:** Our analysis also uncovered seasonal patterns and market dynamics that influence the relationship between mortgage rates, housing inventory, and prices in Florida. For example, we observed higher housing inventory levels during certain times of the year, such as the spring and summer months, coinciding with peak homebuying seasons. Additionally, fluctuations in economic conditions, employment trends, and demographic factors may further impact the dynamics of the Florida housing market.

- **Implications for Stakeholders:** These findings have important implications for various stakeholders in the Florida real estate market, including homebuyers, sellers, real estate agents, and policymakers. Understanding the relationship between mortgage rates and housing market dynamics can inform strategic decision-making and help stakeholders navigate market conditions effectively. For example, homebuyers may benefit from monitoring mortgage rate trends to capitalize on opportunities for favorable pricing and financing options, while sellers may adjust listing strategies based on market conditions and demand trends.

## Recommendations
Based on the findings, recommendations are provided for stakeholders including homebuyers, sellers, real estate agents, and policymakers. Recommendations focus on monitoring mortgage rate trends, adjusting listing strategies, and policy interventions to support housing affordability.

- **Homebuyers:** Stay informed about mortgage rate trends and explore financing options to capitalize on favorable interest rates.
- **Sellers:** Monitor market conditions and adjust listing strategies, such as pricing and marketing efforts, to align with demand trends and maximize sale potential.
- **Real Estate Agents:** Provide valuable insights and guidance to clients based on market analysis and trends, helping them make informed decisions in the buying and selling process.
- **Policymakers:** Consider policy interventions and initiatives to support housing affordability and market stability, such as incentives for first-time homebuyers and measures to promote sustainable homeownership.
- **Future Research Directions:** While our analysis provides valuable insights into the relationship between mortgage rates and housing market dynamics in Florida, there are several avenues for future research. Further analysis could explore additional factors influencing housing demand and supply, such as demographic trends, economic indicators, and local market conditions. Additionally, longitudinal studies and predictive modeling techniques may help forecast future trends and anticipate shifts in the Florida housing market.

By leveraging these findings and recommendations, stakeholders can make informed decisions and navigate the Florida real estate market with confidence, contributing to sustainable growth and prosperity in the housing sector.

## Limitations

The project has several limitations including data limitations, scope limitations, methodological limitations, and external factors. Acknowledging these limitations is essential for interpreting the results accurately.

- **Data Limitations:** The analysis relies on data obtained from the Federal Reserve Economic Data (FRED), which may have limitations such as data gaps, revisions, or inaccuracies.
The datasets used in this analysis have specific timeframes and may not capture longer-term trends or cyclical patterns in the Florida housing market.

- **Scope Limitations:** The analysis focuses on the influence of mortgage rates on housing inventory and prices in Florida and may not generalize to other states or regions with different market dynamics.
Other factors influencing the housing market, such as economic conditions, demographics, and policy changes, are not explicitly considered in this analysis but may have significant impacts on housing trends.

- **Methodological Limitations:** The analysis employs statistical techniques, such as regression analysis or correlation, to assess relationships between variables. However, correlation does not imply causation, and other unobserved factors may confound the results.
Assumptions underlying the statistical models, such as linearity and normality, may not hold true in all cases, leading to potential biases or inaccuracies in the findings.

- **Data Preprocessing Limitations:** Data preprocessing steps, such as cleaning, imputation, or outlier detection, are crucial for ensuring the quality and reliability of the analysis. However, the effectiveness of these steps may be limited by the availability and completeness of the data.
Missing data or inconsistencies in the datasets may introduce biases or errors in the analysis, despite efforts to address them through preprocessing techniques.

- **External Factors:** External factors, such as changes in regulatory policies, economic shocks, or natural disasters, may influence housing market dynamics independently of mortgage rates. These factors are not explicitly accounted for in the analysis but may impact the interpretation of the results.

- **Model Assumptions:** The analysis assumes that the relationship between mortgage rates, housing inventory, and prices is linear and stationary over time. However, underlying market dynamics may be more complex and non-linear, requiring more sophisticated modeling approaches.

- **Interpretation Bias:** The interpretation of the results is subject to bias and subjective judgment, as different stakeholders may have varying perspectives on the significance and implications of the findings.

- **Generalization:** The findings of this analysis may not apply universally to all segments of the housing market, such as luxury properties, rental markets, or specific geographic areas within Florida.

Acknowledging these limitations is essential for providing a balanced and nuanced understanding of the analysis and its implications. Additionally, it can guide future research efforts and help refine the methodology for more robust findings.

## References
References to the datasets used in the analysis obtained from the Federal Reserve Economic Data (FRED).
- Realtor.com, Housing Inventory: Median Listing Price in Florida [MEDLISPRIFL], retrieved from FRED, Federal Reserve Bank of St. Louis; [Link](https://fred.stlouisfed.org/series/MEDLISPRIFL)
- Realtor.com, Housing Inventory: Active Listing Count in Florida [ACTLISCOUFL], retrieved from FRED, Federal Reserve Bank of St. Louis; [Link](https://fred.stlouisfed.org/series/ACTLISCOUFL)
- Freddie Mac, 30-Year Fixed Rate Mortgage Average in the United States [MORTGAGE30US], retrieved from FRED, Federal Reserve Bank of St. Louis; [Link](https://fred.stlouisfed.org/series/MORTGAGE30US)

