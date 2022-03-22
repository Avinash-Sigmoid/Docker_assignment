
import psycopg2


def check_connection():

    try:
        conn = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()

        add_data = 'create table docker_Assignment_table as select dag_id, execution_date from dag_run order by ' \
                   'execution_date; '
        cursor.execute(add_data)
        conn.commit()

        print("data added to a new table Successfully")

        # query = 'select * from docker_Assignment_table;'
        # cursor.execute(query)
        # data = cursor.fetchall()
        # print("This is Data Execution time for every DAG runs :- ")
        # for i in data:
        #     print(i)
        # print("Data Fetched to the Console Successfully")


    except:
        print("Error in connection")
    finally:
        conn.close()
        print("No issues")
