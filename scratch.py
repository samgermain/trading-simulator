import json
with open("assets/json/ada_usdt-15m.json", "rb") as file:
  data = json.load(file)

for i in data:
    print(i)