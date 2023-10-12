from flask import flash, redirect, request, session, render_template, jsonify
from flask_app.models.bandas import Banda
from flask_app.models.usuario import Usuario

from flask_app import app

@app.route('/procesar_banda', methods=["POST"])
def procesar_banda():
    print(request.form)

    errores = Banda.validar_banda(request.form)
    if len(errores) > 0:
        for error in errores:
            flash(error, "error")
        return redirect("/")

    data = {
        'nombre': request.form["nombre"],
        'genero': request.form["genero"],
        'lugar_creacion': request.form["lugar_creacion"],
        'usuario_id': session['usuario_id']

    }
    print(data)
    id = Banda.save_band(data)
    print(id)
    flash( "Banda añadida", "success")

    return redirect("/")

@app.route('/nuevo')
def nuevo():
    if not session.get('usuario_id'):
        flash("No estás logeado!!!!", "error")
        return redirect("/login")

    user_in_session = Usuario.get(session['usuario_id'])
    
    return render_template('nueva_banda.html', user_in_session=user_in_session)


@app.route('/mis_bandas/<id>')
def mis_bandas(id):
    print('HHHHHHHH')
    user_in_session= Banda.get_user_with_bands(session['usuario_id'])
    print(user_in_session.nombre)
    return render_template('mis_bandas.html', user_in_session=user_in_session)


@app.route('/editar/<id>')
def editar(id):
    user_in_session = Usuario.get(session['usuario_id'])
    banda = Banda.get_band(id)
    return render_template('editar_banda.html', banda=banda, user_in_session=user_in_session)

@app.route('/procesar_banda_editar/<id>', methods=["POST"])
def procesar_banda_editar(id):
    print(request.form)

    errores = Banda.validar_banda(request.form)
    if len(errores) > 0:
        for error in errores:
            flash(error, "error")
        return redirect("/")
    banda = Banda.get_band(id)

    banda.nombre = request.form['nombre']
    banda.genero = request.form['genero']
    banda.lugar_creacion = request.form['lugar_creacion']

    banda.update_band()
    
    flash( "Banda editada", "success")

    return redirect("/")


@app.route('/eliminar/<id>')
def eliminar(id):
    Banda.eliminar_banda(id)
    return redirect('/')



