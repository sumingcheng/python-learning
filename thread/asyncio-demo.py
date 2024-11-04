import asyncio
import aiohttp


# 异步下载单个 URL 的函数
async def download_url(session, url):
    try:
        async with session.get(url, timeout=5) as response:
            content = await response.read()
            print(f"成功下载: {url}, 内容长度: {len(content)}")
    except Exception as e:
        print(f"下载失败: {url}, 错误: {e}")


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_url(session, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = [f"https://www.example.com/{i}" for i in range(10)]
    asyncio.run(main(urls))
