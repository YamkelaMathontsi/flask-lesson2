from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route("/")
def user():
    return "This is the user page"


@app.route("/verify/<name>")
def verify_page(name):
    if name == "Godwin":
        return redirect(url_for("student", name=name))
    elif name == "Yamkela":
        return redirect(url_for("vistor", name=name))
    else:
        return redirect(url_for("admin", name=name))


@app.route("/student/<name>")
def student(name):
    return "Student Page" % name


@app.route("/admin/<name>")
def admin(name):
    return "Admin page woo" % name


@app.route("/vistor/<name>")
def guest(name):
    return "HEY im a vistor here." % name


@app.route("/payment/<int:sal>")
def payment(sal):
    if sal <= 7000:
        return redirect("https://www.fnb.co.za")


if __name__ == '__main__':
    app.debug = True
    app.run()
