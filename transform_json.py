import json

# Función para convertir el contenido del JSON al formato solicitado
def transform_json_to_prompts(input_json_file, output_json_file):
    # Cargar el archivo JSON original
    with open(input_json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Preparar la lista de prompts y completions
    transformed_data = []
    
    # Iterar sobre los párrafos de "content" y convertirlos al nuevo formato
    for paragraph in data['content']:
        if paragraph.strip():  # Asegurarse de que no esté vacío
            transformed_data.append({
                "prompt": paragraph.strip(),
                "completion": "no_depresión"  # La "completion" es fija como "depresión"
            })
    
    # Guardar el nuevo JSON en el formato solicitado
    with open(output_json_file, 'w', encoding='utf-8') as f:
        json.dump(transformed_data, f, ensure_ascii=False, indent=4)
    
    print(f"Archivo JSON transformado guardado como: {output_json_file}")

# Ejecutar la transformación
input_json_file = 'archivo2.json'  # Ruta del archivo original
output_json_file = 'no_depresion.json'  # Ruta del nuevo archivo

transform_json_to_prompts(input_json_file, output_json_file)
