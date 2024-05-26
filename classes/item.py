import pyodbc

class Item:
    def __init__(self, item_id, user_id, item_name, description, start_price, start_datetime, end_datetime):
        self.item_id = item_id
        self.user_id = user_id
        self.item_name = item_name
        self.description = description
        self.start_price = start_price
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    @staticmethod
    def add(cursor, user_id, item_name, description, start_price, start_datetime, end_datetime):
        cursor.execute("INSERT INTO Items (UserID, ItemName, Description, StartPrice, StartDateTime, EndDateTime) VALUES (?, ?, ?, ?, ?, ?)",
                       (user_id, item_name, description, start_price, start_datetime, end_datetime))
        cursor.commit()

    @staticmethod
    def delete(cursor, item_id):
        cursor.execute("DELETE FROM Items WHERE ItemID = ?", (item_id,))
        cursor.commit()

    @staticmethod
    def update_description(cursor, item_id, new_description):
        cursor.execute("UPDATE Items SET Description = ? WHERE ItemID = ?", (new_description, item_id))
        cursor.commit()

    @staticmethod
    def get_item_by_id(cursor, item_id):
        cursor.execute("SELECT * FROM Items WHERE ItemID = ?", (item_id,))
        return cursor.fetchone()

    @staticmethod
    def get_all_items(cursor):
        cursor.execute("SELECT * FROM Items")
        return cursor.fetchall()

    @staticmethod
    def filter_items_by_category(cursor, category):
        cursor.execute("SELECT * FROM Items WHERE Category = ?", (category,))
        return cursor.fetchall()
