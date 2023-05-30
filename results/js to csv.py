import csv
import json

def json_to_csv(json_file, csv_file):
    # Buka file JSON dan file CSV
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        
        # Tulis header berdasarkan kunci pada objek pertama dalam JSON
        header = json_data[0].keys()
        csv_writer.writerow(header)
        
        # Tulis data ke file CSV untuk entitas
        # for row in json_data:
        #     ent = []
        #     for obj in row['entities']:
        #         ent.append('{entity : '+obj['entity']+', value : '+obj['value']+'}')
            
        #     pred_ent = []
        #     for obj in row['predicted_entities']:
        #         pred_ent.append('{entity : '+obj['entity']+', value : '+obj['value']+', confidence : '+str(obj['confidence_entity'])+'}')
        #     csv_writer.writerow([row['text'],ent,pred_ent])

        # Tulis data ke file CSV untuk intent
        for row in json_data:
            pred_int = []
            for obj in row['intent_prediction']:
                pred_int.append(row['intent_prediction'])
            csv_writer.writerow([row['text'],row['intent'],pred_int])

# Contoh penggunaan
json_file = r'D:\Skripsi\bimbingan\referensi\results\intent_successes.json'
csv_file = r'D:\Skripsi\bimbingan\referensi\results\intent_successes.csv'
json_to_csv(json_file, csv_file)
