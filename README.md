## Diseño orientado a objetos

El sistema fue diseñado aplicando los principios de Programación Orientada a Objetos. Se definió una clase base `Persona`, desde la cual heredan las clases `Estudiante` y `Docente`, permitiendo reutilizar atributos y métodos comunes.

La clase `Curso` permite gestionar una sección académica asociada a una `Asignatura`, un `Docente` y varios estudiantes. Para registrar calificaciones y determinar aprobación o reprobación, se incorporó la clase `Inscripcion`, que representa la relación entre un estudiante y un curso.

Además, se agregaron las clases `Beca` y `Pago` para representar procesos administrativos complementarios, como descuentos por beneficios y cálculo de aranceles.

El diseño busca mantener modularidad, cohesión y bajo acoplamiento, separando responsabilidades en clases específicas.