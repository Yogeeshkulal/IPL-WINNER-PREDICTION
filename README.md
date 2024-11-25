# IPL Match Winner Prediction

This project uses machine learning to predict the winner of IPL matches based on historical data. The model takes inputs like the score, target, overs, wickets, batting team, bowling team, and city, and predicts which team is likely to win.

## Features

- Predicts the winner of an IPL match based on the input features.
- Uses historical match data and a trained machine learning model for prediction.
- Allows users to input match details through a user-friendly interface built using Streamlit.

## Technologies Used

- **Python**: Programming language used for the project.
- **Streamlit**: Used for creating the interactive web interface.
- **scikit-learn**: Machine learning library used to train the model.
- **Pandas**: Used for handling data and data manipulation.

## How to Use

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Yogeeshkulal/ipl-match-winner-prediction.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

4. Once the app is running, input the details of the IPL match, such as batting team, bowling team, city, score, target, overs, and wickets. Then click "Predict Winner" to get the result.

## Data

The dataset used for training the model contains the following columns:

- `match_id`: Unique ID of the match.
- `batting_team`: The team that is batting.
- `bowling_team`: The team that is bowling.
- `city`: The city where the match is being played.
- `score`: The score achieved by the batting team.
- `target`: The target score to chase.
- `overs`: The number of overs played.
- `wickets`: The number of wickets lost.
- `result`: The outcome of the match (Win/Lose).


