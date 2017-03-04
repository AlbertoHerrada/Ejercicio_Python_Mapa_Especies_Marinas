# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 12:51:12 2017

@author: Alberto
"""
# Especies seleccionadas: Foca Monje (Monachusmonachus) y Posidonia Oceanica 
# Foca Monje en rojo y Posidonia Oceanica en azul

# INSTRUCCION
# Es necesario instalar el paquete Basemap desde Anaconda Navigator
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# MODIFICABLE
# Debeis ajustar las coordenadas del mapa a la localizacion de la especie
# La ayuda esta en: http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
map = Basemap(projection='mill', resolution='l', llcrnrlon=-25, llcrnrlat=20, urcrnrlon=40, urcrnrlat=60)

# MODIFICABLE
# Opciones del mapa
# Muchas mas en: http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
map.drawcoastlines(linewidth=0.5)
map.drawcountries(linewidth=0.5)
map.fillcontinents(color='0.9', alpha=0.5)
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30), labels=[False, False, False, True], linewidth=0.1)
map.drawparallels(np.arange(-90, 90, 30), labels=[False, True, False, False], linewidth=0.1)

# INSTRUCCION
# Debeis descargaros un fichero csv con un conjunto de registros (records) de una especie
# desde la pagina del OBIS: http://www.iobis.org y leerla en un DataFrame de pandas
# Ese DataFrame se debe llamar specie
speciefoca = pd.read_csv('Monachus_monachus.csv')
print(speciefoca)
specieposidonia =pd. read_csv('Posidonia_oceanica.csv')
print(specieposidonia)

# Datos de latitud y longitud de la especie
lonfoca, latfoca = map(list(speciefoca['longitude']), list(speciefoca['latitude']))
lonposidonia, latposidonia = map(list(specieposidonia['longitude']), list(specieposidonia['latitude']))

# MODIFICABLE
# Opciones de visualizacion de la especie
# Muchas mas en: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
map.plot(lonfoca, latfoca, 'ro', markersize=4, markeredgecolor='none' , label='Monachus_monachus')
map.plot(lonposidonia, latposidonia, 'bo', markersize=4, markeredgecolor='none' , label='Posidonia_oceanica')

# INSTRUCCION
# Debeis guardar la figura a un archivo pdf
map.drawcoastlines(linewidth=0.5)
map.drawcountries(linewidth=0.5)
map.fillcontinents(color='0.9', alpha=0.5)
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30), labels=[False, False, False, True], linewidth=0.1)
map.drawparallels(np.arange(-90, 90, 30), labels=[False, True, False, False], linewidth=0.1)
plt.legend(loc='lower right', fontsize='small')
plt.title('Mapa_distribucion_especies_marinas')
plt.savefig("distribution_map_species.pdf")
# Se muestra el mapa por pantalla
plt.figure()

