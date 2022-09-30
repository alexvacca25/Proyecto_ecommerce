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

def validacion_login(usu):
    
    try:
        db=conexion()
        cursor=db.cursor()
        sql='SELECT * FROM usuario WHERE usuario=?'
        cursor.execute(sql,[usu])
        resultado=cursor.fetchone()
        datos=[
            {
                'id':resultado[0],
                'nombre':resultado[1],
                'apellido':resultado[2],
                'usuario':resultado[3],
                'passwd':resultado[4],
                'codverificacion':resultado[5],
                'verificado':resultado[6],
                'rol':resultado[7]
            }
                ]
        return datos
    except:
        return False   


def activar_cuenta(usu,codver):
    try:
        db=conexion()
        cursor=db.cursor()
        sql='UPDATE usuario SET verificado=1 WHERE usuario=? AND cod_verificacion=?'
        cursor.execute(sql,[usu,codver])
        db.commit()
        return True      
    except:
        return False