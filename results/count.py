# import re
# import json

# data = open('intent_report.json')

# json_data = json.load(data)
# text_count = sum(1 for item in json_data if re.search(r'"text"\s*:', json.dumps(item)))

# print("Jumlah label 'text':", text_count)
import json

with open('intent_errors.json', 'r') as file:
    data = json.load(file)

element_count = len(data)
print("Jumlah elemen data:", element_count)
