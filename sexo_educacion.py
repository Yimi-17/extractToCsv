import pandas as pd
import matplotlib.pyplot as plt

#Cargamos el archivo csv
data=pd.read_csv("ENAPREF_CAP200d.csv", delimiter=";", encoding="iso-8859-1")

#Ejemplo de filtro 

#Obtenemos el numero de encuestados cuyo nivel educativo sea 10

# Filtrar los datos por sexo

sexo_masculino_puno = data[(data['sexo'] == "1") & (data['UBIGEO'] == 210101)]
print("Sexo Masculino Puno: ", len(sexo_masculino_puno))

sexo_femenino_puno = data[(data['sexo'] == "2") & (data['UBIGEO'] == 210101)]
print("Sexo Femenino en Puno: ", len(sexo_femenino_puno))

sin_sexo_puno = data[(data['sexo'] == " ") & (data['UBIGEO'] == 210101)]
print("Sin Sexo Puno: ", len(sin_sexo_puno))

sexo_masculino_juliaca = data[(data['sexo'] == "1") & (data['UBIGEO'] == 211101)]
print("Sexo Masculino Juliaca: ", len(sexo_masculino_juliaca))

sexo_femenino_juliaca = data[(data['sexo'] == "2") & (data['UBIGEO'] == 211101)]
print("Sexo Femenino en Juliaca: ", len(sexo_femenino_juliaca))

sin_sexo_juliaca = data[(data['sexo'] == " ") & (data['UBIGEO'] == 211101)]
print("Sin Sexo Juliaca: ", len(sin_sexo_juliaca))

categorias = ["Sexo Masculino Puno", "Sexo Femenino en Puno", "Sin Sexo Puno", "Sexo Masculino Juliaca", "Sexo Femenino en Juliaca", "Sin Sexo Juliaca"]
cantidad_encuestados = [len(sexo_masculino_puno), len(sexo_femenino_puno), len(sin_sexo_puno), len(sexo_masculino_juliaca), len(sexo_femenino_juliaca), len(sin_sexo_juliaca)]

# Crear el gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(categorias, cantidad_encuestados, color=['pink', 'skyblue', 'red', 'blue', 'orange', 'purple'])
plt.xlabel('Categorías')
plt.ylabel('Cantidad de Encuestados')
plt.title('Cantidad de Universitarios y Técnicos Encuestados')
plt.show()

