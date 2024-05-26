import pyodbc

class Bid:
    def __init__(self, bid_id, item_id, user_id, bid_amount, bid_datetime):
        self.bid_id = bid_id
        self.item_id = item_id
        self.user_id = user_id
        self.bid_amount = bid_amount
        self.bid_datetime = bid_datetime

    @staticmethod
    def add(cursor, item_id, user_id, bid_amount, bid_datetime):
        cursor.execute("INSERT INTO Bids (ItemID, UserID, BidAmount, BidDateTime) VALUES (?, ?, ?, ?)",
                       (item_id, user_id, bid_amount, bid_datetime))
        cursor.commit()

    @staticmethod
    def delete(cursor, bid_id):
        cursor.execute("DELETE FROM Bids WHERE BidID = ?", (bid_id,))
        cursor.commit()

    @staticmethod
    def get_bids_by_item(cursor, item_id):
        cursor.execute("SELECT * FROM Bids WHERE ItemID = ?", (item_id,))
        return cursor.fetchall()

    @staticmethod
    def get_bids_by_user(cursor, user_id):
        cursor.execute("SELECT * FROM Bids WHERE UserID = ?", (user_id,))
        return cursor.fetchall()

    @staticmethod
    def get_highest_bid(cursor, item_id):
        cursor.execute("SELECT TOP 1 * FROM Bids WHERE ItemID = ? ORDER BY BidAmount DESC", (item_id,))
        return cursor.fetchone()
