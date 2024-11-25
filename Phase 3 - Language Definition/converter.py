import json
import os


def recursive_namer(data, data_to_search):
    data_tmp = data.copy()
    for key, item in data_tmp.items():
        if key in data_to_search:
            del data[key]
        elif isinstance(item, dict):
            recursive_namer(item, data_to_search)
        elif isinstance(item, list):
            for i in item:
                if isinstance(i, dict):
                    recursive_namer(i, data_to_search)


def process_namer(data: dict) -> str:
    if "channel" in data:
        processes = data["channel"]["atomic_name"].split("2")
        return processes[0] if data["type"] == "Output" else processes[1]

    next_process_key = "process" if "process" in data else "process_then"
    if next_process_key not in data:
        raise ValueError(data)
    return process_namer(data[next_process_key])


data_to_remove = [
    "dotuur_utas",
    "surgaltyn_tuvshin",
    "bagts_tsag",
    "orokh_uliral",
    "todorkhoilson_ogNoo",
    "hicheeliin_tuluwluguunii_helber",
    "lyektsiin_bagts_tsag",
    "syeminaryn_bagts_tsag",
    "laboratoriin_bagts_tsag",
    "biye_daaltyn_bagts_tsag",
    "dadlaga_sudalgaany_bagts_tsag",
    "suraltsakh_khelber",
    "khelber",
    "ded_khelber",
    "page_number",
    "country",
    "sottoTipo",
    "titolari",
    "tutor"
]

if __name__ == "__main__":
    for folder in ["NUM", "UniTN"]:
        for file in os.listdir(folder):
            if not file.endswith(".json"):
                continue

            with open(f"{folder}{os.sep}{file}", "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                for dictionary in data.copy():
                    if dictionary in data_to_remove:
                        del data[dictionary]
                    elif isinstance(dictionary, dict):

                        recursive_namer(dictionary, data_to_remove)
                    elif isinstance(dictionary, list):

                        for i in dictionary:
                            if isinstance(i, dict):

                                recursive_namer(i, data_to_remove)
            elif isinstance(data, dict):
                recursive_namer(data, data_to_remove)

            with open(f"{folder}{os.sep}{file}", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
