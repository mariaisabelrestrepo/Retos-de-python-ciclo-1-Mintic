mas_productos='S'
subtotal=0
print('TIENDA LAS MERCEDES\n')
while mas_productos=='S':
    valorunitario= int(input('Ingrese el valor unitario: '))
    iva= str(input('¿El producto cuenta con IVA?S/N: ')).upper()
    cantidad= int(input('Ingrese la cantidad que lleva el cliente del producto a registrar: '))
    if iva=='S':
        print('IVA incluido')
        subtotal+=(valorunitario+(valorunitario*0.19))*cantidad
    else:
        print('PRODUCTO SIN IVA')
        subtotal+=valorunitario*cantidad
    print(f'SUBTOTAL: {subtotal}')
    mas_productos= str(input('¿Faltan productos por cobrar?S/N: ')).upper()
    if mas_productos== 'N':
        print(f'TOTAL A COBRAR: {subtotal}')
    


