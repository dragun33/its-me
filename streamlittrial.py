import string
from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st

# Function to process text
def process_text(text_content):
    cleaned_text = text_content.lower().translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.split()
    stop_words = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
                  "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom",
                  "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
                  "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but",
                  "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
                  "against", "between", "into", "through", "during", "before", "after", "above", "below", "to",
                  "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then",
                  "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few",
                  "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}
    return [word for word in words if word not in stop_words]

# Sentiment dictionary for categorizing words
sentiment_dict = {
    'modi': 'support', 'bjp': 'support', 'win': 'support', 'victory': 'support', 'trust': 'support',
    'success': 'support', 'coalition': 'support', 'nda': 'support', 'people power': 'support',
    'defeat': 'criticism', 'lose': 'criticism', 'corruption': 'criticism', 'polarisation': 'criticism',
    'failure': 'criticism', 'criticism': 'criticism', 'fraud': 'criticism', 'bribery': 'criticism',
    'conspiracy': 'criticism', 'unfair': 'criticism', 'fake': 'criticism', 'fear': 'criticism',
    'hope': 'mixed sentiment', 'optimism': 'mixed sentiment', 'concern': 'mixed sentiment',
    'uncertainty': 'mixed sentiment', 'doubt': 'mixed sentiment', 'expectation': 'mixed sentiment',
    'confidence': 'mixed sentiment', 'public trust': 'mixed sentiment', 'vitality': 'mixed sentiment',
    'diversity': 'mixed sentiment', 'federalism': 'mixed sentiment', 'livelihood': 'mixed sentiment',
    'inflation': 'mixed sentiment', 'unemployment': 'mixed sentiment',
    'candidate': 'neutral', 'voters': 'neutral', 'turnout': 'neutral', 'poll': 'neutral',
    'election': 'neutral', 'campaign': 'neutral', 'result': 'neutral', 'party': 'neutral',
    'coalition government': 'neutral', 'democracy': 'neutral', 'public': 'neutral'
}

# Function to classify sentiments
def classify_sentiments(words, sentiment_dict):
    sentiments = []
    for word in words:
        sentiment = sentiment_dict.get(word)
        if sentiment:
            sentiments.append(sentiment)
    return Counter(sentiments)

# Function to plot sentiment analysis bar chart
def plot_sentiments(sentiment_counts, title="Sentiment Analysis"):
    fig, ax = plt.subplots()
    ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color='turquoise')
    plt.xlabel("Sentiments")
    plt.ylabel("Count")
    plt.title(title)
    st.pyplot(fig)

# Function to plot sentiment distribution pie chart
def plot_distribution(sentiment_counts, title="Sentiment Category Distribution"):
    labels = list(sentiment_counts.keys())
    sizes = list(sentiment_counts.values())
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(title)
    st.pyplot(fig)

# Streamlit UI

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

# Text area for inputting or pasting text
text_input = st.text_area("Paste the text you wish to analyse here:")

if st.button("Analyze Sentiments"):
    if text_input:
        # Process input text
        words = process_text(text_input)
        # Classify sentiments
        sentiment_counts = classify_sentiments(words, sentiment_dict)
        
        # Display the first graph: Sentiment Analysis as a bar chart
        plot_sentiments(sentiment_counts, title="Sentiment Analysis on Election Results")
        
        # Display the second graph: Sentiment Category Distribution as a pie chart
        plot_distribution(sentiment_counts, title="Distribution of Sentiment Categories")
    else:
        st.write("Please paste some text to analyze.")
