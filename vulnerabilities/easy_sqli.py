# Select in Dropdown: SQL Injection
import sqlite3

def get_user_data(username):
    """
    Level: EASY
    Vulnerability: SQL Injection
    Why: Direct string concatenation of user input into a query.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # The classic vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    print(f"Executing: {query}")
    cursor.execute(query)
    return cursor.fetchall()
