import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

def Translate(word):
    cursor = con.cursor()
    word = word.lower()
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word)
    results = cursor.fetchall()

    print(results)

Translate('HOT')