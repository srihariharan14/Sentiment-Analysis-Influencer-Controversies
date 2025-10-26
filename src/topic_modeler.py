import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def display_topics(model, feature_names, n_top_words):
    """Prints the top N words for each topic."""
    output = []
    for topic_idx, topic in enumerate(model.components_):
        message = f"Topic #{topic_idx+1}: "
        top_words = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        message += ", ".join(top_words)
        output.append(message)
    return "\n".join(output)

def get_lda_topics(df, text_column='clean_comment', n_topics=5, n_top_words=10):
    """
    Performs LDA Topic Modelling and extracts keywords.
    """
    # Filter out empty or near-empty text entries
    df_filtered = df[df[text_column].str.len() > 10].copy()
    
    if df_filtered.empty:
        print("Not enough clean text data for Topic Modeling.")
        return "No topics generated."

    print(f"Running LDA on {len(df_filtered)} comments...")
    
    # 1. TF-IDF Vectorization
    tfidf_vectorizer = TfidfVectorizer(
        max_df=0.95, 
        min_df=2, 
        stop_words='english',
        ngram_range=(1, 2) # Include bigrams for better context
    )
    tfidf = tfidf_vectorizer.fit_transform(df_filtered[text_column])
    tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()

    # 2. LDA Model Training
    lda = LatentDirichletAllocation(
        n_components=n_topics, 
        max_iter=5, 
        learning_method='online', 
        random_state=42
    )
    lda.fit(tfidf)

    # 3. Extract and display topics
    topics_output = display_topics(lda, tfidf_feature_names, n_top_words)
    
    return topics_output

if __name__ == '__main__':
    # Example usage requires processed data
    # Create mock processed data for runnable test
    data = {
        'clean_comment': [
            "apology seems fake money", "love the creator always support", 
            "hate apology fake money", "dont care still buying product",
            "brand needs to drop them immediately", "unsubscribing now money",
            "brand ethics terrible always support", "love the content best creator"
        ]
    }
    df_mock = pd.DataFrame(data)
    
    topics = get_lda_topics(df_mock, n_topics=3, n_top_words=3)
    print("\nGenerated Topics:")
    print(topics)
