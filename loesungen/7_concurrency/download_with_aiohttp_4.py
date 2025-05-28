import asyncio
import aiohttp

async def download_url(session, url):
    """Download a single URL and print the size of the response."""
    try:
        async with session.get(url, timeout=3.0) as response:
            try:
                content = await asyncio.wait_for(response.read(), timeout=2.0)
            except TimeoutError:
                print(f"Timeout for URL {url}!")
            else:
                print(f"Downloaded {url} ({len(content)} bytes), status: {response.status}")
        return 200 <= response.status <=299        
    except Exception as e:
        print(f"Error downloading {url}: {e}")

    return False   # optional

async def main():
    # URLs aus Datei lesen
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]

    async with aiohttp.ClientSession() as session:
        # Aufgabenliste erzeugen
        tasks = [download_url(session, url) for url in urls]
        # Alle Aufgaben gleichzeitig starten
        responses = await asyncio.gather(*tasks)
        print(f"Erfolgreiche Responses: {responses.count(True)}")

if __name__ == "__main__":
    asyncio.run(main())
