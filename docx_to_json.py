import docx
import json

# Función para extraer el texto de un archivo .docx
def docx_to_text(docx_file):
    doc = docx.Document(docx_file)
    text = []
    
    # Extraer cada párrafo del archivo .docx
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    
    return text

# Función para convertir el texto a formato JSON
def convert_docx_to_json(docx_file, json_file):
    # Extraer el texto del archivo .docx
    text = docx_to_text(docx_file)
    
    # Crear el diccionario que será convertido a JSON
    data = {
        "content": text
    }
    
    # Guardar el contenido en un archivo .json
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Archivo JSON creado: {json_file}")

# Ejecutar la conversión
if __name__ == "__main__":
    docx_file = "no depresion.docx"  # Cambia esto por el nombre de tu archivo .docx
    json_file = "archivo2.json"  # Cambia esto por el nombre del archivo .json de salida
    convert_docx_to_json(docx_file, json_file)
