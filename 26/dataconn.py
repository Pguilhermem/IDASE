import psycopg2

class DBConn:
    """
    Classe que encapsula o acesso à base de dados com duas tabelas: sensores e medições
    """
    def __init__(self, passwd, host="localhost", port=5432, database="postgres", user="postgres"):
        """
        Inicializa uma conexão com o banco de dados PostgreSQL.

        :param passwd: senha de acesso ao banco de dados
        :param host: nome do host onde o banco de dados está sendo executado (padrão: localhost)
        :param port: número da porta para se conectar ao servidor PostgreSQL (padrão: 5432)
        :param database: nome do banco de dados a ser utilizado (padrão: postgres)
        :param user: nome do usuário utilizado para se conectar ao banco de dados (padrão: postgres)
        """
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
        except psycopg2.Error as _e:
            print(f"Erro ao conectar com o banco de dados: {_e}")

    def __del__(self):
        """
        Fecha o cursor e as conexões com o banco de dados.
        """
        # Fechando o cursor e as conexões
        self.cur.close()
        self.conn.close()

    def init_db(self):
        """
        Cria as tabelas 'sensores' e 'medicoes' no banco de dados.
        """
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
        except psycopg2.Error as _e:
            print(f"Erro ao criar as tabelas: {_e}")

    def insert_sensor(self, sensor_list):
        """
        Insere os dados de sensores na tabela 'sensores' do banco de dados.
        :param sensor_list: lista de dicionários com os valores a serem inseridos na tabela.
        """
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
        except psycopg2.Error as _e:
            print(f"Erro ao inserir dados na tabela sensores: {_e}")

    def insert_medicao(self, medicao_list):
        """
        Insere os dados de medições
        :param medicao_list: lista de dicionários com os valores a serem inseridos na tabela.
        """
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
        except psycopg2.Error as _e:
            print(f"Erro ao inserir dados na tabela medicoes: {_e}")

    def select_data(self, sql_str):
        """
        Executa uma consulta SQL no banco de dados.

        :param sql_str: string contendo a consulta SQL a ser executada.
        :return: uma lista com as linhas de resultado da consulta, ou None em caso de erro.
        """
        try:
            self.cur.execute(sql_str)
            return self.cur.fetchall()
        except psycopg2.Error as _e:
            print(f"Erro ao executar a consulta: {_e}")
            return None
