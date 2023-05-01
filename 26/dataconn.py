import psycopg2


class DBConn:
    def __init__(self, passwd, host="localhost", port=5432, database="postgres", user="postgres"):
        try:
            # Conexão com o banco de dados PostgreSQL
            self.conn = psycopg2.connect(
                host=host,
                port=port,
                database=database,
                user=user,
                password=passwd
            )
            # Criação de um objeto cursor
            self.cur = self.conn.cursor()
        except psycopg2.Error as e:
            print(f"Erro ao conectar com o banco de dados: {e}")

    def __del__(self):
        # Fechando o cursor e as conexões
        self.cur.close()
        self.conn.close()

    def init_db(self):
        # Código SQL para criação da tabela sensores
        tabela_sensores = """
        CREATE TABLE IF NOT EXISTS sensores (
          id SERIAL PRIMARY KEY,
          tipo VARCHAR(50) NOT NULL,
          unidade VARCHAR(10),
          localizacao VARCHAR(50),
          descricao TEXT
        );
        """
        # Código SQL para criação da tabela medicoes
        tabela_medicoes = """
        CREATE TABLE IF NOT EXISTS medicoes (
          id SERIAL PRIMARY KEY,
          ts timestamp NOT NULL,
          valor REAL NOT NULL,
          sensor_id INTEGER,
          FOREIGN KEY (sensor_id) REFERENCES sensores(id)
        );
        """
        try:
            # Executando o código SQL para criar as tabelas
            self.cur.execute(tabela_sensores)
            self.cur.execute(tabela_medicoes)
            # Realizando as alterações no banco de dados
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Erro ao criar as tabelas: {e}")

    def insert_sensor(self, sensor_list):
        try:
            for sensor_values in sensor_list:
                # Inserindo uma nova linha na tabela sensores
                self.cur.execute(
                    "INSERT INTO sensores (tipo, unidade, localizacao, descricao) VALUES (%s, %s, %s, %s)",
                    (sensor_values["tipo"], sensor_values["unidade"],
                     sensor_values["localizacao"], sensor_values["descricao"])
                )
            # Realizando as alterações no banco de dados
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Erro ao inserir dados na tabela sensores: {e}")

    def insert_medicao(self, medicao_list):
        try:
            for medicao_values in medicao_list:
                # Inserindo uma nova linha na tabela medicoes
                self.cur.execute(
                    "INSERT INTO medicoes (ts, valor, sensor_id) VALUES (%s, %s, %s)",
                    (medicao_values["ts"], medicao_values["valor"],
                     medicao_values["sensor_id"])
                )
            # Realizando as alterações no banco de dados
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Erro ao inserir dados na tabela medicoes: {e}")

    def select_data(self, sql_str):
        try:
            self.cur.execute(sql_str)
            return self.cur.fetchall()
        except psycopg2.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
