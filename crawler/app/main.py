import requests


def fetch_articles():
    url = "https://www.zhihu.com/api/v4/creators/creations/v2/article?start=0&end=0&limit=10&offset=0&need_co_creation=1&sort_type=created"
    headers = {
        "Authorization": "Bearer 你的Access_Token",
        "User-Agent": "你的User-Agent"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print("Failed to fetch data:", response.status_code)
        return None


articles = fetch_articles()
if articles:
    for article in articles:
        print(article['data']['title'], article['data']['created_time'])
