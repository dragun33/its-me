import string
from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit app UI
st.title("Election Sentiment Analysis")

# Text area for user input
text_input = st.text_area("Paste election-related text here:")

# Button to start sentiment analysis
if st.button("Analyze Sentiments"):
    if text_input:
        # Convert text to lowercase
        lower_case = text_input.lower()
        
        # Remove punctuation from the text
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
        
        # Split text into words
        tokenized_words = cleaned_text.split()
        
        # Define common stop words to remove
        stop_words = {
            "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
            "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom",
            "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
            "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but",
            "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
            "against", "between", "into", "through", "during", "before", "after", "above", "below", "to",
            "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then",
            "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few",
            "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
        }
        
        # Remove stop words
        filtered_words = [word for word in tokenized_words if word not in stop_words]
        
        # Define sentiment dictionary for specific terms
        sentiment_dict = {
            'modi': 'bjp', 'bjp win': 'bjp', 'narendra modi': 'bjp', 'trust modi': 'bjp',
            'bjp defeat': 'anti-bjp', 'modi lose': 'anti-bjp', 'fake government': 'anti-bjp',
            'rahul gandhi win': 'congress', 'congress lead': 'congress', 'congress gains': 'congress',
            'congress defeat': 'anti-congress', 'rahul failed': 'anti-congress', 'sonia criticized': 'anti-congress',
            'aap win': 'aap', 'arvind kejriwal': 'aap', 'kejriwal support': 'aap', 'aap defeat': 'anti-aap',
            'candidate': 'neutral', 'voters': 'neutral', 'turnout': 'neutral', 'poll': 'neutral',
            'hope': 'mixed', 'optimism': 'mixed', 'fear': 'mixed', 'concern': 'mixed', 'uncertainty': 'mixed'
        }
        
        # Classify each word into a sentiment category
        sentiments = [sentiment_dict[word] for word in filtered_words if word in sentiment_dict]
        
        # Count the number of occurrences for each sentiment
        sentiment_counts = Counter(sentiments)
        
        # Create a bar chart with sentiment categories and their counts
        fig, ax = plt.subplots()
        ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color='skyblue')
        plt.xlabel("Sentiments")
        plt.ylabel("Count")
        plt.title("EMOTIONS ON RESULTS OF LOK SABHA ELECTION")
        
        # Display the plot in the Streamlit app
        st.pyplot(fig)
    else:
        # Prompt for text input if empty
        st.write("Please paste some text to analyze.")
