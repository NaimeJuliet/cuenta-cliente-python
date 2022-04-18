from Classes.Cliente import Cliente
from Classes.Cuenta import Cuenta
#Definir un menu para
#Registrar CLIENTE NUEVO/CUENTA

opcion=1
print("**********************************")
print("     Bienvenido a BANCOLOMBIA     ")
print("              MENÚ                ")
print("**********************************")
print("1--> Registrar Cliente. ")
print("0--> Salir. ")

while(opcion!=0):
    opcion=int(input("Digita una opcion"))
    
    if (opcion==1):
        nombre=input("Digite el nombre del usuario: ")
        apellido=input("Digite el apellido del usuario: ")
        cedula=input("Digite la cedula del usuario: ")
        saldoInicial=0
        numeroCuenta=input("Digite el numero: ")

        cuenta=Cuenta(numeroCuenta,saldoInicial)
        cliente=Cliente(nombre,apellido,cedula,cuenta)
  
