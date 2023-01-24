
# Una función que toma una lista como argumento
def consultar_nota_final(lista_de_notas):
    # Para sacar el promedio y nota final, se suman todas las notas y se dividen por la cantidad de notas 
    # (nota1 + nota2 + nota3) / cantidad_de_materias

    # Se chequea que el argumento ingresado sea de tipo lista
    if (type(lista_de_notas) == list):
        
        suma_total_notas = 0 # La suma total se va a almacenar en esta variable

        # Se suman todas las notas ejecutando un for loop solo si los valores de la lista son números mayores a 0
        for nota in lista_de_notas:
            if (type(nota) == int):
                if (nota >= 1):
                    suma_total_notas += nota
                else:
                    return ValueError("Error: Las notas deben ser números igual o mayores a 1")
                
            else:
                return TypeError("Error: Las notas deben ser números") 
            
        # Se retorna el total dividido la cantidad de notas (o materias)
        return suma_total_notas / len(lista_de_notas)
    else:
        return TypeError("Error: El argumento debe ser una lista de números mayor o igual a 1")

print(consultar_nota_final([4, 5, 3])) # 4.0
print(consultar_nota_final([3, 2, 5])) # 3.3333
print(consultar_nota_final([3, 0, 1])) # Error: Las notas deben ser números igual o mayores a 1
print(consultar_nota_final("test")) # Error: El argumento debe ser una lista de números mayor o igual a 1
print(consultar_nota_final(["a", "b", "c"])) # Error: Las notas deben ser números

