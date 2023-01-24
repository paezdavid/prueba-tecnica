
def validar_usuario(nombre_de_usuario):
    if (len(nombre_de_usuario) < 6):
        print('El nombre de usuario debe contener al menos 6 caracteres')
        return
    elif (len(nombre_de_usuario) > 12):
        print('El nombre de usuario no puede contener más de 12 caracteres')
        return
    elif (not nombre_de_usuario.isalnum()):
        print(TypeError('El nombre de usuario puede contener solo letras y números'))
    else: 
        print("Correcto!")
    

validar_usuario("a1b2c3")
validar_usuario("-------")
validar_usuario("aaaaa")
validar_usuario("aaaaaaaaaaaaa")