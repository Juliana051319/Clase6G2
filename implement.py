from sistemaVet import *

def main():
    servicio_hospitalario = sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))

        if menu == 1:
            preg = input('''Si su mascotas es:
            1.Gato
            2.Perro
            ''')
            if preg == '1':

                if servicio_hospitalario.verNumeroFelinos() >= 7:
                    print("No hay espacio disponible...")
                    continue
                historia = int(input(" ingrese la historia clinica de la mascota: "))
                if servicio_hospitalario.verificarExisteFelinos(historia) == False:
                    nombre=input("Ingrese el nombre de la mascota: ")
                    tipo= "Felinos"
                    peso=int(input("Ingrese el peso de la mascota: "))
                    fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                    medicamento=Medicamento()
                    medicamento.asignarNombre(input("Ingrese nombre del medicamento: "))
                    medicamento.asignarDosis(int(input("Ingrese dosis del medicamento: ")))
                    mas = Mascota()
                    mas.asignarNombre(nombre)
                    mas.asignarHistoria(historia)
                    mas.asignarPeso(peso)
                    mas.asignarTipo(tipo)
                    mas.asignarFecha(fecha)
                    mas.asignarMedicamento(medicamento)
                    servicio_hospitalario.ingresarFelinos(mas)

                else:
                    print("Ya existe un Felino con el numero de historia clínica ingresado.")
            
            elif preg =='2':
                if servicio_hospitalario.verNumeroCaninos() >= 7:
                    print("No hay espacio disponible...")
                    continue
                historia = int(input(" ingrese la historia clinica de la mascota: "))
                if servicio_hospitalario.verificarExisteCaninos(historia) == False:
                    nombre=input("Ingrese el nombre de la mascota: ")
                    tipo= "Canino"
                    peso=int(input("Ingrese el peso de la mascota: "))
                    fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                    medicamento=Medicamento()
                    medicamento.asignarNombre(input("Ingrese nombre del medicamento: "))
                    medicamento.asignarDosis(int(input("Ingrese dosis del medicamento: ")))
                    mas = Mascota()
                    mas.asignarNombre(nombre)
                    mas.asignarHistoria(historia)
                    mas.asignarPeso(peso)
                    mas.asignarTipo(tipo)
                    mas.asignarFecha(fecha)
                    mas.asignarMedicamento(medicamento)
                    servicio_hospitalario.ingresarFelinos(mas)

                else:
                    print("Ya existe un Canino con el numero de historia clínica ingresado.") 

            else:
                print('Opción invalidad') 

            
        elif menu==2: # Ver fecha de ingreso
            preg = input('''Si su mascotas es:
            1.Gato
            2.Perro
            ''')
            if preg =='1':
                q = int(input("Ingrese la historia clínica de la mascota: "))
                fecha = servicio_hospitalario.verFechaIngresoFelinos(q)
                if fecha != None:  
                    print("La fecha de ingreso del Felino es: " + fecha)
                else:
                    print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            elif preg== '2':
                q = int(input("Ingrese la historia clínica de la mascota: "))
                fecha = servicio_hospitalario.verFechaIngresoCaninos(q)
                if fecha != None:  
                    print("La fecha de ingreso del Canino es: " + fecha)
                else:
                    print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            else:
                print('Opción invalida')
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento=servicio_hospitalario.verMedicamento(q)
            if medicamento != None: 
                print(f"El medicamento suministrado es: {medicamento.verNombre()} con dosis {medicamento.verDosis()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")



if __name__ == "__main__":
    main()