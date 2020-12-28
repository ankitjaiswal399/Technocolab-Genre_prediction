import streamlit as st
import pickle 
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))


    
def predict_genre(acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence):
    input = pd.DataFrame(np.array([[acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence]]).astype(np.float64))
    print(input)
    prediction = model.predict(input)

    return prediction
    

def main():

    html_temp = """
    <div class="main">
        <h1>Genre Prediction</h1
    </div>    
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    acousticness = st.text_input("Enter Acousticness", "0.1")
    danceability = st.text_input("Enter danceability", "0.1")
    energy = st.text_input("Enter energy", "0.1")
    instrumentalness = st.text_input("Enter instrumentalness", "0.1")
    liveness = st.text_input("Enter liveness", "0.1")
    speechiness = st.text_input("Enter speechiness", "0.1")
    tempo = st.text_input("Enter tempo", "0.1")
    valence = st.text_input("Enter valence", "0.1")
    
    rock_html = """
        <h2 style = "color: red"> Rock </h2>
    """
    
    hip_hop_html = """
        <h2 style = "color: red"> Hip-Hop </h2>   
    """
    output = predict_genre(0.988306,0.25566, 0.979774,9.730057e-01,0.121342,0.051740,90.241,0.034018)
    print(output)
    if output == 0.0:
        print('Rock')
        
    elif output == 1.0:
        print('Hip-Hop')
            
    if st.button("Predict"):
        output = predict_genre(acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence)
        #output = predict_genre(1,1,1,1,1,1,1,1)
        print(output)
        if output == 0.0:
            print('Rock')
            st.markdown(rock_html, unsafe_allow_html=True)
        elif output == 1.0:
            print('Hip-Hop')
            st.markdown( hip_hop_html, unsafe_allow_html=True)
if __name__ == '__main__':
    main() 
    