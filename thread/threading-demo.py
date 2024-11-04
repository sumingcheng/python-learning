import threading
import requests


# 下载单个 URL 的函数
def download_url(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"成功下载: {url}, 内容长度: {len(response.content)}")
    except Exception as e:
        print(f"下载失败: {url}, 错误: {e}")


def main(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # 等待所有线程完成


if __name__ == "__main__":
    urls = [f"https://www.example.com/{i}" for i in range(10)]
    main(urls)
