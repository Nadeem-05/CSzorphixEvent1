from flask import Flask,render_template,flash,request,url_for,redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLALCHEMY 
import pyotp
from  flask_login  import LoginManager,login_user,logout_user,login_required,current_user
# configuring flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "APP_SECRET_KEY"
Bootstrap(app)
# creating session  manager
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
#creating database
app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///User.db"
db=SQLAlchemy(app)
@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/2,147,483,647/")
def Flag():
    return render_template("2,147,483,647.html")

@app.route("/login/security/")
@login_required
def login_security_ques():
    return render_template("login_security.html")

@app.route("/login/", methods=["POST"])
def login_form():
    creds = {"username": "bruh", "password": "bruh@123"}
    username = request.form.get("username")
    password = request.form.get("password")
    if username == creds["username"] and password == creds["password"]:
        user=User.query.filter_by(name="bruh")
        login_user(user)
        flash("The credentials provided are valid", "success")
        return redirect(url_for("login_security"))
    else:
        flash("You have supplied invalid login credentials!", "danger")
        return redirect(url_for("login"))

@app.route("/login/security/", methods=["POST"])
@login_required
def login_security():
    creds = {"Catname": "ALEX", "Hometown": "MADURAI","Food":"PIZZA"}
    Catname = request.form.get("Catname")
    Hometown = request.form.get("Hometown")
    Food = request.form.get("Food")
    if Catname.upper() == creds["Catname"] and Hometown.upper() == creds["Hometown"] and Food.upper() == creds["Food"]:
        flash("You have answered the security questions correctly", "success")
        return redirect(url_for("login_2fa"))
    else:
        flash("You have answered the security questions incorrectly!", "danger")
        return redirect(url_for("login_security"))

@app.route("/login/2fa/")
def login_2fa():
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
    return "<h2>This is home page</h2>"
if __name__ == "__main__":
    app.run()
