import os

from flask import (Flask,
                   render_template,
                   redirect,
                   request,
                   flash,
                   session)

from model import (User,
                   connect_to_db)

# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")

# JS_TESTING_MODE = False

# If you use an undefined variable in Jinja2, it raises an error.
# app.jinja_env.undefined = StrictUndefined

# app.secret_key = secret_key.flask_secret_key


# @app.before_request
# def add_tests():
#     g.jasmine_tests = JS_TESTING_MODE

@app.route("/", methods=["GET"])
def index():

    return render_template("sign-in.html")


@app.route('/landing_pg')
def show_landing_pg():
    """Homepage"""

    if "logged_in" in session:
        return render_template("landing_pg.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route("/login", methods=["POST"])
def login_process():

    password = request.form.get("password")
    username = "guest"

    if password:
        guest_password = User.query.filter(User.password == password).first()

        if guest_password.password != password:
            flash("Incorrect password.")
            return redirect("/")

        else:
            session["logged_in"] = username
            flash("Logged in.")
            return redirect("/landing_pg")


@app.route("/logout")
def process_logout():
    """Log user out."""

    del session["logged_in"]

    flash("Logged out.")

    return redirect("/")


@app.route('/resume')
def resume():
    """Resume page"""

    if "logged_in" in session:
        return render_template("resume.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route('/contact')
def contact():
    """Contact page"""

    if "logged_in" in session:
        return render_template("contact.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route('/sfk')
def sfk():
    """Sequoia ForestKeeper page"""

    if "logged_in" in session:
        return render_template("sfk.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route('/melnea')
def melnea():
    """CRWA Melnea Cass Blvd page"""

    if "logged_in" in session:
        return render_template("melnea.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route('/spawning_crwa')
def spawning_crwa():
    """Available spawning area in Charles River page"""

    if "logged_in" in session:
        return render_template("spawning_crwa.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route('/ne_watershed')
def ne_watershed():
    """Patagonia project of New England Watersheds page"""

    if "logged_in" in session:
        return render_template("ne_watershed.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route('/klamath')
def klamath():
    """Klamath River Mussels page"""

    if "logged_in" in session:
        return render_template("klamath.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route('/tir_salmon')
def tir_salmon():
    """Thermal Infered Imaging page"""

    if "logged_in" in session:
        return render_template("TIR_salmon.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route('/birds')
def birds():
    """Tell me about the birds project page"""

    if "logged_in" in session:
        return render_template("birds.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route('/srf')
def srf():
    """Salmonid Restoration Federation (SRF) page"""

    if "logged_in" in session:
        return render_template("srf.html")
    else:
        flash("Incorrect password.")
        return redirect("/login")


@app.route("/error")
def error():
    raise Exception("Error!")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    # app.debug = True
    # app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    # DEBUG_TB_INTERCEPT_REDIRECTS = False
    # import sys
    # if sys.argv[-1] == "jstest":
    #     JS_TESTING_MODE = True

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    connect_to_db(app, os.environ.get("DATABASE_URL"))

    # app.run(host='0.0.0.0')

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
