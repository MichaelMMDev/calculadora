## quando usamos o metodo extend(), podemos adicionar uma lista completa dentro de outra, ao fim dela
## sintax: listaX.extend(listaY)

listaX=['Michael', 12345, 'lindo']
listaY=['é', 54321, 'Michael é lindo']

listaX.extend(listaY)

print(listaX)