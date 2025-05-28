import threading

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
