#!/usr/bin/env python3
import json, sys, os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "genai-attack-payloads.json")
with open(path) as f:
    data = json.load(f)

for cat in data["categories"]:
    for p in cat["payloads"]:
        sys.stdout.write(p + "\n")
