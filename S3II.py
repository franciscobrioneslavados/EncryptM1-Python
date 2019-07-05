import codecs
from itertools import product
from itertools import chain
from Crypto.Cipher import AES
from Crypto import Random
from binascii import hexlify, unhexlify
from datetime import datetime

# ---------------------------------------------------
# Nombre: GRUPO 21 K :  21 a5 21
# M1:  68 6f 6c 61 00 00 00 00 00 00 00 00 00 00 00 00
# C1:  6f ff cc d0 08 eb 30 2c e8 96 23 07 42 0e f1 f6
# M2:  20 20 20 20 63 68 61 6f 00 00 00 00 00 00 00 00
# C2:  40 17 34 7b 1b e5 48 46 f9 c4 fc c1 bc e2 20 2d
# ---------------------------------------------------


#############  OBTENER HORA INICIO Y FIN ############
fechaInicio = datetime.now()
# al final de la ejecucion


print 'Hora de inicio: ' + str(fechaInicio)
print ' '

a=['00','21','42','63','84','a5','c6','e7']
C1='6fffccd008eb302ce8962307420ef1f6'
s=0
fila=0
maximo=10000000

print 'Se imprimira cada: '     + str(maximo) + ' intentos de encontrar clave correcta'
print " "

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
        if (s==maximo):
                print "Intento Nro: " + str(fila) + ' \n' + 'LLave: ' +llavecambiante + ' \n' + 'Texto Encriptado: ' + text_enc_hx + ' \n' + 'Clave a encontrar: ' + C1 + '\n\n'
                s=0
        if text_enc_hx==C1:
                break
print "La llave: " + llavecambiante + ' fue usada para: '+ C1
fechaTermino = datetime.now()
tiempo = fechaTermino - fechaInicio # Devuelve tiempo de ejecucion
segundos = tiempo.seconds
print "texto Encontrado en la conbinacion: "+str(fila)
print "Hora Termino: " + str(fechaTermino)
print "Total transcurrido: " + str(tiempo)
print " "

