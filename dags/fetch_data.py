
import psycopg2


def fetch_info():

    try:
        conn = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()

        query = 'select * from docker_Assignment_table;'
        cursor.execute(query)
        data = cursor.fetchall()
        print("This is Data Execution time for every DAG runs :- ")
        for i in data:
            print(i)
        print("Data Fetched to the Console Successfully")


    except:
        print("Error in connection")
    finally:
        conn.close()
        print("No issues")
