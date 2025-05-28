from concurrent.futures import ThreadPoolExecutor

def main():
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
    # ThreadPoolExecutor mit, z.B., 4 Threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Alle Downloads gleichzeitig starten
        futures = [executor.submit(download_url, url) for url in urls]
        # Optional: auf Fertigstellung warten (und Fehler anzeigen)
        for future in futures:
            future.result()

if __name__ == "__main__":
    main()
