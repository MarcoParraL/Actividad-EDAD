import csv
import json


with open('listadoPersonasEdad.csv', 'r') as archivo_csv:
   
    lector_csv = csv.DictReader(archivo_csv)
    
    rangos = list(lector_csv)


for persona in rangos:
     
        edad = int(persona['edad'])
        
        if edad < 18:
            persona['clasificacionEdad'] = 'Menor de Edad'
        elif 18 <= edad < 31:
            persona['clasificacionEdad'] = 'Persona Joven'
        elif 31 <= edad <= 60:
            persona['clasificacionEdad'] = 'Persona Adulta'
        else:
            persona['clasificacionEdad'] = 'Adulto Mayor'


with open('ClasificaciónEdades.json', 'w',) as archivo_json:
 
    json.dump(rangos, archivo_json, indent=1,ensure_ascii=False)
