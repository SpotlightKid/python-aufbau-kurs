import threading
import requests

def download_url(url, n):
    """Download content from a URL and print length of response."""
    try:
        response = requests.get(url)
        print(f"Downloaded {url} ({len(response.content)} bytes)")
    
        if response.status_code == 200:
            with open(f"output_{n}.txt", "wb") as fobj:
                fobj.write(response.content)
        else:
            raise IOError(
                f"Request failed with status: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    # URLs aus Datei lesen
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
    threads = []
    for i, url in enumerate(urls):
        t = threading.Thread(target=download_url, args=(url, i+1))
        t.start()
        threads.append(t)
    # Warten, bis alle Threads fertig sind
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
