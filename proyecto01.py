

from random import randrange

def jugar():
    puntuacion_usuario = 0
    puntuacion_compu = 0

    while (puntuacion_usuario < 3 and puntuacion_compu < 3):
        eleccion_del_usuario = input("Elige un arma (piedra, papel, tijera): ")
        index_aleatorio = randrange(3)
        eleccion_de_compu = ['piedra', 'papel', 'tijera']

        if eleccion_del_usuario == eleccion_de_compu[index_aleatorio]:
            print('Empate')
            print(f"COMPU {puntuacion_compu} -- {puntuacion_usuario} USUARIO")
            
        elif eleccion_del_usuario == 'piedra' and eleccion_de_compu[index_aleatorio] == 'papel':
            print('Gana la compu porque eligió ' + eleccion_de_compu[index_aleatorio])
            puntuacion_compu += 1
            print(f"COMPU {puntuacion_compu} -- {puntuacion_usuario} USUARIO")
            
        elif eleccion_del_usuario == 'piedra' and eleccion_de_compu[index_aleatorio] == 'tijera':
            print('Gana el usuario porque la compu eligió ' + eleccion_de_compu[index_aleatorio])
            puntuacion_usuario += 1
            print(f"COMPU {puntuacion_compu} -- {puntuacion_usuario} USUARIO")
            
        elif eleccion_del_usuario == 'papel' and eleccion_de_compu[index_aleatorio] == 'piedra':
            print('Gana el usuario porque la compu eligió ' + eleccion_de_compu[index_aleatorio])
            puntuacion_usuario += 1
            print(f"COMPU {puntuacion_compu} -- {puntuacion_usuario} USUARIO")
            
        elif eleccion_del_usuario == 'papel' and eleccion_de_compu[index_aleatorio] == 'tijera':
            print('Gana la compu porque eligió ' + eleccion_de_compu[index_aleatorio])
            puntuacion_compu += 1
            print(f"COMPU {puntuacion_compu} -- {puntuacion_usuario} USUARIO")
            
        elif eleccion_del_usuario == 'tijera' and eleccion_de_compu[index_aleatorio] == 'papel':
            print('Gana el usuario porque la compu eligió ' + eleccion_de_compu[index_aleatorio])
            puntuacion_usuario += 1
            print(f"COMPU {puntuacion_compu} -- {puntuacion_usuario} USUARIO")
            
        elif eleccion_del_usuario == 'tijera' and eleccion_de_compu[index_aleatorio] == 'piedra':
            print('Gana la compu porque eligió ' + eleccion_de_compu[index_aleatorio])
            puntuacion_compu += 1
            print(f"COMPU {puntuacion_compu} -- {puntuacion_usuario} USUARIO")
            
        else:
            print("Esa arma no existe!")
        

jugar()