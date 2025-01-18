from newsapi import NewsApiClient

# Initialize NewsAPI Client
api_key = '509a71a84ab34aeba02b8789d19ce213'
newsapi = NewsApiClient(api_key=api_key)

# Fetch top headlines
try:
    top_headlines = newsapi.get_top_headlines(
        q='bitcoin',
        category='business',  # Remove if using 'sources'
        language='en',
        country='us'  # Remove if using 'sources'
    )
    print("Top Headlines:")
    print(top_headlines)

except Exception as e:
    print(f"An error occurred while fetching top headlines: {e}")

# Fetch everything (if needed)
try:
    all_articles = newsapi.get_everything(
        q='bitcoin',
        domains='bbc.co.uk,techcrunch.com',
        #from_param='2023-01-01',
        #to='2023-12-31',
        language='en',
        sort_by='relevancy',
        page=2
    )
    print("\nAll Articles:")
    print(all_articles)

except Exception as e:
    print(f"An error occurred while fetching all articles: {e}")
