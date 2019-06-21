import itertools
from Crypto.Cipher import AES
from itertools import product
import time
import binascii

#
# Nombre: GRUPO_21
# C1:  be f7 0b 69 5b 65 c0 31 60 33 d0 49 96 fe b4 36
# M1:  68 6f 6c 61 00 00 00 00 00 00 00 00 00 00 00 00
# M2:  20 20 20 20 63 68 61 6f 00 00 00 00 00 00 00 00
# C1:  a9 f3 f7 4e 15 e6 c0 09 88 d0 52 f2 fe 2a c1 9d
#

# strKey = 'e76300c6848400632163a50000000000'
# key = binascii.unhexlify(strKey)

# IV = binascii.unhexlify('00000000000000000000000000000000')
# encryptor = AES.new(key, AES.MODE_CBC, IV=IV)
# MB1 = binascii.unhexlify('686f6c61000000000000000000000000')
# text1 = encryptor.encrypt(MB1)

# text_enc_hex = binascii.hexlify(text1)

# print 'Texto1 encryptado de M1 en Hexadecimal: '
# print text_enc_hex

# raw_input('Presione tecla para seguir ....')

# encryptor = AES.new(key, AES.MODE_CBC, IV=IV)
# MB2 = binascii.unhexlify('202020206368616f0000000000000000')
# text2 = encryptor.encrypt(MB2)
# text_enc_hex = binascii.hexlify(text2)

# print 'Texto1 encryptado de M1 en Hexadecimal: '
# print text_enc_hex

# raw_input('Presione tecla para seguir ....')

start_time = time.time()
cont = 0
count = 0
test = [ '00', '21', '42', '63', '84', 'a5', 'c6', 'e7' ]

for item in product(test, repeat=12):
    cont = cont + 1
    strkey = ''.join(item) + '00000000'
    IV = binascii.unhexlify('00000000000000000000000000000000')
    key = binascii.unhexlify(strkey)
    encryptor = AES.new(key, AES.MODE_CBC, IV=IV)
    MB1 = binascii.unhexlify('686f6c61000000000000000000000000')
    text1 = encryptor.encrypt(MB1)
    textEnc = binascii.hexlify(text1)

    if (cont == 10000000):
        count = count + 1
        prox_time = (time.time() - start_time) / 60
        print 'Key: ' + strkey + ' Cont: ' + str(cont * count) + ' Time: ' + str(prox_time)
        cont = 0

    if (textEnc == 'bef70b695b65c0316033d04996feb436'):
        prox_time = (time.time() - start_time) / 60
        print ('Key Found!' + strkey + ' Cont: ' + str(cont) + ' Time: ' + str(prox_time))
        break

