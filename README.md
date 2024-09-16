![DALL·E 2024-08-28 19 16 36 - A highly detailed and realistic 4K night scene of multiple apartment buildings in the middle of Daegu city, South Korea, with a more dynamic and inter](https://github.com/user-attachments/assets/60787de4-ceab-4ac5-8004-99a191e60d05)

Technical Report -> [Click here!](https://drive.google.com/file/d/1Igmrd8jGm2Z8SkKirR6eb8KYMXOxEvD2/view?usp=sharing)

Presentation Slide -> [Click here!](https://drive.google.com/file/d/1j4QiDPA6clwdY2vJ4D1XBzQhUyyRFGBv/view?usp=sharing)

# Project Background
Daegu, a major metropolitan city in South Korea with a population of around 2.5 million in 2022, is experiencing rising demand for housing due to its growth as an industrial hub. The limited residential land in metropolitan areas, often converted into business zones, presents a challenge for housing development. Apartments, which require less land, are a practical solution, and their demand is expected to increase. This presents a business opportunity for XYZ Company, a property firm specializing in buying and selling apartments in Korea. The company currently relies on third-party services for price checks during purchases, while its internal division manages pricing for apartment sales.

Problem:
- The apartment price survey process is considered inefficient by the company, as it requires additional costs for hiring survey services, which can reduce profit margins when selling the purchased apartments.
- The determination of apartment prices sometimes results in apartments being underpriced or overpriced. Overpriced listings can lead to unsold apartments due to uncompetitive market prices, while underpriced listings result in suboptimal profits.

Objective:
Based on the problems outlined above, the company needs a model that can estimate apartment prices, eliminating the need for third-party services. Additionally, the model should assist the company in determining appropriate sale prices for apartments, avoiding underpricing or overpricing.

Therefore, an analysis of apartment data is required, focusing on prices and apartment characteristics that may influence pricing. The next step involves building a machine learning model to predict apartment prices. This model is expected to help the company in both comparing the prices of apartments to be purchased and setting the selling prices of apartments.

# Data Overview
The dataset includes 4123 rows and 11  columns. Each row of the data represents an apartment unit.
The dataset contains the following variables:

| No  | Variable Name                       | Description                                       |
| --- | ----------------------------------- | ------------------------------------------------- |
| 1   | `HallwayType`                       | Type of apartment                                 |
| 2   | `TimeToSubway`                      | Time required to reach the nearest subway station |
| 3   | `SubwayStation`                     | Name of the nearest subway station                |
| 4   | `N_FacilitiesNearBy(ETC)`           | Number of nearby facilities                       |
| 5   | `N_FacilitiesNearBy(PublicOffice)`   | Number of nearby public facilities               |
| 6   | `N_SchoolNearBy(University)`        | Number of nearby universities                     |
| 7   | `N_Parkinglot(Basement)`            | Number of parking spaces                          |
| 8   | `YearBuilt`                         | Year the apartment was built                      |
| 9   | `N_FacilitiesInApt`                 | Number of facilities in the apartment             |
| 10  | `Size(sqf)`                         | Size of the apartment (in square feet)            |
| 11  | `SalePrice`                         | Apartment price (in Won)                          |

# Executive Summary

## Data Analysis
- Hallway Type: Terraced hallways command the highest median sale prices, reflecting buyer preference for design, privacy, or perceived quality, whereas corridor types are less valued.
- Proximity to Subway: Properties within a 0-5 minute walk to a subway station have the highest prices. However, properties with no nearby subway still retain more value than those 10-20 minutes away, suggesting the influence of other - amenities.
- Subway Station Impact: Properties near "Banwoldang" station have the highest median prices, while those near "Daegu" station have the lowest, indicating varying neighborhood desirability and available amenities.
- Year Built: Newer properties (built between 2003-2015) have higher median prices due to modern amenities and lower maintenance costs, while older properties (pre-1980) are less valued.

Market Price Competitiveness (MPC):

- 54.1% of properties are priced below the market average, indicating a competitive pricing strategy to attract price-sensitive buyers. The distribution is fairly balanced but leans slightly towards lower-priced properties.
- Terraced Hallway Types are most common, with a significant portion priced below the market average (33.4%), suggesting a budget-friendly positioning.
- Mixed Hallway Types are evenly distributed across both premium and budget categories.
- Corridor Hallway Types are least common and primarily positioned as more affordable options, with a higher percentage priced below the market average (6.5%).

Price per Facility:

- The distribution of Price Per Facility is right-skewed, with most apartments priced between 10,000 and 40,000, highlighting affordability. However, some apartments exceed 60,000, reaching up to 100,000, indicating premium listings that cater to niche markets.
- The wide range of median prices per facility, from 68,584 to 13,920, shows strong market segmentation by location.


## Data Modeling

The apartment price prediction model for Daegu uses an XGBRegressor wrapped in a TransformedTargetRegressor with carefully tuned parameters to optimize performance.

Model Performance Metrics:
- Mean Absolute Error (MAE): 31,572 won
- Mean Absolute Percentage Error (MAPE): 16.79%
- Mean Squared Logarithmic Error (MSLE): 0.0463
  
These metrics indicate a good model performance, with a MAPE of 16.7%, which falls within the acceptable range of 10-20% for reliable predictions.

Insights from Scatter Plot:
The scatter plot of predicted vs. actual values shows some bias, particularly for apartment prices above 500,000 won, where the model tends to underestimate values. Despite this, the overall regression pattern is clear and generally accurate.

Feature Importance Analysis:
The most influential features contributing to the model's performance include:
1. Hallway Type (terraced)
2. Number of Facilities in Apartment
3. Proximity to Subway Stations
4. Size of Apartment (sqf)
5. Year Built







