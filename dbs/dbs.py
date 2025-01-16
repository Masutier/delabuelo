import sqlite3 as sql3

def db_conn():
    conn = sql3.connect('dbs/empaacount.db')
    conn.row_factory = sql3.Row
    return conn


def recordDb(sqlquery):
    try:
        conn = db_conn()
        conn.execute("INSERT INTO Sales (id, customer, transac_code, product_id, sale_quantity, sale_price, total_sale) VALUES (?, ?, ?, ?, ?, ?)", sqlquery)
        conn.commit()
        conn.close()
    except:
        sqlQuery = """ CREATE TABLE Sales (id, customer, transac_code, product_id, sale_quantity, sale_price, total_sale)"""
        conn = db_conn()
        conn.execute(sqlQuery)
        conn.commit()
        conn.execute("INSERT INTO Sales (id, customer, transac_code, product_id, sale_quantity, sale_price, total_sale) VALUES (?, ?, ?, ?, ?, ?)", sqlquery)
        conn.commit()
        conn.close()
        sales=[]

    return users


def checkProductDb(csvFile):

    create_table = '''CREATE TABLE products_producto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL,
        categoria TEXT NOT NULL,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        mesure TEXT NOT NULL,
        quantity_package INTEGER NOT NULL,
        quantity_un INTEGER NOT NULL,
        cost_package INTEGER NOT NULL,
        cost_un INTEGER NOT NULL,
        sale_price INTEGER NOT NULL,
        image TEXT NOT NULL,
        date_created DATETIME NOT NULL,
        date_modify DATETIME NOT NULL);
        '''
    
    try:
        conn = db_conn()
        conn.execute("INSERT INTO products_producto (id, customer, transac_code, product_id, sale_quantity, sale_price, total_sale) VALUES (?, ?, ?, ?, ?, ?)", sqlquery)
        conn.commit()
        conn.close()
    except:
        conn = db_conn()
        conn.execute(create_table)
        file = open(csvFile)



        conn.commit()
        conn.execute("INSERT INTO products_producto (id, customer, transac_code, product_id, sale_quantity, sale_price, total_sale) VALUES (?, ?, ?, ?, ?, ?)", sqlquery)
        conn.commit()
        conn.close()
        sales=[]

    return users







