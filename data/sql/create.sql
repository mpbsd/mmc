CREATE TABLE IF NOT EXISTS place(
  id INT NOT NULL,
  name TEXT NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS field(
  id INT NOT NULL,
  name TEXT NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS gradc(
  id INT NOT NULL,
  name TEXT NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS blob(
  place INT NOT NULL,
  field INT NOT NULL,
  gradc INT NOT NULL,
  setup TEXT NOT NULL,
  aterm TEXT NOT NULL,
  PRIMARY KEY(place, field, gradc, setup, aterm),
  FOREIGN KEY(place) REFERENCES place(id) ON UPDATE CASCADE,
  FOREIGN KEY(field) REFERENCES field(id) ON UPDATE CASCADE,
  FOREIGN KEY(gradc) REFERENCES gradc(id) ON UPDATE CASCADE
);

.mode csv
.separator ;

.import data/csv/place.csv place
.import data/csv/field.csv field
.import data/csv/gradc.csv gradc
.import data/csv/blob.csv blob

.mode table
