#Ejercicio clase 3

clientes = int(input('Ingrese numero de clientes entre 1 y 10: '))
while clientes <1 or clientes >10:
    clientes = int(input('Ingrese numero de clientes entre 1 y 120: '))
else:
    for i in range(clientes):

        nombre = input('Ingrese nombre: ')
        edad = int(input('Ingrese edad: '))

        if edad < 18:
            condicion_edad = 'menor'
            tipo_de_venta = 'juguetes'
        elif edad < 65:
            condicion_edad = 'adulte'
            tipo_de_venta = 'ropa'

        print('Entonces: '+nombre+' '+'usted es '+condicion_edad+' '+'Y quiere comprar '+tipo_de_venta)

        tipo_de_precio = int(input('Ingrese cuanto desea gastar: '))

        if tipo_de_precio < 5000:
            tipo_de_tecnologia = 'Analogicos'
            tipo_de_prenda = 'Camisas'
        else:
            tipo_de_tecnologia = 'Digitales'
            tipo_de_prenda = 'Pantalones'

        print('Entonces: '+nombre+' '+'usted es '+condicion_edad+' '+'quiere comprar '+tipo_de_venta+' '+' y que sean de tipo '+tipo_de_tecnologia)
        print('Entonces: '+nombre+' '+'usted es '+condicion_edad+' '+'quiere comprar '+tipo_de_venta+' '+' y que sean de tipo '+tipo_de_prenda)
