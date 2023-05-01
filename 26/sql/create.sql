CREATE TABLE sensores (
  id SERIAL PRIMARY KEY,
  tipo VARCHAR(50) NOT NULL,
  unidade VARCHAR(10),
  localizacao VARCHAR(50),
  descricao TEXT
);

CREATE TABLE medicoes (
  id SERIAL PRIMARY KEY,
  ts timestamp NOT NULL,
  valor REAL NOT NULL,
  sensor_id INTEGER,
  FOREIGN KEY (sensor_id) REFERENCES sensores(id)
);