import sqlite3
import enviaremail

DB_NAME='bdecommerce.s3db'

def conexion():
    conn=sqlite3.connect(DB_NAME)
    return conn

def adicionar_registros(nombre,apellido,usuario,p1):
    try:
        db=conexion()
        cursor=db.cursor()
        sql='INSERT INTO usuario(nombre,apellido,usuario,passwd,cod_verificacion,verificado,id_rol) VALUES(?,?,?,?,?,?,?)'
        cursor.execute(sql,[nombre,apellido,usuario,p1,'V-10001',False,1])
        db.commit()
        enviaremail.enviar_email(usuario,'MT-55555')
        return True
    except:
        return False

      