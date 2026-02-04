from sqlalchemy import create_engine

username = 'root'
password = 'password123'
host = 'localhost'
database = 'my_database'

connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

engine = create_engine(connection_string)

with engine.connect() as connection:
    result = connection.execute("SELECT * FROM my_table LIMIT 5;")
    for row in result:
        print(row)
