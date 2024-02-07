import random, time
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

print("¿Cuántos caracteres quieres que tenga tu contraseña?")
number = int(input())


for i in range(number):
    password += random.choice(characters)

print("Espera, estamos generando tu contraseña")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("Listo!, Tu contraseña a sido generada con exito")
print(password)



