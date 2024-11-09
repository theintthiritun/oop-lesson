class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table  
    
    def filter(self, condition):
        """
        Filter the table based on a condition function that takes a row and returns True if it should be included.
        """
        return [row for row in self.table if condition(row)]

    def aggregate(self, aggregation_function, aggregation_key):
        """
        Apply an aggregation function (like sum, max) on a specified key.
        """
        values = [row[aggregation_key] for row in self.table if aggregation_key in row]
        return aggregation_function(values)

    def __str__(self):
        return f"Table: {self.table_name}, Rows: {len(self.table)}"


class TableDB:
    def __init__(self):
        self.table_database = []
    
    def insert(self, table):
        """
        Insert a Table object into the database.
        """
        self.table_database.append(table)

    def search(self, table_name):
        """
        Search for a table by its name.
        """
        for table in self.table_database:
            if table.table_name == table_name:
                return table
        return None  

    def __str__(self):
        return f"TableDB with {len(self.table_database)} tables"
