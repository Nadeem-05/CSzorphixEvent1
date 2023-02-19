from flask import *
from flask_bootstrap import Bootstrap
import pyotp
# configuring flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "APP_SECRET_KEY"
Bootstrap(app)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

check = False
check1 = False
users = []
users.append(User(id=1, username='test', password='test'))


@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/2,147,483,647/")
def Flag():
    return render_template("2,147,483,647.html")

@app.route("/login/security/")
def login_security_ques():
    global check1
    if check1 != True:
        flash("Please login first", "danger")
        return redirect(url_for('login'))
    check1=False
    return render_template("login_security.html")

@app.route("/login/", methods=["POST"])
def login_form():
    global check1
    creds = {"username": "bruh", "password": "bruh@123"}
    username = request.form.get("username")
    password = request.form.get("password")
    user = [x for x in users if x.username == username][0]
    if user and user.password == password:
        flash("The credentials provided are valid", "success")
        check1=True
        return redirect(url_for("login_security"))
    else:
        flash("You have supplied invalid login credentials!", "danger")
        return redirect(url_for("login"))

@app.route("/login/security/", methods=["POST"])
def login_security():
    global check
    creds = {"Catname": "ALEX", "Hometown": "MADURAI","Food":"PIZZA"}
    Catname = request.form.get("Catname")
    Hometown = request.form.get("Hometown")
    Food = request.form.get("Food")
    if Catname.upper() == creds["Catname"] and Hometown.upper() == creds["Hometown"] and Food.upper() == creds["Food"]:
        flash("You have answered the security questions correctly", "success")
        check = True
        return redirect(url_for("login_2fa"))
    else:
        flash("You have answered the security questions incorrectly!", "danger")
        return redirect(url_for("login_security"))

@app.route("/login/2fa/")
def login_2fa():
    global check
    if check != True:
        flash("Please login first", "danger")
        return redirect(url_for('login'))
    check = False
    return render_template("login_2fa.html")

@app.route("/login/2fa/", methods=["POST"])
def login_2fa_form():
    otp = int(request.form.get("otp"))
    if pyotp.TOTP("JBSWY3DPEHPK3PXP").verify(otp):
        flash("The TOTP 2FA token is valid", "success")
        return redirect(url_for("Flag"))
    else:
        flash("You have supplied an invalid 2FA token!", "danger")
        return redirect(url_for("login_2fa"))

@app.route("/")
def index():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()