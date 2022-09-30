from dataclasses import replace
from datetime import datetime
import sqlite3

from flask import flash
import enviaremail

DB_NAME='bdecommerce.s3db'

def conexion():
    conn=sqlite3.connect(DB_NAME)
    return conn

def adicionar_registros(nombre,apellido,usuario,p1):
    cod_ver=str(datetime.now())
    cod_ver=cod_ver.replace("-","")
    cod_ver=cod_ver.replace(" ","")
    cod_ver=cod_ver.replace(":","")
    cod_ver=cod_ver.replace(".","")
    flash(cod_ver)
    try:
        db=conexion()
        cursor=db.cursor()
        sql='INSERT INTO usuario(nombre,apellido,usuario,passwd,cod_verificacion,verificado,id_rol) VALUES(?,?,?,?,?,?,?)'
        cursor.execute(sql,[nombre,apellido,usuario,p1,cod_ver,0,1])
        db.commit()
        enviaremail.enviar_email(usuario,cod_ver)
        return True
    except:
        return False

      