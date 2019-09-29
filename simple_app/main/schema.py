import sqlite3
from abc import ABC, abstractmethod

class Schema:
    def __init__(self):
        self.connection = sqlite3.connect('todo.db')
        # self.create_user_table()
        self.create_to_do_table()
    
    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def create_to_do_table(self):
        print("Creating ToDo table")
        query = """
        CREATE TABLE IF NOT EXISTS "Todo"(
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT
        );"""

        self.connection.execute(query)

    def create_user_table(self):
        print("Creating User table")
        query = """
        CREATE TABLE IF NOT EXISTS "User"(
            id INTEGER PRIMARY KEY,
            name TEXT,
            email EMAIL
        );"""

        self.connection.execute(query)

class Model(ABC):
    def __init__(self):
        self.connection = sqlite3.connect("todo.db")
    
    def __del__(self):
        self.connection.commit()
        self.connection.close()

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
    
    @abstractmethod
    def retrieve(self):
        pass

class ToDo(Model):
    TABLENAME = "Todo"

    def __init__(self):
        super().__init__()
        self.connection.row_factory = sqlite3.Row

    def __del__(self):
        return super().__del__()

    def create(self, req):
        super().create()
        query = f"INSERT INTO {self.TABLENAME} "\
                f"(title, description) "\
                f"""VALUES ("{req['title']}","{req['description']}")"""
        self.connection.execute(query)

    def update(self, req):
        super().update()
        query = f'UPDATE {self.TABLENAME} '\
                f'SET title="{req["title"]}", description="{req["description"]}") '\
                f'WHERE id="{req["id"]}"'

        self.connection.execute(query)
    
    def delete(self, req):
        super().delete()
        query = f'DELETE FROM {self.TABLENAME} '\
                f'WHERE id="{req["id"]}"'

        result = self.connection.execute(query)
        return result

    def retrieve(self):
        super().retrieve()
        query = f'SELECT * FROM {self.TABLENAME}'

        result_set = self.connection.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]

        return result