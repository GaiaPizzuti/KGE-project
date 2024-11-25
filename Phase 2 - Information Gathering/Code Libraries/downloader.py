import multiprocessing
import json
import os
import requests


def download_file(url, path):
    try:
        response = requests.get(url, timeout=30)
        response.encoding = "utf-8"
        with open(path, "w", encoding="utf-8") as g:
            json.dump(response.json(), g, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error downloading {url}: {e}")


if __name__ == "__main__":
    with open("sources.json") as f:
        urls = json.load(f)

    for category in urls:
        if category == "data_sources":
            for university in urls[category]:
                for url in urls[category][university]:
                    name = url.split("/")[-1]
                    path = f"../{university}/{name}"
                    path = path+".json" if not path.endswith(".json") else path
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    if os.path.isfile(name):
                        continue
                    multiprocessing.Process(
                        target=download_file, args=(url, path)).start()
                    print(f"[{name}]({url})")
