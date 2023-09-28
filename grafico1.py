import pandas as pd
import matplotlib.pyplot as plt

#Cargamos el archivo csv
data=pd.read_csv("ENAPREF_CAP200d.csv", delimiter=";", encoding="iso-8859-1")
print(data.head())

#Mostramos estadisticas descriptivas
print(data.describe())

#Ejemplo de filtro 

#Obtenemos el numero de encuestados cuyo nivel educativo sea 10

# Filtrar los datos por nivel educativo
universitarios=data[data['nivel_educativo']=="10"]
print("Universitarios encuestados: ", len(universitarios))
tecnicos=data[data['nivel_educativo']=="8"]
print("Tecnicos encuestados: ", len(tecnicos))

# Contar la cantidad de universitarios y técnicos
cantidad_universitarios = len(universitarios)
cantidad_tecnicos = len(tecnicos)

# Etiquetas para las barras
categorias = ['Universitarios', 'Técnicos']
cantidad_encuestados = [cantidad_universitarios, cantidad_tecnicos]

# Crear el gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(categorias, cantidad_encuestados, color=['lightblue', 'lightgreen'])
plt.xlabel('Nivel Educativo')
plt.ylabel('Cantidad de Encuestados')
plt.title('Cantidad de Universitarios y Técnicos Encuestados')
plt.show()
