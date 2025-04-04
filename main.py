import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Por favor introduce la cantidad de caracteres que desea en su contraseña = "))

password = ""

for i in range(longitud):
    password += random.choice(caracteres)

print(password)
