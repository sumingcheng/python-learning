import requests
from concurrent.futures import ThreadPoolExecutor


# 下载单个 URL 的函数
def download_url(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"成功下载: {url}, 内容长度: {len(response.content)}")
    except Exception as e:
        print(f"下载失败: {url}, 错误: {e}")


def main(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_url, urls)


if __name__ == "__main__":
    urls = [f"https://www.example.com/{i}" for i in range(10)]
    main(urls)
