import pyodbc

class User:
    def __init__(self, user_id, username, password_hash, email):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.email = email

    @staticmethod
    def login(cursor, username, password):
        cursor.execute(
            "SELECT UserID, Username, PasswordHash, Email FROM Users WHERE Username = ? AND PasswordHash = ?",
            (username, password))
        user_row = cursor.fetchone()
        if user_row:
            user_id, username, password_hash, email = user_row
            return User(user_id, username, password_hash, email)
        else:
            return None

    @staticmethod
    def add(cursor, username, password_hash, email):
        cursor.execute("INSERT INTO Users (Username, PasswordHash, Email) VALUES (?, ?, ?)", (username, password_hash, email))
        cursor.commit()

    @staticmethod
    def delete(cursor, user_id):
        cursor.execute("DELETE FROM Users WHERE UserID = ?", (user_id,))
        cursor.commit()

    @staticmethod
    def update_email(cursor, user_id, new_email):
        cursor.execute("UPDATE Users SET Email = ? WHERE UserID = ?", (new_email, user_id))
        cursor.commit()

    @staticmethod
    def get_user_by_id(cursor, user_id):
        cursor.execute("SELECT * FROM Users WHERE UserID = ?", (user_id,))
        return cursor.fetchone()

    @staticmethod
    def get_all_users(cursor):
        cursor.execute("SELECT * FROM Users")
        return cursor.fetchall()

    @staticmethod
    def validate_login(cursor, username, password_hash):
        cursor.execute("SELECT * FROM Users WHERE Username = ? AND PasswordHash = ?", (username, password_hash))
        return cursor.fetchone()
