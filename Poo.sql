CREATE TABLE actividades (
    id SERIAL PRIMARY KEY,
    mensaje TEXT,
    actividad TEXT
);

INSERT INTO actividades (mensaje, actividad)
VALUES
('Lunes - Registro de actividad', 'Fui a clases para entender los ejercicios de Bases de Datos Avanzadas'),
('Martes - Examen', 'Presentar el examen de Metodología de la Investigación'),
('Miércoles - Proyecto', 'Avanzar el proyecto de Programación Orientada a Objetos (POO)'),
('Jueves - Estudio', 'Repasar Flask y realizar ejercicios prácticos');

select * from actividades;

CREATE TABLE actividades_personales (
    id SERIAL PRIMARY KEY,
    mensaje TEXT,
    actividad TEXT
);

INSERT INTO actividades_personales (mensaje, actividad)
VALUES
('Viernes - Beca', 'Consultar el estado de la beca y participar en el proceso de selección'),
('Sábado - Exposición', 'Preparar y ensayar la exposición de Energías Renovables'),
('Domingo - GitHub', 'Subir el proyecto Flask al repositorio de GitHub y revisar el código'),
('Lunes - Práctica', 'Corregir errores del proyecto y mejorar el conocimiento en Programación Orientada a Objetos');

select * from actividades_personales;
Base de datos: Poo
 Usuario: normalmente postgres
 Contraseña: la que usas para entrar a PostgreSQL
Puerto: 5433 (en tu caso)

SELECT * FROM actividades;
SELECT * FROM actividades_personales;