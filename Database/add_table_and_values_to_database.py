#sending the dataset to the database
import mysql.connector
from mysql.connector import Error
hostname = "ezydkr.h.filess.io"
database = "DataFlowX_silkgasfor"
username = "DataFlowX_silkgasfor"
password = "1acbfe105f7cc7e4796ae8558fa8fa39fb2b57da"
port = "61002"

csv_file_path = "/content/olist_order_payments_dataset.csv"

table_name = "olist_order_payments"


try: 
  connection = mysql.connector.connect(host = hostname, database = database, user = username, password = password, port = port)
  if connection.is_connected():
    print("Connection to database is Successful")

    cursor = connection.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    print(f"table `{table_name}` is dropped if existed")


    create_table_query = f"""
    CREATE TABLE {table_name} (
      order_id VARCHAR(50),
      payment_sequential INT,
      payment_type VARCHAR(20),
      payment_installments INT,
      payment_value FLOAT

    );
    """

    cursor.execute(create_table_query)
    print(f"table `{table_name}` Created Successfully")


    data = pd.read_csv(csv_file_path)
    print("csv data loaded into pandas dataframe")


    batch_size = 500
    total_records = len(data)

    print(f"Starting data insertion into `{table_name}` with a batch size of `{batch_size} records`")
    for start in range(0, total_records, batch_size):
      end = start + batch_size
      batch = data.iloc[start:end]


      batch_records = [
          tuple(row) for row in batch.itertuples(index = False, name = None )

      ]


      insert_query = f"""
      INSERT INTO {table_name}
      (order_id, payment_sequential, payment_type, payment_installments, payment_value)
      values (%s, %s, %s, %s, %s)
      """


      cursor.executemany(insert_query, batch_records)
      connection.commit()
      print(f"Inserted records {start + 1} to {min(end, total_records)} successfully.")
  
  print(f"All {total_records} records inserted successfully into `{table_name}`.")


except Error as e: 
  print("Error while connecting to database or inserting data")
finally: 
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MYSQL connection is close")
