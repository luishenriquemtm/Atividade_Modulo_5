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

## Máquina Virtual

Para demonstrar o funcionamento do Airflow, criei uma máquina virtual no Google Cloud para acesso:

https://35.188.187.24:8080

Será fornecido login e senha para acesso somente para o avaliador do trabalho.

Para Instalação na máquina virtual do GCP, siga esses passos:

1) Crie uma máquina virtual. Estou usando aqui um tipo de máquina: e2-standard-4
    - Descrição: Debian, Debian GNU/Linux, 11 (bullseye), amd64 built on 20230411, supports Shielded VM features
2) Clique no botão SSH e abra o terminal.
3) Insira os comandos:
```
sudo su
```
apt-get update
```
apt install python
```
apt-get install software-properties-common
```
apt-get install python3-pip
```
export SLUGIFY_USES_TEXT_UNIDECODE=yes
```
pip3 install apache-airflow
```

4) Inicialize o Airflow
```
airflow db init
```

5) Crie um usuário e insira a senha quando solicitado
```
airflow users create \
 -— username admin \
 -— firstname FIRST_NAME \
 -— lastname LAST_NAME \
 -— role Admin \
 —- email email@email.com
 ```

 6) Ative o webserver
```
 airflow webserver --port 8080
 ```

 7) Em um novo terminal, inicie o scheduler do Airflow
```
sudo su
```
airflow scheduler
```

9) Nas configurações do Firewall do GCP, libere a porta 8080 e defina um IP Estático.

10) Crie uma pasta dags dentro da pasta /root/airflow e inisira o arquivo de dag.py.

## Lembrando que esses passos são para fins didático e servem para instalação básica.
