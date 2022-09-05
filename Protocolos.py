import os
a=0
print('''Creador de protocolos.''')
def menu():
    print('''
    Opciones
    1.-Crear
    2.-Agregar
    3.-Borrar
    4.-Visualisar''')
menu()
bandera=input("¿Quiere realizar alguna de las opciones dadas? s/n ")
if (bandera == "N" or bandera == "s" or bandera == "S" or bandera == "n"):

    while (bandera == "s" or bandera == "S"):
        opcion=int(input("¿Cuál es la que desea elegir? "))
        if opcion == 1:
            name=input("Escriba el nombre del protocolo: ")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            
            esc=input("¿Quiere escribir las instruciones? s/n ")
            while (esc == "s" or esc=="S"):
                a=a+1
                instruccion=input("Escriba la "+str(a)+"° instrucción: ")
                protocolo.write(str(a) +"-"+ instruccion + '''\n''')
                
                sub=input("¿Quiere escribir una subinstruccion? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escriba la subinstruccion: ")
                    protocolo.write("    "+str(a)+".1-"+subinstruccion+'''\n''')
                    
                esc=input("¿Quiere escribir la siguiente instrucion? s/n ")
            print("Has terminado el protocolo")
            protocolo.close()
            
        elif  opcion == 2:
            
            name=input("Escriba el nombre del protocolo que quiere agregar pasos: ")
            protocolo = open(name + ".txt",'a')
            
            esc=input("¿Quiere agregar una instrucion? s/n ")
            while (esc == "s" or esc=="S"):

                instruccion=input("Escriba la instruccion: ")
                protocolo.write("-"+ instruccion + '''\n''')
                
                sub=input("¿Quiere escribir una subinstruccion? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escriba la subinstruccion: ")
                    protocolo.write(".   -"+subinstruccion+'''\n''')
                    
                esc=input("¿Quiere escribir la otra instrucion? s/n ")
            print("Has terminado el cambio en el protocolo "+name)
            protocolo.close()
            
            
        elif  opcion == 3:
            name=input("Escriba el nombre del protocolo que quiere borrar: ")
            os.remove(name + ".txt")
            print("El fichero ha sido eliminado")
            
        elif  opcion == 4:
            name=input("Escriba el nombre del protocolo que quiere ver: ")
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.close()
                   
        bandera=input("¿Quiere realizar otra de las opciones dadas? s/n ")
        if (bandera=="s" or bandera=="S"):
            continue
        else:
            break
    print("Fin del programa")
    
else:
    print("Fin del programa")
