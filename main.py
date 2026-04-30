from src.estudiante import Estudiante
from src.docente import Docente


def main():
    estudiante = Estudiante(
        rut="12.345.678-9",
        nombre="Camila Torres",
        correo="camila.torres@universidad.cl",
        carrera="Ingeniería en Informática"
    )

    docente = Docente(
        rut="9.876.543-2",
        nombre="Marcelo Rojas",
        correo="marcelo.rojas@universidad.cl",
        especialidad="Programación Orientada a Objetos"
    )

    personas = [estudiante, docente]

    print("=== SISTEMA ACADÉMICO UNIVERSITARIO ===")
    print()

    for persona in personas:
        print(persona.mostrar_info())


if __name__ == "__main__":
    main()