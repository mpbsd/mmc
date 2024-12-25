CREATE TABLE IF NOT EXISTS campus(
  x INT NOT NULL,
  y TEXT NOT NULL UNIQUE,
  PRIMARY KEY(x)
);

CREATE TABLE IF NOT EXISTS curso(
  x INT NOT NULL,
  y TEXT NOT NULL UNIQUE,
  PRIMARY KEY(x)
);

CREATE TABLE IF NOT EXISTS disciplina(
  x INT NOT NULL,
  y TEXT NOT NULL UNIQUE,
  PRIMARY KEY(x)
);

CREATE TABLE IF NOT EXISTS horario(
  x INT NOT NULL,
  y TEXT NOT NULL UNIQUE,
  PRIMARY KEY(x)
);

CREATE TABLE IF NOT EXISTS semestre(
  x INT NOT NULL,
  y TEXT NOT NULL UNIQUE,
  PRIMARY KEY(x)
);


CREATE TABLE IF NOT EXISTS blob(
  campus INT NOT NULL,
  curso INT NOT NULL,
  disciplina INT NOT NULL,
  horario INT NOT NULL,
  semestre INT NOT NULL,
  PRIMARY KEY(campus, curso, disciplina, horario, semestre),
  FOREIGN KEY(campus) REFERENCES campus(x) ON UPDATE CASCADE,
  FOREIGN KEY(curso) REFERENCES curso(x) ON UPDATE CASCADE,
  FOREIGN KEY(disciplina) REFERENCES disciplina(x) ON UPDATE CASCADE,
  FOREIGN KEY(horario) REFERENCES horario(x) ON UPDATE CASCADE,
  FOREIGN KEY(semestre) REFERENCES semestre(x) ON UPDATE CASCADE
);

.mode csv
.separator ;

.import csv/campus.csv campus
.import csv/curso.csv curso
.import csv/disciplina.csv disciplina
.import csv/horario.csv horario
.import csv/semestre.csv semestre
.import csv/blob.csv blob

.mode table

select count(*) from blob;
