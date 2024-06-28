import csv

def Reporte_GreenGarden ():
    nombre= str( input("Ingrese su nombre: "))
    direccion=str(input("Ingrese su direccion: "))
    numero=int(input("Ingrese su numero de telefono: "))
    print("")
    print ("-----GreenGarden----")
    print("")
    print ("productos:")
    print ("ABONO: 1.200 ") 
    print ("TIERRA: 1.000")
    print ("LIRIOS: 1.100")
    print ("ROSAS ROJAS: 1.700")
    print ("MARGARITAS: 1.100")
    print("")
    tipoproducto=input("Que producto desea?: ")
    if tipoproducto == "abono":
        precio=1200
    elif tipoproducto == "tierra":
        precio=1000
    elif tipoproducto == "lirios":
        precio= 11000
    elif tipoproducto == "rosas": 
        precio = 1700
    elif tipoproducto == "margarita": 
        precio =1100
    else:
        print("Producto no disponible, intente nuevamente.")
        return
    cantidad=int(input("Cantidad de productos: "))
    precio_total= precio*cantidad
    print ("Registro Exitoso. ")
    print ("--------BOLETA---------")
    print ("NOMBRE: ", nombre)
    print ("DIRECCION: ", direccion)
    print ("NUMERO TELEFONICO: ", numero)
    print ("PRODUCTO: ", tipoproducto)
    print ("CANTIDAD: ", cantidad)
    print ("PRECIO UNITARIO: ", precio)
    print ("PRECIO TOTAL", precio_total)

    with open ('Reporte_GreenGarden.csv', 'a', newline='') as (file):
        write= csv.writer(file)
        write.writerow ([nombre, direccion, numero, tipoproducto, cantidad, precio, precio_total])
    print ("PEDIDO REGISTRADO.")


def listapedidos():
    print("---Listado de los pedidos---")
    with open ('Reporte_GreenGarden.csv', 'r', newline='') as (file):
        reader = csv.reader (file)
        for row in reader: 
            print (f"nombre{row[0]}, direccion{row[1]}, numero{row[2]}, tipoproducto{row[3]}, cantidad{row[4]}, precio{row[5]}, preciototal{row[6]}")
def main(): 
    while True:
        print("----Sistema de registro de pedidos GreenGarden---- ")
        print("1- Registrar pedidos")
        print("2- Pedidos registrados")
        print("3- salir")
        opciones=input("Elija una opcion: ")
        if opciones=="1" or "uno":  
            Reporte_GreenGarden()
        elif opciones == "2" or "dos": 
            listapedidos()
        else:
            print ("Saliendo del sistema...")
            break
main()
