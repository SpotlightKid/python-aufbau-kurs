import threading
import requests

def download_url(url):
    """Download content from a URL and print length of response."""
    try:
        response = requests.get(url)
        print(f"Downloaded {url} ({len(response.content)} bytes)")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    # URLs aus Datei lesen
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
    threads = []
    for url in urls:
        t = threading.Thread(target=download_url, args=(url,))
        t.start()
        threads.append(t)
    # Warten, bis alle Threads fertig sind
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
