from flask import Flask, render_template, url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/politicas')
def politicas():
    return render_template('politicas.html')


@app.route('/usuarios')
def menu_user():
    return render_template('usuarios.html')

@app.route('/productos')
def menu_productos():
    return render_template('productos.html')

@app.route('/carrito')
def menu_carrito():
    return render_template('carrito.html')

@app.route('/deseos')
def menu_deseos():
    return render_template('deseos.html')

@app.route('/gestion')
def menu_gestion():
    return render_template('gestionproducto.html')



if  __name__=='__main__':
     app.run(debug=True)  