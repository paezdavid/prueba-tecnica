# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase, seguido
# del porcentaje de veces que aparece la letra en la frase.

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

def chequear_aparicion_de_letra(frase, letra):
    total_de_apariciones = frase.count(letra)
    porcentaje_de_apariciones = (total_de_apariciones / len(frase)) * 100

    return total_de_apariciones, porcentaje_de_apariciones

total, porcentaje = chequear_aparicion_de_letra(frase, letra)

print(f"La frase proveída contiene {len(frase)} letras")
print(f"La letra '{letra}' se repite {total} veces.")
print(f"El porcentaje de aparición de la letra '{letra}' es de {round(porcentaje, 2)}%")