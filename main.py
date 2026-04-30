from src.estudiante import Estudiante
from src.docente import Docente
from src.asignatura import Asignatura
from src.curso import Curso


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


if __name__ == "__main__":
    main()