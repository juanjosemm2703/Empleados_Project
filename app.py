import os
from flask import Flask, render_template, url_for, request, flash, redirect
from forms import LogInForm, FilterForm
from tablas import personas, rol, empleados, administrador, Superadministrador, listaTablaEmpleados, listaTablaAdministradores, Lista, buscar_persona
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)

def sortByDate(elem):
    return datetime.strptime(elem[5], '%d/%m/%Y')

@app.route("/", methods=['GET', 'POST'])
def login():
    form =  LogInForm()
    if form.validate_on_submit():
        personaEncontrada = [persona for persona in personas if persona['correo'] == form.username.data and persona['Contrasena'] == form.password.data ]
        if personaEncontrada:
            user = personaEncontrada[0]['Rol']
            return redirect(url_for('profile', user=user))
        else:
            flash(f"El nombre de usuario o contraseña que ha proporcionado no son correctos. Inténtelo de nuevo.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route("/table/<int:user>")
def table(user):

    form = FilterForm(request.args, meta={"csrf": False})
    if user == 1:
        lista=Lista
    if user == 2:
        lista=listaTablaEmpleados
    if user == 3:
        return(redirect(url_for('profile',user=user)))


    longLista = len(lista)
    
    if user==1:
        form.rol.choices = [(0," --- "),(2,"Administrador"),(3,"Empleado")]
    if user==2:
        form.rol.choices = [(3," Empleados ")]

    if form.validate() and lista:
        listaFiltrada = lista[:]

        nombre=form.name.data.strip()
        if nombre:
            for persona in lista:
                if nombre != persona[0] and nombre != persona[1]:
                    try:
                        listaFiltrada.remove(persona)
                    except Exception as e:
                        continue

        if form.rol.data != 0:
                for persona in lista:
                    if form.rol.data != persona[2]:
                        try:
                            listaFiltrada.remove(persona)
                        except Exception as e:
                            continue

        cargo=form.cargo.data.strip()
        if cargo:
            for persona in lista:
                if cargo != persona[3]:
                    try:
                        listaFiltrada.remove(persona)
                    except Exception as e:
                        continue


        dependencia=form.dependencia.data.strip()
        if dependencia:
            for persona in lista:
                if cargo != persona[3]:
                    try:
                        listaFiltrada.remove(persona)
                    except Exception as e:
                        continue

        if form.date_admission.data:
                if form.date_admission.data == 1:
                    listaFiltrada.sort(key=sortByDate, reverse=True)
                if form.date_admission.data == 2:
                    listaFiltrada.sort(key=sortByDate)


        if len(listaFiltrada) == 0:
            flash("No existe un usuario con estos datos","danger")
            return(redirect(url_for('table',user=user)))
        longLista = len(listaFiltrada)
        return render_template('table.html', user=user, form=form ,len=longLista, lista=listaFiltrada)

    else:
        return render_template('table.html',user=user, form=form, len=longLista, lista=lista)

@app.route("/profile/<int:user>", methods=["GET", "POST"])
def profile(user):
    
    return render_template('profile.html',user=user)

@app.route("/edit/<int:id_userEdit>/<int:user>")
def edit(id_userEdit,user):
    return render_template('edit.html',userEdit=id_userEdit, user=user)

@app.route("/view/<int:id_userEdit>/<int:user>")
def view(id_userEdit,user):
    try:
        usuario = buscar_persona(id_userEdit)
    except Exception as e:
        flash("No existe un usuario con este id")
        return(redirect(url_for('profile',user=user)))
    
    if usuario:
        return render_template('view.html',userEdit=usuario, user=user)
    

@app.route("/newuser/<int:user>")
def newUser(user):
    return render_template('NewUser.html', user=user)

@app.route("/dashboard/<int:user>")
def dashboard(user):
    return render_template('index.html', user=user)

@app.route("/retroalimentacion/<int:id_userEdit>/<int:user>")
def retroalimentacion(id_userEdit, user):
    return render_template('retroalimentacion.html', userEdit=id_userEdit, user=user)

@app.route("/nueva_contraseña/<int:id_userEdit>/<int:user>")
def nueva_contrasena(id_userEdit, user):
    return ("Enviar un correo con una nueva contraseña")

@app.route("/delete/<int:id_userEdit>/<int:user>")
def delete(id_userEdit, user):
    return ("Se elimina a la persona")

@app.route("/ForgotPassword")
def ForgotPassword():
    return render_template('ForgotPassword.html')

# Modulo Principal
if __name__=='__main__':
    app.run(debug=True)