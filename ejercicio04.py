# Escribe algún código para determinar si un número es un número Armstrong.

def chequear_armstrong(numero):
    lista_de_numeros = []
    # Convertimos el número en string para poder iterarlo y separar cada dígito
    for num in str(numero):
        lista_de_numeros.append(num)
    
    total_suma = 0

    for num in lista_de_numeros:
        total_suma = total_suma + pow(int(num), len(lista_de_numeros))

    if (total_suma == numero):
        return f"{numero} es un número Armstrong ya que el resultado del cálculo fue {total_suma}"
    else:
        return f"{numero} NO es un número Armstrong ya que el resultado del cálculo fue {total_suma}"

print(chequear_armstrong(9))
print(chequear_armstrong(10))
print(chequear_armstrong(153))
print(chequear_armstrong(154))