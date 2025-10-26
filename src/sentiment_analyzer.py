import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Initialize VADER
VADER_ANALYZER = SentimentIntensityAnalyzer()

def clean_text(text):
    """Performs basic text cleaning for NLP."""
    if not isinstance(text, str):
        return ""
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove mentions and hashtags (keeping the text clean for sentiment)
    text = re.sub(r'@\w+|#\w+', '', text)
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    return text.strip()

def get_vader_scores(text):
    """Calculates VADER sentiment scores (compound, pos, neg, neu)."""
    scores = VADER_ANALYZER.polarity_scores(text)
    return scores['compound'], scores['pos'], scores['neg'], scores['neu']

def get_textblob_scores(text):
    """Calculates TextBlob sentiment scores (polarity and subjectivity)."""
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def analyze_sentiment(df):
    """
    Applies text cleaning and both VADER and TextBlob analysis to the
    'comment_text' column of the DataFrame.
    """
    # 1. Apply cleaning
    df['clean_comment'] = df['comment_text'].apply(clean_text)
    
    # 2. Apply VADER
    df[['vader_compound', 'vader_pos', 'vader_neg', 'vader_neu']] = df['clean_comment'].apply(
        lambda x: pd.Series(get_vader_scores(x))
    )
    
    # 3. Apply TextBlob
    df[['textblob_polarity', 'textblob_subjectivity']] = df['clean_comment'].apply(
        lambda x: pd.Series(get_textblob_scores(x))
    )
    
    print("Sentiment analysis complete (VADER and TextBlob applied).")
    return df

def save_processed_data(df, filename):
    """Saves the processed DataFrame to the data/processed folder."""
    filepath = f'data/processed/{filename}'
    df.to_csv(filepath, index=False)
    print(f"Processed data saved to {filepath}")

if __name__ == '__main__':
    # Example usage requires a DataFrame from the scraper
    from data_scraper import run_data_pipeline
    df_raw = run_data_pipeline("Sample Controversy")
    
    df_processed = analyze_sentiment(df_raw.copy())
    print("\nProcessed Data Head:")
    print(df_processed[['comment_text', 'clean_comment', 'vader_compound', 'textblob_polarity']].head())
