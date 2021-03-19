cadenaPalabras = 'este es un texto el cual deben contar el numero de palabras que tiene, deben tener en cuenta, que algunas palabras se separa por un punto, y una coma, tambien hay que tener en cuenta, que las palabras escritas EN MAYUSCULAS y minusculas cuenta como una este. Texto'

signos=", : ; . ! ¡"

for r in signos:
    cadenaPalabras=cadenaPalabras.replace(r," ")

minusculas= cadenaPalabras.lower()
lista = minusculas.split()
print("cadena "+str(lista))

for i in lista:
    contador = lista.count(i)
    print(i+" "+str(contador))
