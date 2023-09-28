import pandas as pd
import matplotlib.pyplot as plt

#Cargamos el archivo csv
data=pd.read_csv("ENAPREF_CAP200d.csv", delimiter=";", encoding="iso-8859-1")

#Ejemplo de filtro 

#Obtenemos el numero de encuestados cuyo nivel educativo sea 10

hablantes_quechua = data[(data['idioma_ninez'] =="1")]
print("Hablantes Quechua: ", len(hablantes_quechua))

hablantes_aymara = data[(data['idioma_ninez'] =="2")]
print("Hablantes Aymara: ", len(hablantes_aymara))

#hablantes_otros = data[(data['idioma_ninez'] ==3)]
#print("Hablantes Castellano: ", len(hablantes_otros))

hablantes_castellano = data[(data['idioma_ninez'] =="4")]
print("Hablantes Castellano: ", len(hablantes_castellano))

# Cantidad de hablantes en cada grupo
cantidad_quechua = len(hablantes_quechua)
cantidad_aymara = len(hablantes_aymara)
cantidad_castellano = len(hablantes_castellano)

# Datos para el gráfico de pastel
labels = ['Quechua', 'Aymara', 'Castellano']
sizes = [cantidad_quechua, cantidad_aymara, cantidad_castellano]
colors = ['blue', 'red', 'green']

# Crear el gráfico de pastel
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Proporción de Hablantes de Diferentes Idiomas')
plt.axis('equal')  # Esto asegura que el gráfico sea un círculo y no una elipse
plt.show()