# Hackathon-March-2021
#### RMDS 2021 Data Science Competition - Impact of News Sentiment on the Stock Market

<img src="./assets/images/UnfinishedProject.jpg" alt="Ongoing Project" style="height: 310px; width:660px;"/>

[External Resources](#acknowledgements_and_contact)

<a id='back_to_top'></a>

# Ongoing Project: Work-in-Progress
---
### Problem Statement:
> "This data science competition seeks to create an innovative solution to analyze the effects of news sentiment and biases on daily stock performance for top companies in the oil and gas industry. News Sentiments and biases have a significant impact on stock prices and consumer behavior. Contestants will be provided with the necessary news data, stock market data, macro data and company financial data." - [*RMDS Competition Website*](https://grmds.org/competition/news-sentiment)

#### **Exploration of the following specific questions:**
* What is the best model we can create to predict closing stock prices based on prior data?
* What significance does News Sentiment have in that model?

---
### Table of Contents

* [EDA & Data Cleaning](#eda_and_cleaning)
    * [Data Dictionary](#appendix)
* [Preprocessing & Feature Engineering](#preprocessing_and_feature_engineering)
* [Model Benchmarks](#model_benchmarks)
* [Model Tuning](#model_tuning)
* [Production Model & Insights](#production_model_and_insights)
* [Recommendations and Next Steps](#recommendations_and_next_steps)
* [Software Requirements](#software_requirements)
* [Acknowledgements and Contacts](#acknowledgements_and_contact)

<a id='eda_and_cleaning'></a>

---
## EDA & Data Cleaning

### Datasets

* [Data Dictionary](#appendix)

#### Training Datasets:

* [`file_name.csv`](./filepath.csv): Description ([source](http://URL.com) | [data dictionary](http://URL.com))

#### Validation Datasets:

* [`file_name.csv`](./filepath.csv): Description ([source](http://URL.com) | [data dictionary](http://URL.com))


**Notes about the data:**

#### Data Cleaning & EDA
- Missing Values:
- Imputation Methods:
- Management of Outliers:

[Back to Top](#back_to_top)

<a id='preprocessing_and_feature_engineering'></a>


---
## Pre-Processing and Feature Engineering
[Back to Top](#back_to_top)

<a id='model_benchmarks'></a>

---
## Model Benchmarks and Preparation
[Back to Top](#back_to_top)

<a id='model_tuning'></a>

---
## Model Tuning & Assessment
[Back to Top](#back_to_top)

<a id='production_model_and_insights'></a>

---
## Production Model & Insights
[Back to Top](#back_to_top)

<a id='recommendations_and_next_steps'></a>

---
## Recommendations and Next Steps
[Back to Top](#back_to_top)

<a id='software_requirements'></a>

---
## Software Requirements
[Back to Top](#back_to_top)

<a id='acknowledgements_and_contact'></a>

---
## Acknowledgements and Contacts:
[Back to Top](#back_to_top)

### External Resources:

#### Official Competition Resources:
> * [`2021 Data Science Competition Overview`] (GRMDS Online): ([*source*](https://grmds.org/competition/news-sentiment))
> * [`Dataset Overview`] (WorldData.AI): ([*source*](https://worlddata.ai/bucket/WorldDataTeam/Competition_RMDS_WorldData))

#### Other Related Information:
> * [`Which Countries Use the Most Fossil Fuels?`] (Resource Watch): ([*source*](https://blog.resourcewatch.org/2019/05/02/which-countries-use-the-most-fossil-fuels/))
> * [`2020 Russia–Saudi Arabia Oil Price War`] (Wiki): ([*source*](https://en.wikipedia.org/wiki/2020_Russia%E2%80%93Saudi_Arabia_oil_price_war))
> * [`MobilityScore: an Improvement over TransitScore?`] (Blog: Human Transit): ([*source*](https://humantransit.org/2018/01/mobilityscore-an-improvement-over-transitscore.html))
> * [`Media Bias Fact Check`] (MBFC News): ([*source*](https://mediabiasfactcheck.com/2021/03/03/the-latest-fact-checks-curated-by-media-bias-fact-check-3-3-2021/))
> * [`JODI-Oil Data Downloads`] (JODI): ([*source*](https://www.jodidata.org/oil/database/data-downloads.aspx))
> * [`Stock Trading Strategy & Education: Open Interest`] (Investopedia): ([*source*](https://www.investopedia.com/terms/o/openinterest.asp))
> * [`West Texas Intermediate (WTI)`] (Investopedia): ([*source*](https://www.investopedia.com/terms/w/wti.asp))
> * [`Is the Stock Market Closed Today (Dec 5, 2018)? Why?`] (Heavy): ([*source*](https://heavy.com/news/2018/12/stock-market-closed-national-day-of-mourning/))

* [`Title`] (Platform): ([*source*](https://www.URL.com))

### Papers:
* `Valero Energy Corporation Case Study` (Journal of Advanced Research in Social Sciences and Humanities): ([*source*](https://jarssh.com/papers/volume5-issue1/JARSSH-05-2020-0105.pdf))

* `Title` (Journal/Blog): ([*source*](https://www.URL.com))

### Team Contacts:
##### Main Contributors
> * Brandon [GitHub](https://github.com/griffinbran) | [LinkedIn](https://www.linkedin.com/in/griffinbran/)
> * Will [GitHub](https://github.com/griffinwt) | [LinkedIn](https://www.linkedin.com/in/griffinwt)
##### Associates
> * Nader [GitHub](https://github.com/laternader) | [LinkedIn](https://www.linkedin.com/in/ncesmael)
> * Cloudy [GitHub](https://github.com/cloudmcloudyo) | [LinkedIn](https://www.linkedin.com/in/cloudyliu)
> * James [GitHub](https://github.com) | [LinkedIn](https://www.linkedin.com/in/jamessalisbury)
> * Cristina [GitHub](https://github.com/CristinaSahoo) | [LinkedIn](https://www.linkedin.com/in/cristinasahoo)

<a id='appendix'></a>

---
## Appendix: Data Dictionary

[Back to Top](#back_to_top)

|Indicator|Data Type|Dataset|Region-Frequency|Description|
|---|---|---|---|---|
|**Brent Crude Oil**|*float*|Commodity Prices|Daily|Price, in USD per barrel, of North Sea Brent crude oil as traded on the Intercontinental Exchange(ICE).|
|**WTI Crude Oil**|*float*|Commodity Prices|Daily|Price, in USD per barrel, of West Texas Intermediate(WTI) crude oil, the underlying commodity of the NYMSEX. It is the main oil benchmark for North America.|
|**Settlement Price**|*float*|Commodity & Exchange|Daily|Price of final transaction on a futures exchange for a given "trading" day.|
|**Open Interest**|*int*|Commodity & Exchange|Daily|Number of outstanding contracts(positions held) in the derivatives market. Open interest is an indicator of liquidity as each futures contract is for 100 shares.|
|**Grocery & Pharmacy**|*float*|Google Mobility|U.S. Daily|Mobility trends for places like grocery markets, food warehouses, farmers markets, specialty food shops, drug stores, and pharmacies.|
|**Parks**|*float*|Google Mobility|U.S. Daily|Mobility trends for places like local parks, national parks, public beaches, marinas, dog parks, plazas, and public gardens.|
|**Transit Stations**|*float*|Google Mobility|U.S. Daily|Mobility trends for places like public transport hubs such as subway, bus, and train stations.|
|**Retail & Recreation**|*float*|Google Mobility|U.S. Daily|Mobility trends for places like restaurants, cafes, shopping centers, theme parks, museums, libraries, and movie theaters.|
|**Residential**|*float*|Google Mobility|U.S. Daily|Mobility trends for places of residence.|
|**Workplaces**|*float*|Google Mobility|U.S. Daily|Mobility trends for places of work.|
|**Value_(country)\_walk**|*float*|Apple Mobility|Various Nations Daily|Change from baseline (100) in requests for walking directions in given country; ger=Germany, ind = India, rus=Russia, us=USA, jap=Japan|
|**Value_(country)\_drive**|*float*|Apple Mobility|Various Nations Daily|Change from baseline (100) in requests for driving directions in given country; ger=Germany, ind = India, rus=Russia, us=USA, jap=Japan|
|**Value_(country)\_trans**|*float*|Apple Mobility|Various Nations Daily|Change from baseline (100) in requests for transit routing in given country (not available for Russia or India); ger=Germany, us=USA, jap=Japan|
|**d\_f\_(keyword)**|*float*|News Sentiment Score|Worldwide Daily|Daily News Sentiment score from Financial News sources related to Direct keywords: chevron, drilling, exxon, fossil_fuel, marathon_oil, occidental_petroleum, oil, oilfield, phillips_66, pipeline, valero|
|**d\_g\_(keyword)**|*float*|News Sentiment Score|Worldwide Daily|Daily News Sentiment score from Global News sources related to Direct keywords: chevron, drilling, exxon, fossil_fuel, oil, oilfield, pipeline, valero|
|**i\_f\_(keyword)**|*float*|News Sentiment Score|Worldwide Daily|Daily News Sentiment score from Financial News sources related to Indirect keywords: airline, carbon_footprint, emissions, epa, greenhouse, hurricane_storm, pollution, sanction, solar, turbine, vacation|    
|**i\_g\_(keyword)**|*float*|News Sentiment Score|Worldwide Daily|Daily News Sentiment score from Global News sources related to Indirect keywords: airline, carbon_footprint, emissions, epa, greenhouse, hurricane_storm, pollution, sanction, solar, turbine, vacation|
 |**Value_(company)**|*float*|Closing Price|NYSE Daily|Daily close price for given company, used as target (y value) for modeling - companies: phillips_66, bp_plc, valero_energy_corporation, chevron_corporation, occidental_petroleum_corporation, marathon_oil_corporation, pioneer_natural_resources_company, conocophillips, exxon_mobil_corporation, marathon_petroleum_corporation|
|**dow_jones_transportation_average**|*float*|Stock Market Index|U.S. Daily|"The Dow Jones Transportation Average (DJTA, also called the "Dow Jones Transports") is a U.S. stock market index from S&P Dow Jones Indices of the transportation sector, and is the most widely recognized gauge of the American transportation sector."[Wikipedia](https://en.wikipedia.org/wiki/Dow_Jones_Transportation_Average)|
|**dow_jones_composite_average**|*float*|Stock Market Index|U.S. Daily|"The Dow Jones Composite Average is a stock index from Dow Jones Indexes that tracks 65 prominent companies. The average's components include every stock from the Dow Jones Industrial Average (30 components), the Dow Jones Transportation Average (20), and the Dow Jones Utility Average (15)."[Wikipedia](https://en.wikipedia.org/wiki/Dow_Jones_Composite_Average)|
|**dow_jones_industrial_average**|*float*|Stock Market Index|U.S. Daily|"The Dow Jones Industrial Average (DJIA), Dow Jones, or simply the Dow (/ˈdaʊ/), is a stock market index that measures the stock performance of 30 large companies listed on stock exchanges in the United States."[Wikipedia](https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average)|
|**dow_jones_utility_average**|*float*|Stock Market Index|U.S. Daily|"The Dow Jones Utility Average (DJUA, also known as the "Dow Jones Utilities") is a stock index from S&P Dow Jones Indices that tracks the performance of 15 prominent utility companies traded in the United States"[Wikipedia](https://en.wikipedia.org/wiki/Dow_Jones_Utility_Average)|
|**s&p_500**|*float*|Stock Market Index|U.S. Daily|"The S&P 500, or simply the S&P, is a stock market index that measures the stock performance of 500 large companies listed on stock exchanges in the United States. It is one of the most commonly followed equity indices."[Wikipedia](https://en.wikipedia.org/wiki/S%26P_500)|


[Back to Top](#back_to_top)

---