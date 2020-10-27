import sqlite3

class Database:
    #Atributes


    #Constructor
    def __init__(self):
        self.db_connection = sqlite3.connect('LSI.db')
        self.cursor = self.db_connection.cursor()
        self.create_table()

    #Destructor
    def __del__(self):
        self.db_connection.close()

    #Methods
    def create_table(self):
        self.cursor.execute("""
        create table setences(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            text VARCHAR(16000) NOT NULL
        );
        """)

    def insert_values(self, values = "anything"):
        params = [(values)]
        self.cursor.execute(f"""INSERT INTO setences(text) VALUES(?)""", params)
        self.db_connection.commit()
