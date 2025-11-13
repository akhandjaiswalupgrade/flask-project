from flask import Blueprint, render_template, request
import database  # importing our db functions

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return render_template('login.html')



@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        mobileno = request.form.get('mobileno', '').strip()

        if name and mobileno:
            database.add_user(name, mobileno)
            return render_template('suceess.html', name=name)

        error = "Please provide both name and mobile number."
        return render_template('register.html', error=error, name=name, mobileno=mobileno), 400

    return render_template('register.html')