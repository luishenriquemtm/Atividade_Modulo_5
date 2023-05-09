import sqlite3
import pandas as pd
from datetime import datetime, timedelta
from textwrap import dedent
from airflow.utils.edgemodifier import Label
from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.models import Variable
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['luis.silva@indicium.tech'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}
# Aqui define o caminho do arquivo de banco de dados
caminho_db = '/root/airflow/data/Northwind_small.sqlite'

# Aqui define o caminho do arquivo CSV de saída
arquivo_csv = '/root/airflow/data/output_orders.csv'

# Aqui define o caminho do arquivo TXT de saída
arquivo_txt = '/root/airflow/data/count.txt'

# Aqui define o caminho do arquivo OUTPUT
output = '/root/airflow/data/final_output.txt'

def extracao_orders_csv():
    conn = sqlite3.connect(caminho_db)
    df = pd.read_sql_query("SELECT * FROM 'Order'", conn)
    df.to_csv(arquivo_csv, index=False)
    conn.close()

def calculo_qnt_vendida():
    conn = sqlite3.connect(caminho_db)
    query = 'SELECT * FROM OrderDetail'
    df_order = pd.read_sql_query(query, conn)
    df_csv = pd.read_csv(arquivo_csv)
    df_merged = pd.merge(df_order, df_csv, left_on='OrderId', right_on='Id', how='inner')
    quantidade_total = df_merged[df_merged['ShipCity'] == 'Rio de Janeiro']['Quantity'].sum()
    with open (arquivo_txt, 'w') as f:
        f.write(str(quantidade_total))
    conn.close()

def export_final_output():
    import base64
    # Import count
    with open(arquivo_txt) as f:
        count = f.readlines()[0]
    my_email = Variable.get("my_email")
    message = my_email+count
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    with open(output,"w") as f:
        f.write(base64_message)
    return None

with DAG(
    
    # Aqui definimos a DAG
    
    'Cálculo da qnt. vendida',
    default_args=default_args,
    description='Desafio de Airflow Lighthouse Módulo V - Luis Henrique',
    schedule_interval='*/5 * * * *',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
   
) as dag:
    dag.doc_md = """
        Calcular qual a soma da quantidade vendida (Quantity) com destino (ShipCity) para o Rio de Janeiro.
    """
   
# Task 1: Extração do CSV
    task1 = PythonOperator(
        task_id='extrair_csv',
        python_callable= extracao_orders_csv,
        op_kwargs={'sqlite_file': caminho_db, 'csv_file': arquivo_csv}
    )

    task1.doc_md = dedent(
        """\
    #### Task Documentation

    Carrega a tabela 'Order' em um dataframe do pandas e salva num arquivo chamado "output_orders.csv"

    """
    )

    # Task 2: Calcular a quatidade vendida e extrair em um arquivo TXT
    task2 = PythonOperator(
        task_id='Soma_quantidade_Rio',
        python_callable= calculo_qnt_vendida,
        op_kwargs={'sqlite_file': caminho_db, 'csv_file': arquivo_csv, 'txt_file':arquivo_txt}
    )

    task2.doc_md = dedent(
        """\
    #### Task Documentation

    Carrega o arquivo "output_orders.csv" em um dataframe do pandas.
    Carrega a tabela 'OrderDetail' em um dataframe do pandas. 
    Cria o dataframe só com a cidade do Rio de Janeiro
    Faz o JOIN dos dados da tabela "Order" (em "output_orders.csv") e "OrderDetail" usando o campo "OrderID". 
    Pega os dados "ShipCity" onde o valor é igual a "Rio de Janeiro". 
    Calcula a quantidade vendida (quantidade_total) e salva em "count.txt"

    """
    )

    export_final_output = PythonOperator(
        task_id='export_final_output',
        python_callable=export_final_output,
        provide_context=True

    )

    task1 >> task2 >> export_final_output # define a ordem de execução das tarefas

    # Tarefa final para criptografar os arquivos gerados
