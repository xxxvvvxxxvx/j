import sqlite3

db=sqlite3.connect('test.db')



db.execute(""" CREATE TABLE IF NOT EXISTS darbinieki
           (id    INTEGER  PRIMARY KEY  NOT NULL,
           vards   TEXT  NOT NULL,
           alga    REAL,
           piezimes  CHAR(50)
           )
           """)

db.execute(""" INSERT INTO darbinieki
           (id,vards,alga,piezimes)
           VALUES(1,"Anna",980.50,"Ekonomiskas")
           """)

db.commit()


dati=db.execute("""SELECT*FROM darbinieki
                WHERE id=]
               """)
rezultats=dati.fetcha
print(rezultats)

db.execute(
"""
CREATE TABLE IF NOT EXISTING
(id  INTEGER  PRIMARY KEY  AUTOINCREMENT  NOT NULL,
pceturksnis REAL,
oceturksnis REAL,
tceturksnis REAL,
cceturksnis REAL
)
"""
)
p_ceturksnis=Input('Ievadi pirmā ceturksņa prēmiju')
o_ceturksnis=Input('Ievadi otrā ceturksņa prēmiju')
t_ceturksnis=Input('Ievadi trešā ceturksņa prēmiju')
c_ceturksnis=Input('Ievadi ceturtā ceturksņa prēmiju')
db.execute(
"""
INSERT INTO premijas
(pceturksnis, oceturksnis, tceturksnis, cceturksnis)
VALUES[:'pceturksnis,':'p_ceturksnis','oceturksnis':o_ceturksnis,'tceturksnis':t_ceturknis,'cceturksnis':c_ceturksnis ]
"""
)
db.commit()
dati =db.execute("""SELECT*FROM premijas
                 WHERE id=1
                 """)

dati = db.execute(""" SELECT * FROM darbinieki
                  JOIN premijas
                  ON darbinieki.id = premijas.id
                  """)

rezultats =dati.fetchall()
print(rezultats)


for rinda in rezultats:
  print("ID:", rinda[0])
  print("Vārds:"rinda[1])
  print("Alga:"rinda[2])