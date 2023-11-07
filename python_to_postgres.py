import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'pos'
username = 'postgres'
pwd = 'maneesha'
port_id = 5432

conn = None
cur = None

try:
    with psycopg2.connect(
        host=hostname,
        user=username,
        password=pwd,
        dbname=database,
        port=port_id
    ) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS employee;')

            create_script = (
                "CREATE TABLE IF NOT EXISTS employee ("
                "    id SERIAL PRIMARY KEY,"
                "    name VARCHAR(50) NOT NULL,"
                "    email VARCHAR(50) NOT NULL,"
                "    password VARCHAR(50) NOT NULL,"
                "    role VARCHAR(50) NOT NULL"
                ");"
            )

            insert_script = (
                'INSERT INTO employee '
                '(name, email, password, role) '
                'VALUES (%s, %s, %s, %s);'
            )

            insert_values = [
                ('maneesha', 'maneesha@gmail.com', 'maneesha', 'admin'),
                ('ann', 'ann@gmail.com', 'ann', 'admin'),
                ('denver', 'denver@gmail.com', 'denver', 'admin')
            ]

            cur.execute(create_script)
            conn.commit()

            for record in insert_values:
                cur.execute(insert_script, record)

            # cur.execute('SELECT * FROM employee')
            # rows = cur.fetchall()
            # for rec in rows:
            #     print(rec)

            cur.execute('SELECT * FROM employee')
            rows = cur.fetchall()
            for rec in rows:
                print(rec['name'])

            # update_script = (
            #     'UPDATE employee '
            #     'SET name = name '
            #     'WHERE id = %s;'
            # )

            delete_script = (
                'DELETE FROM employee '
                'WHERE id = %s;'
            )

            cur.execute(delete_script, (16,))

        conn.commit()

except psycopg2.Error as e:
    print("Error: ", e)
# check if connection is closed
finally:
    if conn is not None:
        conn.close()
