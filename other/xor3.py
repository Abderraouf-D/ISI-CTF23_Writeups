from pwn import *
from binascii import unhexlify
"""
p =  b'****************************'
k1 = b'****************************'
k2 = b'****************************'
a = xor(p, k1, k2)
b = xor(p, k1)
c = xor(p, k2)
print((a+b+c).hex())"""
h= unhexlify("4953491504467d2865765b7d2f614f640f0d7d0e5f67212b2d292f28786671746027191a54446a0c4b023e503a6c076a3e5e5012455016497866712230271f4b01476e4516502e006a394a363e54454a1c4a4b1c")

a=h[0:28]
b=h[28:2*28]
c=h[2*28:3*28]

k1=xor(a,b)
k2=xor(a,c)

p=xor(a,k1)
p=xor(p,k2)
print(p)

