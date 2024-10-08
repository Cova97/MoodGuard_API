import json

# Función para combinar dos archivos JSON en uno solo
def combine_json_files(depresion_file, no_depresion_file, output_file):
    # Cargar el archivo de depresión
    with open(depresion_file, 'r', encoding='utf-8') as f:
        depresion_data = json.load(f)
    
    # Cargar el archivo de no-depresión
    with open(no_depresion_file, 'r', encoding='utf-8') as f:
        no_depresion_data = json.load(f)
    
    # Combinar los datos
    combined_data = depresion_data + no_depresion_data
    
    # Guardar los datos combinados en un nuevo archivo
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=4)
    
    print(f"Archivo combinado creado: {output_file}")

# Ejecutar la función para combinar los archivos
combine_json_files('json/depresion.json', 'json/no_depresion.json', 'json/data_set.json')
