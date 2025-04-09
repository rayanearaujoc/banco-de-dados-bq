from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime
import os

class BigQuery:
    def __init__(self):
        caminho_credenciais = "credencial-servico.json"
        credentials = service_account.Credentials.from_service_account_file(caminho_credenciais)
        self.client = bigquery.Client(credentials=credentials, project=credentials.project_id)
        self.tabela = "mefirst-448318.petshop.cachorros"

    def execute_query(self, query):
        query_job = self.client.query(query)
        result = query_job.result()
        return result, query

    def insert_cachorro(self, nome, raca, idade, nome_tutor):
        agora = datetime.utcnow()
        query = f"""
            INSERT INTO `{self.tabela}` (nome, raca, idade, nome_tutor, data_criacao, data_atualizacao)
            VALUES ('{nome}', '{raca}', {idade}, '{nome_tutor}', DATETIME('{agora}'), DATETIME('{agora}'))
        """
        return self.execute_query(query)

    def update_cachorro(self, nome, nova_idade):
        agora = datetime.utcnow()
        query = f"""
            UPDATE `{self.tabela}`
            SET idade = {nova_idade}, data_atualizacao = DATETIME('{agora}')
            WHERE nome = '{nome}'
        """
        return self.execute_query(query)

    def delete_cachorro(self, nome):
        query = f"""
            DELETE FROM `{self.tabela}`
            WHERE nome = '{nome}'
        """
        return self.execute_query(query)