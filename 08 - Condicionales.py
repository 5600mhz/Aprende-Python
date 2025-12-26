#########################
#                       #
# Aprende Python en 60s #
# 5600 MHz              #
#                       #
#########################

# Condicionales

numero = 12


# Evaluar condicion
if numero > 5:
    # Este codigo se ejecuta si la
    # condicion es verdadera
    print("El numero es mayor que 5")
else: # "si no"
    # Este codigo se ejecuta si la
    # condicion NO es verdsdera
    print("El numero es <= que 5")


# Varias posibilidades
if numero > 100:
    # mayor que 100
    print(">100")
elif numero > 90 and numero < 100:
    # segunda opcion
    print(">90 y <100")
else: # "si no"
    # ninguna de las condiciones
    # se cumplio
    print("invalido")
