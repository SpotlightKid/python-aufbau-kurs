import requests
import threading
from concurrent.futures import ThreadPoolExecutor

def download_url(url):
    """Download content from a URL and print length of response."""
    try:
        response = requests.get(url)
        print(f"Downloaded {url} ({len(response.content)} bytes)")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def threaded_download():
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
    threads = []
    for url in urls:
        t = threading.Thread(target=download_url, args=(url,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def pool_download():
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(download_url, url) for url in urls]
        for future in futures:
            future.result()

if __name__ == "__main__":
    print("Download mit threading.Thread:")
    threaded_download()
    print("\nDownload mit ThreadPoolExecutor:")
    pool_download()
