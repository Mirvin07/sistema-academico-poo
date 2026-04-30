# Sistema Académico Universitario - Programación Orientada a Objetos

## Descripción general

Este proyecto corresponde a un sistema académico universitario desarrollado en Python, aplicando los principios de la Programación Orientada a Objetos.

El sistema permite gestionar información básica de estudiantes, docentes, asignaturas, cursos, inscripciones, calificaciones, becas y pagos de arancel. Además, permite validar cupos de cursos, calcular promedios y determinar si un estudiante aprueba o reprueba una asignatura.

## Funcionalidades principales

- Registro de estudiantes y docentes.
- Creación de asignaturas y cursos.
- Asignación de docentes a cursos.
- Inscripción de estudiantes en cursos.
- Validación de cupos disponibles.
- Registro de calificaciones.
- Cálculo de promedio académico.
- Determinación de aprobación o reprobación.
- Asignación de becas.
- Cálculo de descuentos y pagos de arancel.
- Menú interactivo por consola.

## Principios de Programación Orientada a Objetos aplicados

### Herencia

Se utiliza una clase base `Persona`, desde la cual heredan las clases `Estudiante` y `Docente`.

### Polimorfismo

Las clases `Estudiante` y `Docente` sobrescriben el método `mostrar_info()`, permitiendo que cada tipo de persona muestre su información de manera específica.

### Encapsulamiento

Los atributos principales de las clases se definen como protegidos mediante el uso de guion bajo, por ejemplo `_nombre`, `_rut`, `_correo`, `_carrera`, entre otros.

### Modularidad

El sistema está dividido en distintos archivos dentro de la carpeta `src`, donde cada clase tiene una responsabilidad específica.

### Cohesión y bajo acoplamiento

Cada clase cumple una función concreta dentro del sistema, evitando concentrar toda la lógica en un solo archivo.

## Estructura del proyecto

```text
sistema-academico-poo/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── uml/
│   ├── diagrama_clases.puml
│   └── diagrama_clases.png
│
└── src/
    ├── __init__.py
    ├── persona.py
    ├── estudiante.py
    ├── docente.py
    ├── asignatura.py
    ├── curso.py
    ├── inscripcion.py
    ├── beca.py
    └── pago.py