# EXEMPLO 5 - fatorial de um número

numero = int(input('diga um número'))
if numero > 0:
 resultado = 1
 count = 1
while count <= numero:
    resultado *= count
    count += 1
print (resultado)

# Jeito dois

numero = int(input('Digite um número'))
if numero > 0:
   fatorial = 1
   for item in range(1, numero + 1):
      fatorial = fatorial * item
   print(fatorial)