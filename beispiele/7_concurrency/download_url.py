import requests

def download_url(url):
    """Download content from a URL and print length of response."""
    try:
        response = requests.get(url)
        print(f"Downloaded {url} ({len(response.content)} bytes)")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
