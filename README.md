# FloridaHousingMortgageAnalysis

### 1. Table of Contents

1. Table of Contents
2. Overview
3. Objectives
4. Data Source
5. Exploratory Data Analysis (EDA)
6. Results and Findings
7. Recommendations
Future Research Directions
References

### 2. Overview

The "Florida Housing Market Analysis" project aims to investigate the influence of mortgage rates on housing inventory and prices in the state of Florida. By analyzing datasets obtained from the Federal Reserve Economic Data (FRED), including Florida Median Listing Price, US Mortgage Average, and Housing Inventory in Florida, the project seeks to uncover insights into the dynamics of the Florida housing market.

The main objectives of the project are:

To understand the trends and patterns in Florida's housing market over time.
To explore the relationship between mortgage rates, housing inventory, and median listing prices in Florida.
To identify factors influencing fluctuations in housing inventory and prices in the state.
To provide recommendations for stakeholders based on the findings of the analysis.
The analysis will involve conducting exploratory data analysis (EDA) to visualize and summarize the datasets, followed by regression analysis or other statistical techniques to assess the impact of mortgage rates on housing inventory and prices. The project aims to contribute to a better understanding of the factors driving changes in Florida's housing market and to provide actionable insights for homebuyers, real estate agents, policymakers, and other stakeholders.

The project is expected to shed light on key trends and dynamics in the Florida housing market and provide valuable insights for decision-making in the real estate sector.

### 3. Objectives

The objectives of the Florida Housing Market Analysis project are as follows:

1. Trend Analysis: Understand trends and patterns in Florida's housing market over time. This involves analyzing historical data to identify long-term trends, seasonal variations, and cycles in housing inventory and prices.

2. Relationship Exploration: Explore the relationship between mortgage rates, housing inventory, and median listing prices in Florida. This includes examining how changes in mortgage rates impact housing affordability, demand, and supply dynamics.

3. Factor Identification: Identify factors influencing fluctuations in housing inventory and prices in the state. This involves identifying external factors such as economic conditions, demographic trends, and policy changes that may affect the housing market.

4. Recommendation Generation: Provide recommendations for stakeholders based on analysis findings. This includes offering actionable insights for homebuyers, sellers, real estate agents, and policymakers to navigate the Florida housing market effectively.

By achieving these objectives, the project aims to contribute to a better understanding of the dynamics driving the Florida housing market and provide valuable insights for decision-making in the real estate sector.

### 4. Data Source

The data sources include datasets obtained from the Federal Reserve Economic Data (FRED). These datasets include:

Florida Median Listing Price: This dataset contains information on the median listing price of homes in Florida from 2016 to present. It provides insights into the pricing trends and fluctuations in the Florida housing market.
US Mortgage Average: This dataset consists of data on average mortgage rates in the United States, from 2016 to present. It helps to understand how changes in mortgage rates impact housing affordability and demand.
Housing Inventory in Florida: This dataset includes information on the inventory of homes available for sale in Florida from 2016 to present. It tracks the number of homes listed for sale and provides insights into the supply side of the Florida housing market.
These datasets are available in digital format and it was accessed through the FRED website, using  API (Application Programming Interface).

### 5 Tools

1. Python: Python was utilized as the primary programming language for data manipulation, analysis, and visualization. Libraries such as Pandas, Plotly, and Requests were employed for data handling, visualization, and API interaction, respectively.

2. Microsoft Visual Studio Code (VS Code): VS Code served as the integrated development environment (IDE) for Python development. It provided features such as syntax highlighting, code completion, and debugging capabilities.

3. Plotly: Plotly was used for creating interactive visualizations, including line charts, bar charts, and area charts, to explore and analyze the datasets obtained from the Federal Reserve Economic Data (FRED) API.

4. Requests: The Requests library was used to interact with the FRED API and fetch datasets related to Florida Median Listing Price, US Mortgage Average, and Housing Inventory in Florida. This allowed for seamless data retrieval from the FRED platform.

5. GitHub: GitHub served as the version control and collaboration platform for the project, providing a centralized repository for storing project code and documentation. It facilitated collaboration among team members and ensured version control throughout the project development process.

By leveraging these tools and technologies, the project successfully conducted exploratory data analysis and created interactive visualizations to gain insights into the dynamics of the Florida housing market and the influence of mortgage rates on housing inventory and prices.

### 6. Exploratory Data Analysis

Before diving into the analysis, it's crucial to prepare the data by cleaning and organizing it appropriately. In this section, we'll outline the steps taken to clean and prepare the datasets obtained from the Federal Reserve Economic Data (FRED) API.

1. Data Retrieval:
The first step involved retrieving the necessary datasets from the FRED API using Python's requests library. We fetched data for the Florida Median Listing Price, US Mortgage Average, and Housing Inventory in Florida for the period from 2016 to 2024.

2. Data Conversion:
Once the data was retrieved, we converted it into Pandas DataFrames for ease of manipulation and analysis. Each dataset was structured into a DataFrame with two columns: 'Date' and 'Value', representing the observation date and the corresponding data value, respectively.

3. Data Cleaning:
The next step was to clean the data to ensure its integrity and consistency. This involved several tasks:
Handling Missing Values: We checked each dataset for missing values using the .isnull().sum() method to identify any gaps in the data. Fortunately, there were no missing values in any of the datasets, simplifying the cleaning process.

4. Data Type Validation: We verified the data types of each column in the DataFrames using the .dtypes attribute. This allowed us to confirm that the 'Date' column was in the datetime format and the 'Value' column contained numeric data, ensuring compatibility with subsequent analyses.

4. Data Organization:
Finally, we organized the cleaned datasets for further analysis. Each DataFrame was ready for exploratory data analysis (EDA) and statistical modeling, with the 'Date' column serving as the index for temporal analysis.

By completing these data cleaning and preparation steps, we ensured that the datasets were accurate, consistent, and ready for in-depth analysis. These efforts set the stage for uncovering insights into the dynamics of the Florida housing market and the relationship between mortgage rates, housing inventory, and median listing prices.

### 5. Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) is a crucial step in understanding the dynamics of the Florida housing market and investigating the relationships between mortgage rates, housing inventory, and median listing prices. In this section, we outline the key components of the EDA conducted on the Florida Median Listing Price, US Mortgage Average, and Housing Inventory in Florida datasets.

1. Loading and Inspection of Datasets:
The first step involved loading the datasets obtained from the Federal Reserve Economic Data (FRED) into our analysis environment. Each dataset was loaded into a Pandas DataFrame, allowing for efficient manipulation and exploration. We inspected the structure of the datasets, including column names, data types, and missing values, to ensure data integrity and consistency.

2. Summary Statistics:
Summary statistics were computed for each dataset to gain insights into the central tendencies and distributions of the variables. Measures such as mean, median, standard deviation, minimum, and maximum values were calculated. Summary statistics provided a concise overview of the dataset characteristics and helped identify any outliers or anomalies that required further investigation.

3. Data Visualization:
Visualization played a pivotal role in uncovering patterns and trends within the datasets. Various plots, including time series plots, histograms, and scatter plots, were created to visualize the relationships between variables and identify potential trends over time. Visualization allowed for a comprehensive exploration of the data and facilitated the identification of significant insights.

4. Key Findings:
The EDA revealed several key findings regarding the Florida housing market and the influence of mortgage rates on housing inventory and median listing prices:

a. Temporal Trends: Time series analysis showed temporal trends in median listing prices, mortgage rates, and housing inventory levels over the study period. Fluctuations and potential seasonal patterns were observed, providing insights into the cyclical nature of the Florida housing market.

b. Correlation Analysis: Scatter plots and correlation matrices were utilized to explore the relationships between mortgage rates, housing inventory, and median listing prices. Strong correlations were observed between mortgage rates and housing inventory levels, as well as between housing inventory and median listing prices. These findings indicated the interconnected nature of the variables and their influence on market dynamics.

c. Distribution Characteristics: Histograms and distribution plots revealed the distributional characteristics of the variables, such as skewness and kurtosis. Understanding the distributions of the variables was essential for assessing their normality and identifying potential outliers or anomalies that could impact the analysis.

5. Insights and Implications:
Overall, the EDA provided valuable insights into the Florida housing market's dynamics and the relationships between key variables. By understanding the patterns and trends within the data, we gained a deeper understanding of the factors driving changes in median listing prices, housing inventory levels, and mortgage rates. These insights laid the foundation for further analysis and informed decision-making for stakeholders in the real estate market.

### 6. Results and Findings 

After conducting exploratory data analysis and statistical modeling, we have uncovered several key findings regarding the influence of mortgage rates on housing inventory and prices in Florida.

1. Relationship Between Mortgage Rates and Housing Inventory:
Our analysis revealed a significant direct relationship between mortgage rates and housing inventory levels in Florida. As mortgage rates decrease, we observe a corresponding decrease in housing inventory, indicating a loweer supply of homes available for sale. Conversely, when mortgage rates rise, housing inventory tends to increase as potential homebuyers face higher borrowing costs and may be less inclined to enter the market.

2. Impact of Mortgage Rates on Median Listing Prices:
We found that changes in mortgage rates have a noticeable impact on median listing prices in Florida. When mortgage rates are low, we observe an uptick in median listing prices, as lower borrowing costs make homeownership more affordable and stimulate demand for homes. Conversely, when mortgage rates rise, median listing prices tend to stabilize or decline, reflecting reduced demand and affordability constraints for potential homebuyers.  Additionally, we noted a significant impact on median listing prices in Florida during periods of low housing inventory, particularly when mortgage rates are declining. The scarcity of available homes intensifies competition among buyers, leading to heightened demand and upward pressure on prices. This highlights the interplay between housing inventory levels and mortgage rates, emphasizing the importance of considering both factors in understanding fluctuations in median listing prices.

3. Seasonal Patterns and Market Dynamics:
Our analysis also uncovered seasonal patterns and market dynamics that influence the relationship between mortgage rates, housing inventory, and prices in Florida. For example, we observed higher housing inventory levels during certain times of the year, such as the spring and summer months, coinciding with peak homebuying seasons. Additionally, fluctuations in economic conditions, employment trends, and demographic factors may further impact the dynamics of the Florida housing market.

4. Implications for Stakeholders:
These findings have important implications for various stakeholders in the Florida real estate market, including homebuyers, sellers, real estate agents, and policymakers. Understanding the relationship between mortgage rates and housing market dynamics can inform strategic decision-making and help stakeholders navigate market conditions effectively. For example, homebuyers may benefit from monitoring mortgage rate trends to capitalize on opportunities for favorable pricing and financing options, while sellers may adjust listing strategies based on market conditions and demand trends.

### 7. Recommendations:
Based on our findings, we offer the following recommendations for stakeholders:

Homebuyers: Stay informed about mortgage rate trends and explore financing options to capitalize on favorable interest rates.
Sellers: Monitor market conditions and adjust listing strategies, such as pricing and marketing efforts, to align with demand trends and maximize sale potential.
Real Estate Agents: Provide valuable insights and guidance to clients based on market analysis and trends, helping them make informed decisions in the buying and selling process.
Policymakers: Consider policy interventions and initiatives to support housing affordability and market stability, such as incentives for first-time homebuyers and measures to promote sustainable homeownership.
6. Future Research Directions:
While our analysis provides valuable insights into the relationship between mortgage rates and housing market dynamics in Florida, there are several avenues for future research. Further analysis could explore additional factors influencing housing demand and supply, such as demographic trends, economic indicators, and local market conditions. Additionally, longitudinal studies and predictive modeling techniques may help forecast future trends and anticipate shifts in the Florida housing market.

By leveraging these findings and recommendations, stakeholders can make informed decisions and navigate the Florida real estate market with confidence, contributing to sustainable growth and prosperity in the housing sector.

### 8. 

### 9. References

References to the datasets used in the analysis obtained from the Federal Reserve Economic Data (FRED):

Realtor.com, Housing Inventory: Median Listing Price in Florida [MEDLISPRIFL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/MEDLISPRIFL, April 21, 2024.
Realtor.com, Housing Inventory: Active Listing Count in Florida [ACTLISCOUFL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/ACTLISCOUFL, April 21, 2024.
Freddie Mac, 30-Year Fixed Rate Mortgage Average in the United States [MORTGAGE30US], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/MORTGAGE30US, April 21, 2024.
