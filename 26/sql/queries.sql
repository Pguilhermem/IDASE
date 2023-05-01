-- Busca de todos os dados do sensor 1
SELECT * FROM medicoes WHERE sensor_id = 1

-- Busca de todos os dados do sensor 1 ordenados por valor em ordem ascendente
SELECT * FROM medicoes WHERE sensor_id = 1 order by valor asc

-- Busca dos 5 menores valores do sensor 1
SELECT * FROM medicoes WHERE sensor_id = 1 order by valor asc limit 5

-- Quantidade de registros do primeiro sensor
SELECT COUNT(*) FROM medicoes WHERE sensor_id = 1

-- valor máximo do sensor 1
SELECT MAX(valor) FROM medicoes WHERE sensor_id = 1

-- valor médio do sensor 1
SELECT AVG(valor) FROM medicoes WHERE sensor_id = 1

-- Busca através do nome do sensor ao invés do id usando JOIN (Combinação)
SELECT m.* FROM medicoes m
JOIN sensores s ON m.sensor_id = s.id
WHERE s.tipo = 'Termometro';

-- Alteração de restrição de tabela
ALTER TABLE medicoes
DROP CONSTRAINT IF EXISTS medicoes_sensor_id_fkey;

ALTER TABLE medicoes
ADD CONSTRAINT medicoes_sensor_id_fkey
FOREIGN KEY (sensor_id) REFERENCES sensores (id)
ON DELETE RESTRICT;

-- Remoção de dados da tabela sensores
DELETE FROM sensores WHERE id = 1

-- Inserção de um novo sensor
INSERT INTO sensores (tipo, unidade, localizacao, descricao) VALUES ('Termometro', 'Celsius','SalaX555', 'Mede a temperatura ambiente');

-- Alteração das colunas NULL Medições para o novo sensor
UPDATE medicoes
set sensor_id=5
WHERE sensor_id is NULL
