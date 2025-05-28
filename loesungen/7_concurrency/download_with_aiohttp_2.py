import asyncio
import aiohttp

async def download_url(session, url):
    """Download a single URL and print the size of the response."""
    try:
        async with session.get(url) as response:
            content = await response.read()
            print(f"Downloaded {url} ({len(content)} bytes), status: {response.status}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

async def main():
    # URLs aus Datei lesen
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]

    async with aiohttp.ClientSession() as session:
        # Aufgabenliste erzeugen
        tasks = [download_url(session, url) for url in urls]
        # Alle Aufgaben gleichzeitig starten
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
