CREATE TABLE actividades (
    id SERIAL PRIMARY KEY,
    mensaje TEXT,
    actividad TEXT
);

INSERT INTO actividades (mensaje, actividad)
VALUES
('Registro de actividad', 'Fui a clases entender los ejercicios de base de datos avanzadas');
select * from actividades;

CREATE TABLE actividades_becas (
    id SERIAL PRIMARY KEY,
    mensaje TEXT,
    actividad TEXT
);

INSERT INTO actividades_becas (mensaje, actividad)
VALUES (
    'Martes - Registro de beca',
    'Ver y participar en las becas si podré ser uno de sus ganadores'
);

CREATE TABLE actividades_exposicion (
    id SERIAL PRIMARY KEY,
    mensaje TEXT,
    actividad TEXT
);

INSERT INTO actividades_exposicion (mensaje, actividad)
VALUES (
    'Miercoles',
    'Hacer una exposicion'
);


CREATE TABLE actividades_jueves (
    id SERIAL PRIMARY KEY,
    actividad TEXT,
    observacion TEXT
);

INSERT INTO actividades_jueves (actividad, observacion)
VALUES (
'Jueves mejorar las actividades del deber y mejorar el conocimiento en la clase de orientacion a objetos',
'Esta actividad me resulto muy dificil y mi PostgreSQL funciona con el puerto 5433 mientras que para la mayoria suele ser 5432'
);