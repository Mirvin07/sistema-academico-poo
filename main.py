from datetime import date

from src.estudiante import Estudiante
from src.docente import Docente
from src.asignatura import Asignatura
from src.curso import Curso
from src.inscripcion import Inscripcion
from src.beca import Beca
from src.pago import Pago


def cargar_datos_demo():
    """
    Carga datos iniciales para demostrar el funcionamiento del sistema.
    """

    estudiante_1 = Estudiante(
        rut="12.345.678-9",
        nombre="Camila Torres",
        correo="camila.torres@universidad.cl",
        carrera="Ingeniería en Informática"
    )

    estudiante_2 = Estudiante(
        rut="18.456.789-1",
        nombre="Felipe González",
        correo="felipe.gonzalez@universidad.cl",
        carrera="Ingeniería en Informática"
    )

    estudiante_3 = Estudiante(
        rut="19.111.222-3",
        nombre="Valentina Muñoz",
        correo="valentina.munoz@universidad.cl",
        carrera="Ingeniería en Informática"
    )

    docente = Docente(
        rut="9.876.543-2",
        nombre="Marcelo Rojas",
        correo="marcelo.rojas@universidad.cl",
        especialidad="Programación Orientada a Objetos"
    )

    asignatura = Asignatura(
        codigo="POO101",
        nombre="Programación Orientada a Objetos",
        creditos=6
    )

    curso = Curso(
        codigo="POO101-A",
        asignatura=asignatura,
        horario="Lunes y Miércoles 10:00 - 11:30",
        cupo=2
    )

    curso.asignar_docente(docente)

    curso.inscribir_estudiante(estudiante_1)
    curso.inscribir_estudiante(estudiante_2)

    resultado_inscripcion_3 = curso.inscribir_estudiante(estudiante_3)

    inscripcion_1 = Inscripcion(estudiante_1, curso)
    inscripcion_1.registrar_calificacion(6.0)
    inscripcion_1.registrar_calificacion(5.5)
    inscripcion_1.registrar_calificacion(6.2)

    inscripcion_2 = Inscripcion(estudiante_2, curso)
    inscripcion_2.registrar_calificacion(3.5)
    inscripcion_2.registrar_calificacion(4.0)
    inscripcion_2.registrar_calificacion(3.8)

    beca_excelencia = Beca(
        nombre="Beca Excelencia Académica",
        porcentaje_descuento=50
    )

    pago_camila = Pago(
        arancel=1200000,
        fecha_pago=date.today()
    )

    estudiante_1.asignar_beca(beca_excelencia)
    estudiante_1.agregar_pago(pago_camila)

    datos = {
        "estudiantes": [estudiante_1, estudiante_2, estudiante_3],
        "docentes": [docente],
        "asignaturas": [asignatura],
        "cursos": [curso],
        "inscripciones": [inscripcion_1, inscripcion_2],
        "becas": [beca_excelencia],
        "pagos": [pago_camila],
        "resultado_inscripcion_3": resultado_inscripcion_3,
    }

    return datos


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """

    print()
    print("==============================================")
    print("     SISTEMA ACADÉMICO UNIVERSITARIO POO")
    print("==============================================")
    print("1. Ver estudiantes")
    print("2. Ver docentes")
    print("3. Ver asignaturas")
    print("4. Ver cursos")
    print("5. Ver estudiantes inscritos en curso")
    print("6. Ver calificaciones y estado académico")
    print("7. Ver becas y pagos")
    print("8. Probar control de cupo")
    print("0. Salir")
    print("==============================================")


def ver_estudiantes(estudiantes):
    print()
    print("=== LISTADO DE ESTUDIANTES ===")

    for estudiante in estudiantes:
        print(estudiante.mostrar_info())


def ver_docentes(docentes):
    print()
    print("=== LISTADO DE DOCENTES ===")

    for docente in docentes:
        print(docente.mostrar_info())


def ver_asignaturas(asignaturas):
    print()
    print("=== LISTADO DE ASIGNATURAS ===")

    for asignatura in asignaturas:
        print(asignatura.mostrar_info())


def ver_cursos(cursos):
    print()
    print("=== LISTADO DE CURSOS ===")

    for curso in cursos:
        print(curso.mostrar_info())


def ver_estudiantes_inscritos(cursos):
    print()
    print("=== ESTUDIANTES INSCRITOS ===")

    for curso in cursos:
        curso.listar_estudiantes()


def ver_calificaciones(inscripciones):
    print()
    print("=== CALIFICACIONES Y ESTADO ACADÉMICO ===")

    for inscripcion in inscripciones:
        print(inscripcion.mostrar_resumen())


def ver_becas_y_pagos(estudiantes, pagos):
    print()
    print("=== BECAS Y PAGOS ===")

    for estudiante in estudiantes:
        if estudiante.beca:
            print(estudiante.mostrar_info())
            print(estudiante.beca.mostrar_info())

            for pago in estudiante.pagos:
                print(pago.mostrar_info(estudiante.beca))
                pago.marcar_pagado()
                print("Después de registrar el pago:")
                print(pago.mostrar_info(estudiante.beca))
        else:
            print(f"{estudiante.nombre} no tiene beca registrada.")


def probar_control_cupo(resultado_inscripcion):
    print()
    print("=== CONTROL DE CUPO ===")

    if resultado_inscripcion:
        print("El tercer estudiante fue inscrito correctamente.")
    else:
        print("No se pudo inscribir al tercer estudiante: el curso no tiene cupos disponibles.")


def main():
    datos = cargar_datos_demo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_estudiantes(datos["estudiantes"])

        elif opcion == "2":
            ver_docentes(datos["docentes"])

        elif opcion == "3":
            ver_asignaturas(datos["asignaturas"])

        elif opcion == "4":
            ver_cursos(datos["cursos"])

        elif opcion == "5":
            ver_estudiantes_inscritos(datos["cursos"])

        elif opcion == "6":
            ver_calificaciones(datos["inscripciones"])

        elif opcion == "7":
            ver_becas_y_pagos(datos["estudiantes"], datos["pagos"])

        elif opcion == "8":
            probar_control_cupo(datos["resultado_inscripcion_3"])

        elif opcion == "0":
            print("Saliendo del sistema académico. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()