# -*- coding: utf-8 -*-
import codecs
from itertools import product
from itertools import chain
from Crypto.Cipher import AES
from Crypto import Random
from binascii import hexlify, unhexlify
from datetime import datetime
import time

# ---------------------------------------------------
# Nombre: GRUPO 21 K :  21 a5 21
# M1:  68 6f 6c 61 00 00 00 00 00 00 00 00 00 00 00 00
# C1:  6f ff cc d0 08 eb 30 2c e8 96 23 07 42 0e f1 f6
# M2:  20 20 20 20 63 68 61 6f 00 00 00 00 00 00 00 00
# C2:  40 17 34 7b 1b e5 48 46 f9 c4 fc c1 bc e2 20 2d
# ---------------------------------------------------

print '-------------------------------------------------------'
print '-------- Encriptor de Claves AES CIISA 2019 -----------'
print '-------------------------------------------------------'
print ''
fechaInicio = datetime.now()
print 'Hora de inicio: ' + str(fechaInicio)
print ''
print 'Mostrando a cada 10.000.000 de conbinaciones'

a=['00','21','42','63','84','a5','c6','e7']
C1='6fffccd008eb302ce8962307420ef1f6'
s=0
fila=0
maximo=10000000
start_time = time.time()

for i in chain(product(a,repeat=9)):
        s=s+1
        fila=fila+1
        llavecambiante='21a521'+''.join(i)+'00000000'
        key = unhexlify(llavecambiante)
        IV = unhexlify('00000000000000000000000000000000')
        encriptor= AES.new(key,AES.MODE_CBC,IV=IV)
        mb1 = unhexlify('686f6c61000000000000000000000000')
        text=encriptor.encrypt(mb1)
        text_enc_hx=hexlify(text)
        prox_time = (time.time() - start_time) / 60
        if (s==maximo):
                print "Intento Nº: " + str(fila / 10000000)  +\
                      '; LLave: ' +llavecambiante +\
                      '; Texto Encriptado: ' + text_enc_hx  +\
                      '; Clave a encontrar: ' + C1 +\
                      '; Tiempo Transcurrido: '+str(prox_time)
                s=0
        if text_enc_hx==C1:
                break

print ''
print '------------------------------------------------------'
print "Total de Combinaciones: " + fila
print "La llave: " + llavecambiante
print ' fue usada para: '+ C1
fechaTermino = datetime.now()
tiempo = fechaTermino - fechaInicio # Devuelve tiempo de ejecucion
segundos = tiempo.seconds
print "texto Encontrado en la conbinacion: "+str(fila)
print "Hora Termino: " + str(fechaTermino)
print "Total transcurrido: " + str(tiempo)
print " "

