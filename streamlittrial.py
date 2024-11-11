import string
from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st

# Sentiment Dictionary
sentiment_dict = {
    'modi': 'support', 'bjp': 'support', 'nda': 'support', 'amit shah': 'support',
    'trust modi': 'support', 'win': 'support', 'victory': 'support', 'success': 'support',
    'strong leadership': 'support', 'nationalist': 'support', 'growth': 'support',
    'development': 'support', 'make in india': 'support', 'people power': 'support',
    'coalition': 'support', 'progress': 'support', 'people’s choice': 'support',
    'defeat': 'opposition', 'lose': 'opposition', 'corruption': 'opposition', 'polarisation': 'opposition',
    'failure': 'opposition', 'fake': 'opposition', 'scam': 'opposition', 'fraud': 'opposition',
    'unfair': 'opposition', 'bribery': 'opposition', 'conspiracy': 'opposition', 'fear': 'opposition',
    'mismanagement': 'opposition', 'inefficiency': 'opposition', 'unemployment': 'opposition',
    'inflation': 'opposition', 'poverty': 'opposition',
    'election': 'neutral', 'candidate': 'neutral', 'voters': 'neutral', 'poll': 'neutral',
    'turnout': 'neutral', 'democracy': 'neutral', 'result': 'neutral', 'public': 'neutral',
    'campaign': 'neutral', 'party': 'neutral', 'manifesto': 'neutral', 'ballot': 'neutral',
    'coalition government': 'neutral', 'manifesto': 'neutral', 'debate': 'neutral', 'agenda': 'neutral',
    'vote': 'neutral', 'polling station': 'neutral', 'election commission': 'neutral',
    'hope': 'mixed', 'optimism': 'mixed', 'concern': 'mixed', 'uncertainty': 'mixed',
    'confidence': 'mixed', 'expectation': 'mixed', 'public trust': 'mixed', 'vitality': 'mixed'
}

# Streamlit UI
st.title("Election Result Sentiment Analysis")

# Text input area
text_input = st.text_area("Paste the election-related text here:")

# Button to analyze sentiments
if st.button("Analyze Sentiments"):
    if text_input:
        # Step 1: Clean and process the text
        cleaned_text = text_input.lower().translate(str.maketrans('', '', string.punctuation))
        words = cleaned_text.split()

        # Step 2: Initialize an empty list to hold emotions
        emotion_list = []

        # Step 3: Iterate through each word in the processed text and classify sentiment
        for word in words:
            # Instead of checking all keys, check directly if any sentiment term is in the word
            for key, sentiment in sentiment_dict.items():
                if key in word:  # Match if the word contains any of the sentiment keys
                    emotion_list.append(sentiment)  # Append the sentiment directly
                    break  # Stop checking after a match is found

        # Step 4: Count the occurrences of each sentiment using Counter
        sentiment_count = Counter(emotion_list)

        # Step 5: Display the sentiment counts
        st.write(f"Support: {sentiment_count['support']}")
        st.write(f"Opposition: {sentiment_count['opposition']}")
        st.write(f"Neutral: {sentiment_count['neutral']}")
        st.write(f"Mixed Sentiments: {sentiment_count['mixed']}")

        # Title in teal with larger font size and bold styling
        st.markdown("""
            <h1 style='color: #C70039; font-size: 60px; font-weight: bold; text-align: center;'>
                Election Sentiment Analysis
            </h1>
        """, unsafe_allow_html=True)

        st.markdown("""
            <h2 style='color: #581845 ; font-size: 28px; font-style: italic; text-align: center; padding: 10px;'>
                Dive into the Pulse of the Nation – Sentiments, Reactions, and Emotions around the Latest Election Results!
            </h2>
        """, unsafe_allow_html=True)

        # Step 6: Plot the sentiment counts in a bar chart
        fig, ax = plt.subplots()
        ax.bar(sentiment_count.keys(), sentiment_count.values(), color='skyblue')
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.title("Election Sentiment Analysis")
        st.pyplot(fig)
    else:
        st.write("Please paste some text to analyze.")
