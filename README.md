# 🎤 Sentiment Analysis of Influencer Controversies using NLP & YouTube Data Scraping

## 🎯 Project Goal

This project investigates the immediate public reaction to a major influencer controversy by analyzing large volumes of user-generated content scraped from YouTube. The primary objective is to measure shifts in public sentiment, identify key thematic clusters in discussions, and understand the general trends in audience engagement following a scandal.

***

## 💻 Technologies and Libraries

This project was developed using a robust stack of Python technologies for data handling and Natural Language Processing (NLP), demonstrating proficiency in:

* **Core Languages:** Python
* **Sentiment Analysis:** **VADER** and **TextBlob**
* **Data Handling:** Pandas, NumPy
* **Web Scraping/API:** Google API Client (YouTube Data API v3)
* **Topic Modelling:** Scikit-learn (for LDA/NMF)
* **Visualization:** Matplotlib, Seaborn

***

## ⚙️ Methodology (Project Breakdown)

The analysis follows a three-step data science pipeline, mirroring the project requirements:

### 1. Data Acquisition and Processing
* Scraped YouTube data (titles, likes, comments) for videos related to the **[Name of Influencer]** controversy.
* Processed them to create structured datasets, storing raw data in `data/raw/` and cleaned data in `data/processed/` for analysis.

### 2. Sentiment Analysis
* Performed sentiment analysis using **VADER** and **TextBlob**, focusing on detecting public sentiment (polarity and subjectivity) around the controversy.
* **VADER** was used for its sensitivity to social media slang and emojis, while **TextBlob** provided a comparative, general sentiment measure.

### 3. Topic Modelling and Keyword Clustering
* Implemented **Topic Modelling** using **Latent Dirichlet Allocation (LDA)** on the comment text.
* Applied **Keyword Clustering** (via TF-IDF vectorization and LDA output) to analyze engagement and identify recurring themes and trends in public reactions.

***

## 📊 Key Findings and Results

**Data Source:** Comments from [Number] YouTube videos related to the **[Controversy Name]** over a period of [X] days.

| Analysis Type | Key Finding |
| :--- | :--- |
| **Overall Sentiment** | **[e.g., The average TextBlob polarity shifted from +0.15 (neutral-positive) to -0.05 (neutral-negative) post-controversy.]** |
| **VADER Polarity** | **[e.g., VADER showed a significant *increase in sentiment strength* (higher absolute compound score), indicating greater polarization and emotional intensity, rather than just universal negativity.]** |
| **Topic Modelling** | The LDA model identified **[Number]** dominant themes. The top 3 most discussed topics were: **Topic 1:** *[e.g., Apology & Accountability]*, **Topic 2:** *[e.g., Brand Sponsorship Ethics]*, and **Topic 3:** *[e.g., Community Defense of Influencer]*. |

***

## 🚀 How to Run the Project

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/srihariharan14/Sentiment-Analysis-Influencer-Controversies](https://github.com/srihariharan14/Sentiment-Analysis-Influencer-Controversies)
    cd Sentiment-Analysis-Influencer-Controversies
    ```

2.  **Set up Virtual Environment:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
    *(Note: Ensure you have set your YouTube API key as an environment variable before running the scraper.)*

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Analysis:**
    * Start the Jupyter server and navigate to the `notebooks/` folder.
    * Execute **`1.0_Data_Pipeline.ipynb`** to run the scraping and processing functions.
    * Execute **`2.0_Analysis_and_Results.ipynb`** to generate the sentiment charts, run the Topic Model, and view the final visualizations.

***

## 📂 Repository Structure

Sentiment-Analysis-Influencer-Controversies/
├── data/              # Stores all datasets
│   ├── raw/           # Raw, untouched scraped data (ignored by git)
│   └── processed/     # Cleaned data with added sentiment scores
├── notebooks/         # Sequential Jupyter notebooks for execution and results
├── src/               # Modular Python scripts (reusable functions)
│   ├── data_scraper.py
│   ├── sentiment_analyzer.py
│   ├── topic_modeler.py
│   └── __init__.py
├── .gitignore         # Excludes venv/ and data/raw/
└── requirements.txt   # Lists all Python dependencies