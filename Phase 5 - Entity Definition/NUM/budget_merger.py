import json
import shutil
import os

with open("project-finance.json", "r", encoding="utf-8") as f:
    budgets = json.load(f)

with open("project-overview.json", "r", encoding="utf-8") as f:
    projects = json.load(f)

for el in budgets:
    for p in projects:
        if p["project_id"] == el["project_id"]:
            p["budget"] = el["budget"]

if not os.path.isdir("old"):
    os.mkdir("old")

shutil.move("project-finance.json", "old/project-finance.json")
shutil.move("project-overview.json", "old/project-overview.json")

with open("project-overview.json", "w", encoding="utf-8") as f:
    json.dump(projects, f, indent=4, ensure_ascii=False)