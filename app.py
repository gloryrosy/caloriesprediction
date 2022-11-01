
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

cal_model = pickle.load(open('copy_of_calories_burnt_prediction.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          ['Calories burnt Prediction' ],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Calories Prediction Page
if (selected == 'Calories Burnt Prediction'):
    
    # page title
    st.title('Calories burnt Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age ')
        
    with col2:
        Height = st.text_input('Height')
    
    with col3:
        Weight = st.text_input('Weight')
    
    with col1:
        Duration = st.text_input('Exercise Duration')
    
    with col2:
        Heart_Rate = st.text_input('Heart Rate')
    
    with col3:
        Body_Temp = st.text_input('Body Temparature')
    
   
    
    # code for Prediction
    cal_pred = ''
    
    # creating a button for Prediction
    
    if st.button('Predict Calories'):
        cal_prediction = cal_model.predict([[Age, Height, Weight, Duration, Heart_Rate, Body_Temp]])
        st.write('The Calories to be Burnt is',cal_prediction)
        
    st.success(cal_pred)




