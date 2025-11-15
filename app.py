from flask import Flask, render_template, request, redirect, url_for, session

app=Flask(__name__)

app.secret_key="mysecretkey2805"

@app.route("/",methods=["GET"])
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def islogin():
    user={
        "praveen":"2005"
        }
    uname=request.form.get("username")
    pw=request.form.get("password")
    print(user[uname])
    if uname in user and user[uname]==pw:
        return render_template("after_login.html")
    error="user name or password is doesent match"
    return render_template("login.html",error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)