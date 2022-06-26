
nota_acum=0
acum_porcentaje=0
print('¡Bienvenido! En esta aplicación los estudiantes podran gestionar las notas de su materia')
nombre=str(input('Ingrese el nombre del estudiante: '))
materia=str(input('Ingrese el nombre de la materia: '))
while True:
    
    nota=float(input('Ingrese la nota obtenida por el estudiante: '))
    porcentaje=int(input('Ingrese el porcentaje de la nota: '))
    acum_porcentaje+=porcentaje
    nota_acum+=(nota*porcentaje)/100
    if acum_porcentaje>100:
        acum_porcentaje-=porcentaje
        nota_acum-=(nota*porcentaje)/100
        print('El porcentaje evaluado de una materia no puede ser mayor a 100')
    elif acum_porcentaje<100:
        continuar=str(input('¿Faltan notas por ingresar?S/N: ')).upper()

    if acum_porcentaje== 100 or continuar=='N':
        if nota_acum>=3:
            print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acum} resultado en aprobado')
        elif nota_acum<3:
            print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acum} resultado en reprobado')
    break


