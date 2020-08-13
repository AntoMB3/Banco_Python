import math
from datetime import date

class Cuenta:
    __dinero = 0
    def __init__(self,nombre,clabe,vencimiento,dinero):
        self.nombre = nombre
        self.__clabe = clabe
        self.vencimiento = vencimiento
        self.__dinero = dinero

    #Redefinir la funcion de str para mostrar los datos de la cuenta de forma ordenada
    def __str__(self):
        return "Nombre del propietario: {} \n CLABE: {} \n Fecha de vencimiento: {} \n Saldo: {} ".format(self.nombre,self.__clabe,self.vencimiento,self.__dinero)

    #Realiza un aumento a la cantidad de dinero de la cuenta
    def deposito(self,valor):
        self.__dinero += valor
        print("Saldo actual es de: ",self.__dinero)

    #Checa que haya suficiente dinero en la cuenta
    def fondos_disponibles(self,valor):
        if self.__dinero >= valor:
            return True
        else:
            return False

    #Realiza una disminución al dinero de la cuenta
    def retiro(self,valor):
        if valor > self.__dinero: #Valida que tenga fondos suficientes
            print("No hay fondo disponibles para la acción")
        else:
            self.__dinero -= valor
            print("Saldo actual de la cuenta {} es de: {}  ".format(self.__clabe,self.__dinero))
    
    #Obtenemos la clabe de la cuenta
    def getclabe(self):
        return self.__clabe


#Una fucnión para realizar una transferencia, quitando fondos de un lado y depositáandolo en el otro
def transferencia(account,dic_cuentas):
    transfer_b = int(input("Ingresa la CLABE de la cuenta a transferir: ")) 
    cantidad = int(input("Ingresa cantidad a transferir: "))
    try:
        if account.fondos_disponibles(cantidad):
            dic_cuentas[transfer_b].deposito(cantidad) #En base al diccionario, buscamos una KeyError si la cuenta no se encuentra
            account.retiro(cantidad)
        else:
            print("Error")
    except KeyError:
        print("Error: Cuenta no encontrada")

#Crear una cuenta y  agregarla al diccionario
def crearcuenta(dic_cuentas):
    nombre = input("Ingresa el nombre: ")
    clabe = int(input("Ingresa la clabe: "))
    vencimiento = int(input("Ingresa la fecha de vencimiento: "))
    saldo_inicial = int(input("Ingresa el saldo inicial: "))
    nueva = Cuenta(nombre,clabe,vencimiento,saldo_inicial) #Se crea la cuenta
    dic_cuentas[clabe] = nueva #Se agrega al diccionario de cuentas

#Borra una cuenta en base a la CLABE
def borrar_cuenta(dic_cuentas, clabe):
    try:
        del(dic_cuentas[clabe])
    except KeyError:
        print("Error: Cuenta no existente: ")

def mostrar_cuenta(dic_cuentas):
    clabe = int(input("Ingrese la clabe: "))
    try:
        print(dic_cuentas[clabe])
    except KeyError:
        print("Error Cuenta no existente")

def validar_fecha(date):
    #Obtenemos la fecha dividiendola para compararlar
    month = 0
    year = 0
    temp = math.trunc(date / 1000)
    r1 = date % 1000
    month += temp * 10
    temp = math.trunc(r1 / 100)
    month += temp
    r1 = r1 % 100
    temp = math.trunc(r1 / 10)
    year += temp * 10
    r1 = r1 % 10
    year += r1

    #Obtenemos la fecha de hoy
    actual_date = today.strftime("%m/%y")
    temp_list_day = actual_date.split('/') #Hacemos una lista con el mes y el año separados para compararlos con los de arriba
    month_t = int(temp_list_day[0]) #Guardamos en variables separaadas el mes y año
    year_t = int(temp_list_day[1])
    if ((year_t > year) or (month_t > month and year_t == year)): #Comparamos con el m/y de la tarjeta para ver si no ha caducado
        return False
    else:
        return True



s = 1
dic_cuentas =  {} #Creamos un diccionario vacío de cuentas
today = date.today()
while s == 1:
    print("Qué deseas hacer? \n1. Crear cuenta \n2. Transferir a cuenta \n3. Eliminar cuenta \n4. Mostrar cuenta\n")
    resp = int(input())
    if resp == 1:
        crearcuenta(dic_cuentas)
    elif resp == 2:
        transfer_a = int(input("Ingrese la clabe de la cuenta de origen: "))
        if validar_fecha(dic_cuentas[transfer_a].vencimiento):
            try:
                transferencia(dic_cuentas[transfer_a],dic_cuentas)
            except KeyError:
                print("Error: Cuenta no existente")
        else:
            print("La tarjeta de origen ha vencido")
    elif resp == 3:
        del_a = int(input("Ingrese la clabe de la cuenta: "))
        borrar_cuenta(dic_cuentas, del_a)
    elif resp == 4:
        mostrar_cuenta(dic_cuentas)
    else:
        print("Opcion no valida")

    s = int(input("Desea hacer otra accion \n 1. Si \n 2. No "))