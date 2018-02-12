import json

data = {'name': 'Paul'}

with open('data.json', 'w') as fh:
  json.dump(data, fh)

with open('data.json', 'r') as fh:
  data = json.load(fh)
  print(data)