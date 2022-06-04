import psycopg2

# query = 'select*from public. "Cambodia"'
con = psycopg2.connect(host="localhost",
                       database="Narendra1",
                       user="postgres",
                       password="narendra1552"
                       )


# cur=con.cursor()
# cur.execute(query)
# rows=cur.fetchall()
# for i in rows:
#     print(i)
#     cur.close()
#     con.close()
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:narendra1552@localhost:5432/Narendra1')
