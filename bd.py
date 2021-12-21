import sqlite3

connection = sqlite3.connect("aquarium.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE brand(
    id_brand INTEGER PRIMARY KEY,
    id_manufacturer INTEGER NOT NULL,
    id_wine_type INTEGER NOT NULL,
    Name_b varchar(50) DEFAULT NULL,
	price float(24),
	FOREIGN KEY (id_manufacturer) REFERENCES manufacturer(id_manufacturer)
	

);

""")

#cursor.execute("INSERT INTO wine_type(?, ?, ?)" VALUES ('id_aos','id_tog','id_wm')")


#cursor.execute("INSERT INTO brand VALUES (?, ?, ?)", ('Jamie', 'vbn', 0))

#cursor.execute("INSERT INTO wine_materials VALUES (?, ?, ?)", ('Jamie', 'vbn', 0))
connection.commit()

#row = cursor.execute("SELECT * FROM products").fetchall()
#print(row)