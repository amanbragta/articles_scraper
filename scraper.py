from newspaper import Article, Config
from fastapi import FastAPI

# 1. Setup - Adding a User-Agent helps avoid being blocked by news sites
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

app = FastAPI()

# 2. List of Logistics URLs (Add your links here)
# urls = [
#        "https://www.thehindu.com/news/international/nepal-election-2026-voting-time-results-gen-z-protests-kp-sharma-oli-world-news/article70705797.ece"
#     ]

def extract_news(url):
    try:
        print(f"Processing: {url}")
        article = Article(url, config=config)
        article.download()
        article.parse()
        # Formatting the date
        # publish_date = article.publish_date
        # if publish_date:
        #     formatted_date = publish_date.strftime('%Y-%m-%d')
        # else:
        #     formatted_date = "No Date Found"

        # Building the data dictionary
        return {
            "Title": article.title,
            "Content": article.text.replace('\n', ' '), # Clean newlines for CSV
            "Source": url
        }
        
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return {f"Error processing {url}: {e}"}

# 3. Execution and Export
# if __name__ == "__main__":
@app.get("/extract")
def extract(url: str):
    extracted_article = extract_news(url)
    print(extracted_article)
    return extracted_article

    # results = extract_news(urls)
    # print(results)
    
    # if results:
    #     df = pd.DataFrame(results)
    #     df.to_csv("logistics_news_data.csv", index=False, encoding='utf-8-sig')
    #     print("\nSuccess! Data saved to 'logistics_news_data.csv'")
    # else:
    #     print("No data extracted.")