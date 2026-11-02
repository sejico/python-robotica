medidas=[40,12,80,25]

print (medidas, type (medidas))
print (len(medidas))
print (medidas[0])
print (medidas[-1])

medidas.append (5)

print (medidas, type (medidas))

medidas.insert (2, 30)

print (medidas, type (medidas))
medidas[0] = 15

print (medidas, type(medidas))

medidas.remove (80)

print (medidas, type (medidas))

ordenadas = sorted (medidas)

print ( medidas, type (medidas))
print (ordenadas, type (ordenadas))
print (ordenadas [0])
print (ordenadas [-1])
print (medidas [1:4])
