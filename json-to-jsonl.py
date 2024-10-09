import json

def convert_json_to_jsonl(json_file, jsonl_file):
    # Cargar el archivo .json
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Escribir el archivo .jsonl
    with open(jsonl_file, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')

# Ejecutar la conversión
json_file = 'json/data_set.json'  # Archivo original en formato JSON
jsonl_file = 'json/data_set.jsonl'  # Archivo de salida en formato JSONL
convert_json_to_jsonl(json_file, jsonl_file)
