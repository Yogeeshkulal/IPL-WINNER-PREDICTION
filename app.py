import streamlit as st # type: ignore
import pandas as pd # type: ignore
import pickle
with open('pipe.pkl', 'rb') as file:
    model = pickle.load(file)
feature_names = [
    'score', 'target', 'overs', 'wickets',
    'batting_team_Delhi Capitals', 'batting_team_Kings XI Punjab',
    'batting_team_Kolkata Knight Riders', 'batting_team_Mumbai Indians',
    'batting_team_Rajasthan Royals', 'batting_team_Royal Challengers Bangalore',
    'batting_team_Sunrisers Hyderabad', 'bowling_team_Delhi Capitals',
    'bowling_team_Kings XI Punjab', 'bowling_team_Kolkata Knight Riders',
    'bowling_team_Mumbai Indians', 'bowling_team_Rajasthan Royals',
    'bowling_team_Royal Challengers Bangalore', 'bowling_team_Sunrisers Hyderabad',
    'city_Bangalore', 'city_Chennai', 'city_Delhi', 'city_Hyderabad',
    'city_Jaipur', 'city_Kolkata', 'city_Mumbai'
]
def predict_match_result(input_data):
    prediction = model.predict(input_data)
    return prediction[0]
st.title("IPL Match Winner Prediction")
batting_team = st.selectbox("Select Batting Team", 
    ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 
     'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 
     'Delhi Capitals', 'Rajasthan Royals'])

bowling_team = st.selectbox("Select Bowling Team", 
    ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 
     'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 
     'Delhi Capitals', 'Rajasthan Royals'])

city = st.selectbox("Select City", 
    ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata', 'Mumbai'])

score = st.number_input("Enter Score", min_value=0)
target = st.number_input("Enter Target", min_value=0)
overs = st.number_input("Enter Overs", min_value=0)
wickets = st.number_input("Enter Wickets", min_value=0)

if st.button("Predict Winner"):
    input_data = {
        'score': [score],
        'target': [target],
        'overs': [overs],
        'wickets': [wickets],
        'batting_team_Delhi Capitals': [1 if batting_team == 'Delhi Capitals' else 0],
        'batting_team_Kings XI Punjab': [1 if batting_team == 'Kings XI Punjab' else 0],
        'batting_team_Kolkata Knight Riders': [1 if batting_team == 'Kolkata Knight Riders' else 0],
        'batting_team_Mumbai Indians': [1 if batting_team == 'Mumbai Indians' else 0],
        'batting_team_Rajasthan Royals': [1 if batting_team == 'Rajasthan Royals' else 0],
        'batting_team_Royal Challengers Bangalore': [1 if batting_team == 'Royal Challengers Bangalore' else 0],
        'batting_team_Sunrisers Hyderabad': [1 if batting_team == 'Sunrisers Hyderabad' else 0],
        'bowling_team_Delhi Capitals': [1 if bowling_team == 'Delhi Capitals' else 0],
        'bowling_team_Kings XI Punjab': [1 if bowling_team == 'Kings XI Punjab' else 0],
        'bowling_team_Kolkata Knight Riders': [1 if bowling_team == 'Kolkata Knight Riders' else 0],
        'bowling_team_Mumbai Indians': [1 if bowling_team == 'Mumbai Indians' else 0],
        'bowling_team_Rajasthan Royals': [1 if bowling_team == 'Rajasthan Royals' else 0],
        'bowling_team_Royal Challengers Bangalore': [1 if bowling_team == 'Royal Challengers Bangalore' else 0],
        'bowling_team_Sunrisers Hyderabad': [1 if bowling_team == 'Sunrisers Hyderabad' else 0],
        'city_Bangalore': [1 if city == 'Bangalore' else 0],
        'city_Chennai': [1 if city == 'Chennai' else 0],
        'city_Delhi': [1 if city == 'Delhi' else 0],
        'city_Hyderabad': [1 if city == 'Hyderabad' else 0],
        'city_Jaipur': [1 if city == 'Jaipur' else 0],
        'city_Kolkata': [1 if city == 'Kolkata' else 0],
        'city_Mumbai': [1 if city == 'Mumbai' else 0],
    }

    input_df = pd.DataFrame(input_data)
    input_df_encoded = input_df.reindex(columns=feature_names, fill_value=0)
    result = predict_match_result(input_df_encoded)
    if result == 1:
        st.success(f"The predicted result is: {batting_team} wins!")  
    else:
        st.error(f"The predicted result is: {batting_team} loses.")
