# Trabajo final de fundamentos de programación
# Emmily Daniela Vega Rincón
# Fase 5 - Evaluación final
# Fundamentos de programación
# Autoría propia



def calcular_jornada(horas):

    total_horas = sum(horas)

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total_horas, clasificacion


#Lista
recursos = []



for i in range(4):

    print(f"\nIngreso de datos del recurso {i + 1}")

    

    while True:

        nombre = input("Ingrese el nombre del trabajador: ")

        if nombre.isalpha():

            break

        else:

            print("Error: El nombre debe contener solamente letras.")


    horas = []

    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]



    for dia in dias:

        while True:

            try:

                hora = float(input(f"Ingrese horas trabajadas el {dia}: "))

                if hora < 0:

                    print("Error: Las horas no pueden ser negativas.")

                else:

                    horas.append(hora)
                    break

            except ValueError:

                print("Error: Debe ingresar solamente números.")



    recursos.append([nombre] + horas)



print("\nREPORTE SEMANAL DE HORAS\n")


for recurso in recursos:

    nombre = recurso[0]

    horas = recurso[1:]

    total_horas, clasificacion = calcular_jornada(horas)

    print("Nombre:", nombre)
    print("Total de horas:", total_horas)
    print("Clasificación:", clasificacion)
    print("---------------------------")