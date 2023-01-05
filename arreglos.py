
import numpy as np

#arreglo de 4 dimensiones ordenando nombre o edad
cabecera = [('nombre','S10'),('edad',int)]
arreglo=[[[[('Luis',25)],[('Pedro',35)]]],[[[('Maria',40)],[('Rosa',37)]]]]
dimensiones=np.array(arreglo, dtype=cabecera)
np.sort(dimensiones, order='nombre')