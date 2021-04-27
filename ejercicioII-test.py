#Ejercicio II-test
#personas = int(input('Cuantas personas desea registrar?: '))
#while personas <1 or clientes >120:
#    personas = int(input('Cuantas personas desea registrar?: '))
#    print('Perfecto, iniciando proceso')
#else:
#    print('Numero no valido de personas')

clientes = int(input('Ingrese numero de clientes entre 1 y 120: '))
while clientes <1 or clientes >120:
    clientes = int(input('Ingrese numero de clientes entre 1 y 120: '))
else:
    for i in range(clientes):


        nombre = input('Ingrese nombre: ')
        apellido = input('Ingrese apellido: ')
        edad = int(input('Ingrese edad: '))



        if edad < 18:
            condicion_edad = 'menor'
        elif  edad < 65:
            condicion_edad = 'mayor'
        elif  edad < 120:
            condicion_edad = 'jubilado'
        else:
            condicion_edad = 'fallecido'

        print('Su nombre es: '+nombre+' '+apellido+' '+'Y usted es '+condicion_edad)
