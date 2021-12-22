import psycopg2
import datetime
import time

def add_Nachricht(name, email, betreff, text):
  database_ready = False
  while not database_ready:
    db = None
    try:
      db = psycopg2.connect(
        host="XXX",
        user="XXX",
        password="XXX",
        database="XXX"
      )
      database_ready = True
      print("Db is ready")
    except:
      print("DB is not ready yet")
      time.sleep(2)

  cursor = db.cursor()
  CurrentTime = datetime.datetime.now()

  sql = ("INSERT INTO nachrichten (Name, EMail, Betreff, Text, Zeit) VALUES (%s, %s, %s, %s, %s);")
  cursor.execute(sql, (name, email, betreff, text, CurrentTime))
  db.commit()
  cursor.close()
  db.close()