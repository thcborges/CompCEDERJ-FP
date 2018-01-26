import random
import struct


def intToQuadBytes(num):
    return struct.pack('<i', num)


def geraBinario(filename):
    f = open(filename, 'wb')
    v = 0
    for i in range(100):
        v = v + random.randint(1, 5)
        b = intToQuadBytes( v )
        f.write( b )
    f.close()


def geraBinario2(filename):
    f = open(filename, 'wb')
    for i in range(19, -1, -1):
        v1 = i % 2
        v2 = (v1 + 1) % 2
        b = struct.pack('<iff', i // 2, v1, v2)
        f.write( b )
    f.close()

#
#  Programa Principal
#
geraBinario('q5.bin')

geraBinario2('q6.bin')
