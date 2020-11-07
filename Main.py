from Empleado import *

empleados = []

# Crear un empleado
e1 = Empleado()
e1.setNombre("Jonathan")
e1.setApellido("Campos Lozano")
e1.setSueldo(1000000)
e1.setDiasLiquidados(24)

#añadirlo al arreglo vacio
empleados.append(e1)

# Crear el segundo empleado 
e2 = Empleado()
e2.setNombre("Pedro")
e2.setApellido("Marciano")
e2.setSueldo(3000000)
e2.setDiasLiquidados(10)
# añadi al arreglo
empleados.append(e2)

'''
for i in empleados:
    print('******************')
    print(i)
'''
f = open('empleados.txt', 'w')
for i in empleados:
    f.write('\n******************\n')
    f.write(str(i))
f.close()



