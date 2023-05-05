# 🚀 Indicium - Desafio Airflow - Luis Henrique (Engenheiro de Dados Lighthouse) 🚀

## Desafio

Esse desafio é parte do programa da trilha "Orquestração com Airflow" e é pré-requisito para obtenção da competência de nível Trainee em Airflow.

## Problema 

- Utilizar o Airflow para extrair os dados do banco Northwind_small.sqlite.
    - *I)* Extrair dados da tabela "Order" do banco para um arquivo CSV, 
    - *II)* Fazer a junção com uma tabela "OrderDetail" do banco
    - *III)* Calcular o total vendido para a cidade do Rio de Janeiro (ShipCity), exportar para um arquivo TXT

### Instalação e criação de DAG

- 1. Clone este repositório em sua máquina local.
```
- 2. Acesse a pasta do projeto:
```
- 3. Crie um ambiente virtual 
```
python3 -m venv "nome do ambiente"
```
- 4. Ative o ambiente virtual:
```
source "nome do ambiente""/bin/activate
```
- 5. Instale as dependências do projeto:
```
pip install -r requirements.txt
```
- 6. Execute o script de instalação do Airflow:
```
bash install.sh
```
- 6. Inicie o Airflow.
```
airflow standalone
```
- 7. Acesse o Airflow em seu navegador através do endereço 'http://localhost:8080'.

#### Importante:

* As Dags criadas utilizam as bibliotecas sqlite3, pandas, datetime, textwrap e módulos da biblioteca airflow.
* A exportação da tabela "Order" utiliza o módulo sqlite3 para conexão ao arquivo Northwind_small.sqlite. Para isso, podemos fazer:
```

Crie uma conexão com a base de dados SQLite. Acesse a interface do Airflow e vá em Admin > Connections. Clique em "Create" e preencha os campos conforme as informações abaixo:

- Conn Id: sqlite
- Conn Type: SQLite
- Host: /path/to/northwind_small.sqlite (substitua pelo caminho completo para o arquivo northwind_small.sqlite em sua máquina)
- Schema: deixe em branco
- Login: deixe em branco
- Password: deixe em branco
- Port: deixe em branco
- Clique em "Save".

```

- Os arquivos de Banco de Dados (Northwind_small.sqlite), "output_orders.csv", "count.txt" e foram salvos na pasta data.