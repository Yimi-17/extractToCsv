import pandas as pd
import matplotlib.pyplot as plt

#Cargamos el archivo csv
data=pd.read_csv("ENAPREF_CAP200d.csv", delimiter=";", encoding="iso-8859-1")

#Ejemplo de filtro 

#Obtenemos el numero de encuestados cuyo nivel educativo sea 10

# Filtrar los datos por nivel educativo
universitarios_puno = data[(data['nivel_educativo'] == "10") & (data['UBIGEO'] ==210101)]
print("Universitarios encuestados en Puno: ", len(universitarios_puno))

tecnicos_puno = data[(data['nivel_educativo'] == "8") & (data['UBIGEO'] ==210101)]
print("Tecnicos encuestados en Puno: ", len(tecnicos_puno))

universitarios_juliaca = data[(data['nivel_educativo'] == "10") & (data['UBIGEO'] ==211101)]
print("Universitarios encuestados en Puno: ", len(universitarios_juliaca))

tecnicos_juliaca = data[(data['nivel_educativo'] == "8") & (data['UBIGEO'] ==211101)]
print("Tecnicos encuestados en Puno: ", len(tecnicos_juliaca))



categorias = ["Universitarios en Puno", "Técnicos en Puno", "Universitarios en Julica", "Técnicos en Juliaca"]
cantidad_encuestados = [len(universitarios_puno), len(tecnicos_puno), len(universitarios_juliaca), len(tecnicos_juliaca)]

# Crear el gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(categorias, cantidad_encuestados, color=['lightblue', 'lightgreen', 'red', 'blue'])
plt.xlabel('Categorías')
plt.ylabel('Cantidad de Encuestados')
plt.title('Cantidad de Universitarios y Técnicos Encuestados')
plt.show()






