#standard imports
import streamlit as st
import pandas as pd
#REMINDER - to preview in local browser: strealit run file_name.py (in bash)

#custom imports
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error

from matplotlib.backends.backend_agg import RendererAgg #https://docs.streamlit.io/en/stable/deploy_streamlit_app.html?highlight=matplotlib%20lock#limitations-and-known-issues
_lock = RendererAgg.lock

st.set_page_config(
    page_icon=':fuelpump:',
    initial_sidebar_state='auto'
)

st.title('"Putting Stock" in Sentiment')
st.subheader('An Examination of the Relationship Between Closing Stock Prices and Daily News Stories')

page = st.sidebar.selectbox(
    'Select-A-Page',
    ('Overview', 'Financial Trends', 'Mobility Data', 'News Sentiment', 'Modeling', 'Create A Model', 'Data Dictionary', 'About The Team')
)

#functions

def plot_preds(ytraindf, ytestdf, pred_df, title='Title', xlab=None, ylab=None):
    with _lock:
        fig, ax = plt.subplots(figsize=(35,23))
        for col in ytraindf.columns:
            ax.plot(ytraindf[col], linewidth=3) #plot each ytrain
        for col in ytestdf.columns:
            ax.plot(ytestdf[col], color='black', linewidth=2) #plot each ytest
        for col in pred_df.columns:
            ax.plot(pred_df[col], color='magenta', linewidth=2) #plot the preds
        ax.set_title(title, fontsize=35)
        ax.set_xlabel(xlab, fontsize=28)
        ax.set_ylabel(ylab, fontsize=28)
        ax.tick_params(axis='x', labelsize=22)
        ax.tick_params(axis='y', labelsize=22)
        ax.legend(pred_df.columns, fontsize=22)
        return st.pyplot(fig)

def model(a_list):
    included = [] #list to put included features into
    for n in range(len(a_list)): #list of feature checkboxes
        if a_list[n]: #if box is checked (boolean)
            included.append(selectafeat[n]) # create list of included features
    if len(included) == 0:
        return "Please choose at least one feature to include"
    else:
        col_selected = ['date'] #empty list to put columns that will be read in into
        col_selected += targets #add target columns
        col_selected += lagged_targets #add lagged target columns
        for inc in included:
            col_selected += selection[inc] #add lists of features that should be included
        mod = pd.read_csv('app_dataset.csv', usecols = col_selected) #read in with selected columns only
        mod.set_index(pd.to_datetime(mod['date']), inplace=True)
        mod.drop(columns='date', inplace=True)
        mod.sort_index(inplace=True)
        pred_list = {}
        train_list = {}
        test_list = {}
        scores = {}
        #coefs = {}
        for target in targets:
            X_train, X_test, y_train, y_test = train_test_split(mod.drop(columns=targets), #drop all target columns
                                                           mod[target], #target is selected as y
                                                           test_size=.2, #80%/20% train/test split
                                                           shuffle=False) #predict most recent values
            X_train = sm.add_constant(X_train)
            X_test = sm.add_constant(X_test) #add intercepts
            lm = sm.OLS(y_train, X_train)
            lm_results = lm.fit()
            preds = lm_results.predict(X_test)
            train_list[target] = y_train #update dictionary with y_train
            test_list[target] = y_test #update dictionary with y_test
            pred_list[target] = preds #update dictionary with preds
            #coefs[target] = lm_results.params #update dictionary with coefficient values
            scores[target] = mean_squared_error(y_test, lm_results.predict(X_test))**.5 #update dictionary with RMSE score
        
        final_preds = pd.DataFrame(pred_list) #turn dictionary of lists into dataframe
        training = pd.DataFrame(train_list) #turn dictionary of lists into dataframe
        testing = pd.DataFrame(test_list) #turn dictionary of lists into dataframe

        plot_preds(training, testing, final_preds, title='Predicting Daily Closing Price - Energy Stocks',
                   xlab='Year-Month', ylab='USD($)')
        #plt.legend(final_preds.columns, fontsize=18)
        #st.write(plt.show())
        #return st.write('RMSE for each target:', scores)
        return pd.DataFrame(scores, index=('RMSE',)).T

#lists
targets = ['Value_PHILLIPS 66', 'Value_BP P.L.C.',
       'Value_VALERO ENERGY CORPORATION', 'Value_CHEVRON CORPORATION',
       'Value_OCCIDENTAL PETROLEUM CORPORATION',
       'Value_MARATHON OIL CORPORATION',
       'Value_PIONEER NATURAL RESOURCES COMPANY', 'Value_CONOCOPHILLIPS',
       'Value_EXXON MOBIL CORPORATION', 'Value_MARATHON PETROLEUM CORPORATION']

lagged_targets = ['lag_Value_PHILLIPS 66', #target value from the previous day
       'lag_Value_BP P.L.C.', 'lag_Value_VALERO ENERGY CORPORATION',
       'lag_Value_CHEVRON CORPORATION',
       'lag_Value_OCCIDENTAL PETROLEUM CORPORATION',
       'lag_Value_MARATHON OIL CORPORATION',
       'lag_Value_PIONEER NATURAL RESOURCES COMPANY',
       'lag_Value_CONOCOPHILLIPS', 'lag_Value_EXXON MOBIL CORPORATION',
       'lag_Value_MARATHON PETROLEUM CORPORATION']

direct_g = ['lag_d_g_chevron', 'lag_d_g_drilling', 'lag_d_g_exxon',
       'lag_d_g_fossil_fuel', 'lag_d_g_oil', 'lag_d_g_oilfield',
       'lag_d_g_pipeline', 'lag_d_g_valero']


direct_f = ['lag_d_f_chevron',
       'lag_d_f_drilling', 'lag_d_f_exxon', 'lag_d_f_fossil_fuel',
       'lag_d_f_marathon_oil', 'lag_d_f_occidental_petroleum', 'lag_d_f_oil',
       'lag_d_f_oilfield', 'lag_d_f_phillips_66', 'lag_d_f_valero']

indirect_g = ['lag_i_g_airline', 'lag_i_g_carbon_footprint', 'lag_i_g_emissions',
       'lag_i_g_epa', 'lag_i_g_greenhouse', 'lag_i_g_hurricane_storm',
       'lag_i_g_pollution', 'lag_i_g_sanction', 'lag_i_g_solar',
       'lag_i_g_turbine', 'lag_i_g_vacation']

indirect_f = ['lag_i_f_airline',
       'lag_i_f_carbon_footprint', 'lag_i_f_emissions', 'lag_i_f_epa',
       'lag_i_f_greenhouse', 'lag_i_f_pollution', 'lag_i_f_sanction',
       'lag_i_f_solar', 'lag_i_f_turbine', 'lag_i_f_vacation']

financial = ['lag_futures_settle',
       'lag_crude_usd_per_barrel', 'futures_prev_day_open_interest']

selection = {
    'direct_g':direct_g,
    'direct_f':direct_f,
    'indirect_g':direct_g,
    'indirect_f':indirect_f,
    'financial':financial
}  #dictionary to lookup combinations of features
    
if page == 'Overview':
    st.subheader('Overview')
    st.write('''

This is an interactive application to display models and visualizations related to the RMDS / WorldData.ai Data Science competition "Impact of News Sentiment on the Stock Market".

(From the competition homepage) *This data science competition seeks to create an innovative solution to analyze the effects of news sentiment and biases on daily stock performance for top companies in the oil and gas industry.*  [Competition Link](https://grmds.org/competition/news-sentiment)

''')
    st.subheader('Use the drop-down menu on the left to discover more about the data, our approach and an interactive model-building widget to try out for yourself!')

    st.image('./images/oilrig.jpg', use_column_width=True)
    st.write('Photo by [Clyde Thomas](https://unsplash.com/@clydeo)')

elif page =='Financial Trends':
    st.subheader('Financial Trends')

    st.image('./images/all_closing_wout_mobility.png', use_column_width=True)
    st.write('''
    This graph shows four years of NYSE closing prices (2017-2021) for each of our ten target companies. The volatility is obvious, especially in the past year as the pandemic triggered a huge dip in March 2020. Interestingly, some companies appear to suffer from higher volatility than others. Here's a second visualization of the same data:    
    ''')

    st.image('./images/boxplot_price_distro_wout_legend.png', use_column_width=True)

    st.write('''
    We see that Marathon Oil ("MRO") in the center has a low price but also stays very close to its median value over time, neither rising nor falling to any great degree. In contrast, Pioneer Natural Resource Company (PXD) takes on a vast range of closing prices, suggesting it can make or break the risk-loving investor. BP and Chevron (CVX) appear to hold the highest median value but also suffer some peaks and valleys over time.
    ''')

elif page =='Mobility Data':
    st.write('**Apple**')
    st.image('./images/apple_weekly.png', use_column_width=True)
    st.write('This is a graph of the Apple mobility data - it was recorded in daily increments but for this graph it has been resampled at a weekly rate to provide a clearer trend picture. The countries whose scores were analyzed (USA, India, Russia, Japan, Germany) correspond to the top fossil fuel using countries with the exception of China for which no scores were available. The countries scores are further broken down into the categories of driving, walking, and transit, however there were no transit scores in the data for Russia and India. This led to a total of 13 Apple mobility features (USA:3, India:2, Russia:2, Japan:3, Germany:3). While this line graph undertakes a vaguely similar shape to the stock prices over the same time period, it did not prove to be particularly helpful with modeling and in fact brought down RMSE on the OLS model. Even more significantly, this dataset begins in early 2020, giving us little more than a year (~240 rows of business days) to analyze if we wanted to include it as a feature. Without it, we were able to include about four times as many rows using closing prices, sentiment, and indexes going back to early 2017.')

    st.write('**Google**')
    st.image('./images/google_mobility.png')
    st.write('The Google mobility data is measured in percent change from baseline (defined as the first day records began) and divided into 6 categories - Workplaces, Retail and Recreation, Grocery and Pharmacy, Residential, Transit Stations, and Parks. The data the visualization above is specficially related to US Google map queries. As time progresses, we see that most mobility is on a downward trend in the early part of 2020 except for Residential which spike significantly, no doubt due to most people solely traveling in a residential context during various closures early in the pandemic. We see a suspicious spike in Retail and Grocery during early July, likely due to the Independence Day holiday. Similar spikes are evident towards the tail of the graph, likely representing Thanksgiving and Christmas. As we might intuitively expect, Residential travel spikes at those times, as does Grocery and Pharmacy, followed by substaial drop-offs as people stay at home with all the food they cooked themselves for the holidays! Unfortunately the Google data suffered much the same fate as the Apple data in that it was not particularly useful in modeling and also restricted us to using a single year of data in order to include it, so it did not last in the latest iterations of our models.') 

elif page =='News Sentiment':
    st.subheader('News Sentiment')
    st.image('./images/news.jpg', use_column_width=True)  
    st.write('Photo by [AbsolutVision](https://unsplash.com/@freegraphictoday)')

    st.write('''
    WorldData.ai provides an impressive array of news archives and sentiment scoring. Every article is analyzed through Natural Language Processing on a scale of -1 to 1 where anything above zero would be generally positive and anything below zero has a negative tilt. The scores we used were calculated by WorldData.ai so we (fortunately) did not have to classify tens of thousands of articles ourselves! Two things we DID have control over were news source and keyword selection.
    
    With regards to sources, we investigated both Global and Financial news. Examples of Global news would be "The Guardian", "CNN", "Nigerian Tribune", "Toronto Star", or "Newsweek". In contrast, Financial sources included outlets like "Reuters", "The Wall Street Journal", and "Economic Times". These sources had little to no overlap based on our results, giving us confidence that we were not victims of redundant research. We searched all of our keywords across both types of sources, including all features that returned at least 100 related articles.
    
    For keyword selection, we created the distinction of "Direct" and "Indirect" to differentiate our terms. Direct keywords had a parallel and often synonymous relationship with the target variables, including words like "oil", "pipeline", "drilling", as well as several target companies like "Exxon", "Valero, and "Chevron". Indirect keywords, however, had a varied range of relationships to our target closing prices. These were words like "Solar", "Greenhouse", "Emissions", "Airline", "Vacation", and "Sanctions". Some of the Direct keywords did not return enough results from the Global news sources to be included (i.e., "Marathon Oil"), but all of the indirect keywords found enough traction among both types of sources to be included as features in our model.
    ''')

elif page =='Modeling':
    st.subheader('Modeling')
    st.write('**OLS**')
    st.write('The first model we developed was an ordinary least squares regression using the statsmodels package in Python. We used the NYSE closing prices as the base of the dataframe and then (left) joined all other features by matching dates. The mobility data, while thought provoking, only exists for roughly the past year, so it was disregarded in favor of a broader (4 year) look.')

    st.image('./images/wout_mobility_preds_1.png', use_column_width=True)

    st.write('The measure of error (RMSE) was very good, indicating that the 10 close price predictions were within $0.65 to $4.47 of true values on average, as we might expect based on the consistent overlap between the black lines (test data) and purple lines (predicted close prices) in the image above. More importantly, however, a closer examination of the coefficients reveals which features were most critical to our predictions.')

    st.markdown('''
|                                            |   Feature_count |
|:-------------------------------------------|----------------:|
| lag_d_f_oil                                |               8 |
| lag_d_f_marathon_oil                       |               7 |
| lag_d_f_phillips_66                        |               5 |
| const                                      |               5 |
| lag_i_f_carbon_footprint                   |               4 |
| lag_d_f_valero                             |               3 |
| lag_d_f_occidental_petroleum               |               3 |
| lag_d_f_fossil_fuel                        |               3 |
| lag_Value_CONOCOPHILLIPS                   |               1 |
| lag_Value_EXXON MOBIL CORPORATION          |               1 |
| lag_Value_OCCIDENTAL PETROLEUM CORPORATION |               1 |
| lag_i_g_hurricane_storm                    |               1 |
| lag_i_g_greenhouse                         |               1 |
| lag_Value_PHILLIPS 66                      |               1 |
| lag_d_f_chevron                            |               1 |
| lag_Value_BP P.L.C.                        |               1 |
| lag_d_g_oil                                |               1 |
| lag_i_f_solar                              |               1 |
| lag_Value_MARATHON OIL CORPORATION         |               1 |
| lag_Value_MARATHON PETROLEUM CORPORATION   |               1 |
    
    ''')
    st.write('')
    st.write('''
    
    This is an aggregate table of the 5 largest coefficients (by absolute value) for each of the ten target closing prices. Each feature is preceded by the word "lag" because it was lagged one day in order to simulate "yesterday's" news sentiment as a predictive factor for "today's" close price. We can see that the Direct keyword "oil" from the Financial News database was one of the top 5 most important features for 8 of the 10 targets! Second on the list is the Direct, Financial search phrase "marathon oil", followed by the Direct, Financial phrase "Phillips 66". Tied for third was the constant added to provide a y-intercept that is necessary in time-series modeling so not particularly valuable to us, however the next four most frequent are also news sentiment scores! We see the Indirect phrase "carbon footprint" from the Global News sources and then three more entries from the Direct, Financial news bucket, namely "valero", "occidental petroleum", and "fossil fuel". 
    ''')

    st.write('**ARIMA**')
    st.write('The second model we tried was an ARIMA model. There were several challenges to this model including the number of features and the amount of missing dates which had to be imputed or manually added. After performing a manual gridsearch, we discovered that the ARIMA model was able to make predictions of percent change (once differentiated) like the visualization below in reference to Marathon Oil.''')

    st.image('./images/arima2.png', use_column_width=True)
    st.write('''
    Again, news sentiment was vital to the success of the model. Features include the lagged closing prices of all 10, crude oil settle prices lagged, previous day open interest, crude oil futures, direct financial "oil" sentiment, direct global "pipeline", and indirect global "airline".
    ''')

elif page =='Create A Model':
    st.subheader('Create A Model')
    st.write('''
Use the checkboxes to select which features to include, then click "Run" to visualize the model.

Try it out for yourself:
    ''')

    d = st.checkbox('News Sentiment - Direct Keywords, Global News Sources')
    e = st.checkbox('News Sentiment - Direct Keywords, Financial News Sources')
    i = st.checkbox('News Sentiment - Indirect Keywords, Global News Sources')
    j = st.checkbox('News Sentiment - Indirect Keywords, Financial News Sources')
    f = st.checkbox('Financial and Commodity Indexes')
    featlist = [d,e,i,j,f]
    selectafeat = ['direct_g', 'direct_f','indirect_g', 'indirect_f', 'financial']

    st.write('*This model includes lagged (day before) closing price as a base feature by default; some features like mobility data were not included for the purposes of this demonstration.*')
    st.write('**The test data will appear on the graph in black, predictions for those same values will be overlaid in purple.**')   

    if st.button('Run Model!'): #if the button is clicked
        if d == False and e == False and i == False and j == False and f == False:
            st.write(model(featlist)) #output is a string
        else:
            st.table(model(featlist)) #output is a dataframe

    else:
        st.write('Click the button to run a model with your selected features')

elif page == 'Data Dictionary':
    st.subheader('Data Dictionary')

    st.write('**Commodity Prices**')
    st.markdown('''
    |Indicator|Data Type|Dataset|Region-Frequency|Description|
    |---|---|---|---|---|
    |**Brent Crude Oil**|*float*|Commodity Prices|Daily|Price, in USD per barrel, of North Sea Brent crude oil as traded on the Intercontinental Exchange(ICE).|
    |**WTI Crude Oil**|*float*|Commodity Prices|Daily|Price, in USD per barrel, of West Texas Intermediate(WTI) crude oil, the underlying commodity of the NYMSEX. It is the main oil benchmark for North America.|
    |**Settlement Price**|*float*|Commodity & Exchange|Daily|Price of final transaction on a futures exchange for a given "trading" day.|
    |**Open Interest**|*int*|Commodity & Exchange|Daily|Number of outstanding contracts(positions held) in the derivatives market. Open interest is an indicator of liquidity as each futures contract is for 100 shares.|''')

    st.write('**Google Mobility**')
    st.write('"Each Community Mobility Report is broken down by location and displays the change in visits to places like grocery stores and parks." [Direct link](https://www.google.com/covid19/mobility/)')
    st.markdown('''
    |Indicator|Data Type|Dataset|Region-Frequency|Description|
    |---|---|---|---|---|
    |**Grocery & Pharmacy**|*float*|Google Mobility|U.S. Daily|Mobility trends for places like grocery markets, food warehouses, farmers markets, specialty food shops, drug stores, and pharmacies.|
    |**Parks**|*float*|Google Mobility|U.S. Daily|Mobility trends for places like local parks, national parks, public beaches, marinas, dog parks, plazas, and public gardens.|
    |**Transit Stations**|*float*|Google Mobility|U.S. Daily|Mobility trends for places like public transport hubs such as subway, bus, and train stations.|
    |**Retail & Recreation**|*float*|Google Mobility|U.S. Daily|Mobility trends for places like restaurants, cafes, shopping centers, theme parks, museums, libraries, and movie theaters.|
    |**Residential**|*float*|Google Mobility|U.S. Daily|Mobility trends for places of residence.|
    |**Workplaces**|*float*|Google Mobility|U.S. Daily|Mobility trends for places of work.|
    ''')

    st.write('**Apple Mobility**')
    st.write('"This data is generated by counting the number of requests made to Apple Maps for directions in select countries/regions, sub-regions, and cities." [Direct link](https://covid19.apple.com/mobility)')
    st.markdown('''
    |Indicator|Data Type|Dataset|Region-Frequency|Description|
    |---|---|---|---|---|
    |**Value_(country)_walk**|*float*|Apple Mobility|Various Nations Daily|Change from baseline (100) in requests for walking directions in given country; ger=Germany, ind = India, rus=Russia, us=USA, jap=Japan|
    |**Value_(country)_drive**|*float*|Apple Mobility|Various Nations Daily|Change from baseline (100) in requests for driving directions in given country; ger=Germany, ind = India, rus=Russia, us=USA, jap=Japan|
    |**Value_(country)_trans**|*float*|Apple Mobility|Various Nations Daily|Change from baseline (100) in requests for transit routing in given country (not available for Russia or India); ger=Germany, us=USA, jap=Japan|

    ''')

    st.write('**News**')
    st.markdown('''
    |Indicator|Data Type|Dataset|Region-Frequency|Description|
    |---|---|---|---|---|
    |**d\_f\_(keyword)**|*float*|News Sentiment Score|Worldwide Daily|Daily News Sentiment score from Financial News sources related to Direct keywords: chevron, drilling, exxon, fossil_fuel, marathon_oil, occidental_petroleum, oil, oilfield, phillips_66, pipeline, valero|
    |**d\_g\_(keyword)**|*float*|News Sentiment Score|Worldwide Daily|Daily News Sentiment score from Global News sources related to Direct keywords: chevron, drilling, exxon, fossil_fuel, oil, oilfield, pipeline, valero|
    |**i\_f\_(keyword)**|*float*|News Sentiment Score|Worldwide Daily|Daily News Sentiment score from Financial News sources related to Indirect keywords: airline, carbon_footprint, emissions, epa, greenhouse, hurricane_storm, pollution, sanction, solar, turbine, vacation|    
    |**i\_g\_(keyword)**|*float*|News Sentiment Score|Worldwide Daily|Daily News Sentiment score from Global News sources related to Indirect keywords: airline, carbon_footprint, emissions, epa, greenhouse, hurricane_storm, pollution, sanction, solar, turbine, vacation|
    ''')

    st.write('**Financial Data**')
    st.markdown('''
    |Indicator|Data Type|Dataset|Region-Frequency|Description|
    |---|---|---|---|---|
    |**Value_(company)**|*float*|Closing Price|NYSE Daily|Daily close price for given company, used as target (y value) for modeling - companies: phillips_66, bp_plc, valero_energy_corporation, chevron_corporation, occidental_petroleum_corporation, marathon_oil_corporation, pioneer_natural_resources_company, conocophillips, exxon_mobil_corporation, marathon_petroleum_corporation|
    |**dow_jones_transportation_average**|*float*|Stock Market Index|U.S. Daily|"The Dow Jones Transportation Average (DJTA, also called the "Dow Jones Transports") is a U.S. stock market index from S&P Dow Jones Indices of the transportation sector, and is the most widely recognized gauge of the American transportation sector."[Wikipedia](https://en.wikipedia.org/wiki/Dow_Jones_Transportation_Average)|
    |**dow_jones_composite_average**|*float*|Stock Market Index|U.S. Daily|"The Dow Jones Composite Average is a stock index from Dow Jones Indexes that tracks 65 prominent companies. The average's components include every stock from the Dow Jones Industrial Average (30 components), the Dow Jones Transportation Average (20), and the Dow Jones Utility Average (15)."[Wikipedia](https://en.wikipedia.org/wiki/Dow_Jones_Composite_Average)|
    |**dow_jones_industrial_average**|*float*|Stock Market Index|U.S. Daily|"The Dow Jones Industrial Average (DJIA), Dow Jones, or simply the Dow (/ˈdaʊ/), is a stock market index that measures the stock performance of 30 large companies listed on stock exchanges in the United States."[Wikipedia](https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average)|
    |**dow_jones_utility_average**|*float*|Stock Market Index|U.S. Daily|"The Dow Jones Utility Average (DJUA, also known as the "Dow Jones Utilities") is a stock index from S&P Dow Jones Indices that tracks the performance of 15 prominent utility companies traded in the United States"[Wikipedia](https://en.wikipedia.org/wiki/Dow_Jones_Utility_Average)|
    |**s&p_500**|*float*|Stock Market Index|U.S. Daily|"The S&P 500, or simply the S&P, is a stock market index that measures the stock performance of 500 large companies listed on stock exchanges in the United States. It is one of the most commonly followed equity indices."[Wikipedia](https://en.wikipedia.org/wiki/S%26P_500)|
    ''')


elif page == 'About The Team':

    st.subheader('About The Team')
    st.write('''
We are curious, humble and enthusiastic data scholars, formerly classmates in General Assembly's Data Science Immersive program (Graduated December 2020). We entered this competition under the team name "Sc13nce Squad" because we were members of GA's DSI cohort #13.
    ''')
    st.image('./images/bran.JPG', use_column_width=True)

    st.write('''
**Brandon** - I am a data-driven strategist, decision-maker, and storyteller with an earnest appreciation for the collaborative nature of problem solving. My research experience analyzing and extracting insights from multidimensional data has instilled in me a fascination for a number of computer vision related tasks such as object localization, detection, and image segmentation. The quantitative and analytic nature of physics excites me and I actively pursue machine learning solutions, to data science problems, in the same way.

As a Data Scientist, I excel at overcoming technical challenges by my unique ability to work well with others in ways that leverage my customer-facing experience in the service industry with my rigorous training in STEM research. In particular, I attribute my achieving work ethic and communicative fluidity to a passion for making meaningful impacts on the community I live in, here and now. 

[Brandon's LinkedIn](https://www.linkedin.com/in/griffinbran/)
    ''')

    st.image('./images/will_hat.jpg', use_column_width=True)

    st.write('''
**Will** - After 8 successful years in logistics and management, I set out on a new career in Data Science in the Fall of 2020. I am passionate about finding practical solutions to complex problems and creating strategies that translate to every level of an organization. I enjoy developing novel approaches to help departments, teams, and individuals perform at their best and exceed expectations.

[Will's Portfolio Site](https://griffinwt.github.io/)
    ''')


    st.write('''
**With special thanks** to Nader Esmael, Cloudy Liu, James Salisbury & Cristina Sahoo.
    ''')

