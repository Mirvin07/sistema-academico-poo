from datetime import date

from src.estudiante import Estudiante
from src.docente import Docente
from src.asignatura import Asignatura
from src.curso import Curso
from src.inscripcion import Inscripcion
from src.beca import Beca
from src.pago import Pago


def main():
    print("=== SISTEMA ACADÉMICO UNIVERSITARIO ===")
    print()

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

    resultado = curso.inscribir_estudiante(estudiante_3)

    print(asignatura.mostrar_info())
    print(curso.mostrar_info())
    print(docente.mostrar_info())
    print()

    curso.listar_estudiantes()
    print()

    if resultado:
        print("Estudiante inscrito correctamente.")
    else:
        print("No se pudo inscribir: el curso no tiene cupos disponibles.")

    print()
    print("=== REGISTRO DE CALIFICACIONES ===")

    inscripcion_1 = Inscripcion(estudiante_1, curso)
    inscripcion_1.registrar_calificacion(6.0)
    inscripcion_1.registrar_calificacion(5.5)
    inscripcion_1.registrar_calificacion(6.2)

    inscripcion_2 = Inscripcion(estudiante_2, curso)
    inscripcion_2.registrar_calificacion(3.5)
    inscripcion_2.registrar_calificacion(4.0)
    inscripcion_2.registrar_calificacion(3.8)

    print(inscripcion_1.mostrar_resumen())
    print(inscripcion_2.mostrar_resumen())

    print()
    print("=== GESTIÓN DE BECAS Y PAGOS ===")

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

    print(estudiante_1.mostrar_info())
    print(beca_excelencia.mostrar_info())
    print(pago_camila.mostrar_info(estudiante_1.beca))

    pago_camila.marcar_pagado()
    print("Después de registrar el pago:")
    print(pago_camila.mostrar_info(estudiante_1.beca))


if __name__ == "__main__":
    main()