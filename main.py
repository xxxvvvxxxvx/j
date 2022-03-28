import sqlite3 

db = sqlite3.connect('test.db')

db.execute("""
           CREATE TABLE IF NOT EXISTS darbinieki
           (id INTEGER PRIMARY KEY  NOT NULL, 
           vards TEXT   NOT NULL,
           alga REAL,
           piezimes CHAR(50)
           )
           """)

db.execute("""INSERT INTO darbinieki
           (id,vards,alga,piezimes)
           VALUES(1, 'Anna', 900.50, 'ljaljaljalja')
           """)

db.commit()

dati = db.execute("""SELECT * FROM darbinieki
                  WHERE id=1
                  """)

rezultats = dati.fetchall()
print(rezultats)

db.execute(
  """
  CREATE TABLE IF NOT EXISTS
  (id INTEGER PRIMARY KEY AUTOINCREMENT
  pceturksnis REAL,
  oceturksnis REAL,
  tceturksnis REAL,
  cceturksnis REAL,
  )
  
  """
)

print("tt:")

db.execute("""
           INSERT INTO premijas:
           ()
           VALUES(:)
          
           """)

