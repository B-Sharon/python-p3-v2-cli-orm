#database environmnet setup
import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
