import pandas as pd
import numpy as np
import os
from googleapiclient.discovery import build

# --- MOCK DATA FOR IMMEDIATE EXECUTION ---
# In a real environment, replace fetch_mock_data() with real API calls.
def fetch_mock_data(controversy_name, video_count=5):
    """
    Generates mock YouTube data for immediate pipeline testing.
    In a real scenario, this would call the YouTube Data API.
    """
    print(f"Generating mock data for controversy: {controversy_name}")
    
    # Mock comments array designed to test all aspects (positive, negative, neutral, polarized)
    mock_comments = [
        "I can't believe they did this. It's truly awful. I'm unsubscribing now! 😠", # Highly Negative
        "Honestly, I still love them. People make mistakes. Give them a break. ❤️", # Highly Positive
        "Not sure how I feel about this. The statement was long. I guess we'll see.", # Neutral/Subjective
        "Wow, that apology was so fake. They just did it for the money. #exposed #scam", # Negative, good for topic modeling
        "The brand should drop them immediately! I won't buy that product anymore.", # Brand focused, negative
        "This is an overreaction. They didn't do anything wrong. I support them 100%.", # Highly Positive/Supportive
        "I use their code to get a discount. Does this change anything? Probably not.", # Neutral/Engagement-focused
        "I was shocked when I saw the news. But I'll wait for the full story.", # Neutral
        "This is the worst thing I've ever seen on YouTube. Seriously disappointed.", # Highly Negative
        "Best video ever! What controversy? I don't care. LOL", # Positive, dismissive
    ] * (50 // 10) # Repeat to get a good number of rows

    data = {
        'video_id': [f'vid_{i % video_count}' for i in range(len(mock_comments))],
        'video_title': [f'{controversy_name} - Part {i % video_count}' for i in range(len(mock_comments))],
        'comment_text': mock_comments,
        'comment_likes': np.random.randint(1, 500, size=len(mock_comments)),
        'comment_date': pd.to_datetime('2025-09-01') + pd.to_timedelta(np.arange(len(mock_comments)), unit='h')
    }
    
    df = pd.DataFrame(data)
    return df.drop_duplicates(subset=['comment_text']).reset_index(drop=True)

# --- REAL API INTEGRATION PLACEHOLDER (NOT RUNNABLE WITHOUT KEY) ---
def get_youtube_service():
    """Initializes the YouTube Data API service object."""
    # Ensure you set the YOUTUBE_API_KEY environment variable
    API_KEY = os.environ.get("YOUTUBE_API_KEY")
    if not API_KEY:
        raise ValueError("YOUTUBE_API_KEY environment variable not set.")
    
    youtube = build("youtube", "v3", developerKey=API_KEY)
    return youtube

def fetch_real_video_data(youtube_service, query, max_results=50):
    """Placeholder for actual API scraping logic."""
    # In a real app, this function would call the API's search, video, and commentThreads endpoints
    # and structure the results into a DataFrame.
    print(f"Placeholder: Fetching real data for '{query}'...")
    return fetch_mock_data(query) # Fallback to mock data for demonstration

def run_data_pipeline(controversy_name):
    """Orchestrates the data acquisition and persistence."""
    try:
        # data = fetch_real_video_data(get_youtube_service(), controversy_name)
        data = fetch_mock_data(controversy_name) # Using mock data for immediate execution
        return data
    except ValueError as e:
        print(f"Error initializing YouTube API: {e}. Using mock data as fallback.")
        return fetch_mock_data(controversy_name)
        

def save_data(df, filename):
    """Saves the raw DataFrame to the data/raw folder."""
    filepath = f'data/raw/{filename}'
    df.to_csv(filepath, index=False)
    print(f"Raw data saved to {filepath}")


if __name__ == '__main__':
    # Example usage (for internal testing)
    df_raw = run_data_pipeline("Tarte Brand Trip Controversy")
    print(df_raw.head())
    save_data(df_raw, "tarte_raw_comments.csv")
