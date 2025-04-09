# Gerenciador de Cadastro de Cachorros com Flask e BigQuery

Este projeto é uma aplicação web simples desenvolvida com Flask que permite gerenciar informações de cachorros, incluindo inserção, atualização e deleção de registros. Os dados são armazenados no Google BigQuery.

## Funcionalidades

- **Adicionar Cachorro**: Insere um novo registro de cachorro no BigQuery.
- **Atualizar Idade**: Atualiza a idade de um cachorro existente.
- **Deletar Cachorro**: Remove um registro de cachorro do banco de dados.

## Pré-requisitos

- Python 3.x instalado.
- Conta no Google Cloud com o BigQuery habilitado.
- Credenciais de uma conta de serviço do Google Cloud.

## Configuração

1. **Clonar o Repositório**:

   ```bash
    cd caminho-da-sua-pasta
   git clone https://github.com/rayanearaujoc/banco-de-dados-bq.git

2. **Criar e Ativar um Ambiente Virtual**:
    python -m venv venv
    'venv\Scripts\activate'

3. **Instalar as Dependências**:
    pip install -r requirements.txt

4. **Configurar as Credenciais do Google Cloud**:
    caminho_credenciais = "caminho-para-sua-chave-de-servico.json"

5. **Executar a Aplicação**:
    flask run