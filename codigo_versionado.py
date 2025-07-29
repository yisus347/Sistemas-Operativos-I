
# Versión 1: Hola mundo
print("Hola mundo")

# ---------------------------------------

# Versión 2: Agrega una variable
mensaje = "Hola mundo"
print(mensaje)

# ---------------------------------------

# Versión 3: Añade entrada del usuario
mensaje = input("Escribe un mensaje: ")
print(mensaje)

# ---------------------------------------

# Versión 4: Añade función
def saludar():
    mensaje = input("Escribe un mensaje: ")
    print(mensaje)

saludar()

# ---------------------------------------

# Versión 5: Añade condiciones y ciclo
def saludar():
    for _ in range(3):
        mensaje = input("Escribe un mensaje: ")
        if mensaje == "":
            print("No escribiste nada.")
        else:
            print(mensaje)

saludar()
