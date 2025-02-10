import json

base_name = "DU-UNITN-mindprod-2016.json"

with open(base_name, "r") as f:
    base = json.load(f)

for i in range(17, 24):
    with open(base_name.replace("16", str(i)), "r") as f:
        data = json.load(f)
        base.extend(data)
    
with open("DU-UNITN-mindprod-2016-23.json", "w") as f:
    json.dump(base, f, indent=4)