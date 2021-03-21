#standard imports
import streamlit as st
import pandas as pd
#REMINDER - to preview in local browser: strealit run file_name.py (in bash)

#custom imports
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import r2_score, mean_squared_error

st.set_page_config(
    page_icon=':fuelpump:',
    initial_sidebar_state='auto'
)

st.title('RMDS Hackathon')

page = st.sidebar.selectbox(
    'Select-A-Page',
    ('Overview', 'Models', 'About The Team')
)

#functions

def model(a_list):
    included = [] #list to put included features into
    for n in range(len(a_list)): #list of feature checkboxes
        if a_list[n]: #if box is checked (boolean)
            included.append(feats[n]) # create list of included features
    if len(included) == 0:
        return "Please choose at least one feature to include"
    else:
        return {f'Display model with {included} as features'} #this is where regression will be performed

    
if page == 'Overview':
    st.subheader('Overview')
    st.write('''

Display of models and visualizations related to RMDS / WorldData.ai Data Science competition.

''')
    st.subheader('Use the drop-down menu on the left to explore')

    st.image('./images/oilrig.jpg', caption='Photo by Clyde Thomas from unsplash.com (https://unsplash.com/@clydeo)', use_column_width=True)

elif page =='Models':
    st.subheader('Models')
    st.write('''
Use the checkboxes to select which features to include, then click "Run" to visualize the model.

Try it out for yourself:
    ''')

    d = st.checkbox('News Sentiment - Direct')
    i = st.checkbox('News Sentiment - Indirect')
    a = st.checkbox('Apple Mobility Data')
    g = st.checkbox('Google Mobility Data')
    c = st.checkbox('Commodity Pricing')
    w = st.checkbox('Dow Jones Indicators')
    e = st.checkbox('OECD Interest Rates')
    f = st.checkbox('Futures')
    featlist = [d,i,a,g,c,w,e,f]
    feats = ['direct','indirect','apple','google','commodity','dowjones','oecd','futures']

    if st.button('Run Model!'): #if the button is clicked
        st.write(model(featlist)) #run the function with chosen features
    else:
        st.write('Click the button to run a model with your selected features')

    #lookup = pd.read_pickle('./compressed/books_look_p3')

    #with open('./compressed/books_rec_small.pkl', 'rb') as f:
    #    recommender = pickle.load(f)

    #with open('./compressed/books_text_dict.pkl', 'rb') as f:
    #    text = pickle.load(f)

    #query = st.text_input('Please enter a word or phrase to search: ', max_chars=50)

    #wout = st.text_input('If you would like to exclude a term from your results, please enter it here: ', max_chars=50)

    #searched, recommendation = make_recs_new(query, wout)

    #if type(recommendation) == str:
    #    st.write(recommendation) #if result is a string, print it
    #else:
    #    st.write(searched) #show searched term
    #    st.table(recommendation) #if result is a df, show it

    st.write('''
    *SPACE FOR DATA DICTIONARY (IN TABLE FORMAT)
    ''')

elif page == 'About The Team':

    st.subheader('About The Team')
    st.write('''
Former GA DSI classmates (add text here)
    ''')

    #st.table(pd.read_pickle('./compressed/sample_pivot.pkl'))

    st.write('''
Brandon - (profile, optional image)
    ''')

    #st.image('./images/sample_vectors.png', use_column_width=True)

    st.write('''
Will - (profile, optional image)   
    ''')

    #st.image('./images/sample_vectors.png', use_column_width=True)

    st.write('''
James/Nader/Cloudy/Cristina content
    ''')

