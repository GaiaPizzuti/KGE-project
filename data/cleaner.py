import json

if __name__ == "__main__":
    with open("sources.json") as f:
        urls = json.load(f)

    for category in urls:
        if category == "data_sources":
            for university in urls[category]:
                for url in urls[category][university]:
                    name = url.split("/")[-1]
                    file = f"./{university}/{name}"
                    file = file+".json" if not file.endswith(".json") else file
                    print(file)
                    with open(file) as f:
                        data = json.load(f)
                    with open(file, "w") as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                    