import psycopg2

con = psycopg2.connect(database="escueladb", user="userit", host="localhost",
                       port="5432", password="3scu3l41t")
cur = con.cursor()
cur.execute("select * from accounts")

record = cur.fetchall()

for row in record:
    print(row)
