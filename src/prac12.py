#!/src/bin/python
#!ecoding: UTF-8

import modulo
import time

nro_test=10
intervalos=[10, 50, 100, 150, 500, 550, 1000, 10000, 100000]
umbral=[1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
nombre = "prac12.txt"

#Abrimos el archivo y escribimos, como cabecera, el orden en el que almacenaremos los datos.

f=open(nombre, 'w')
f.write ('Intervalos,  Valor aproximado,  Porcetaje de fallos, Tiempo CPU \n ')
f.write('============================ \n')
# Vamos a 
for n in intervalos:
  p=[]
  p=p+[n]                                                 
  a=modulo.aproximacion(n)
  p=p+[a]                                                
  ci=time.clock()
  for e in umbral:                                       
    e=modulo.error(n, nro_test, e)
    p=p+[e]                                               
  cf=time.clock()                                       
  tp=cf-ci
  p=p+[tp]                                                
  f.write(str(p))                                         
  f.write("\n")
f.close()