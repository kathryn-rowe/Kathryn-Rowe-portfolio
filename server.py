import os

from flask import (Flask,
                   redirect,
                   render_template)

from model import User, connect_to_db, db

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


@app.route('/')
def index():
    """Homepage"""

    return render_template("landing_pg.html")


@app.route("/login", methods=["GET"])
def show_login():

    return render_template("sign_in.html")


@app.route("/login", methods=["POST"])
def login_process():

    username = request.form.get("username")
    password = request.form.get("password")

    emails = User.query.filter(User.email == username).first()

    if emails is None:
        flash("No such email address. Please register")
        return redirect('/register')

    elif emails.password != password:
        flash("Incorrect password.")
        return redirect("/login")
    else:
        session["logged_in"] = username
        user_id = emails.user_id
        flash("Logged in.")
        return redirect("/user_info/" + str(user_id))


@app.route("/logout")
def process_logout():
    """Log user out."""

    del session["logged_in"]
    flash("Logged out.")
    return redirect("/")


@app.route('/resume')
def resume():
    """Resume page"""

    return render_template("resume.html")


@app.route('/contact')
def contact():
    """Contact page"""

    return render_template("contact.html")


@app.route('/sfk')
def sfk():
    """Sequoia ForestKeeper page"""

    return render_template("sfk.html")


@app.route('/melnea')
def melnea():
    """CRWA Melnea Cass Blvd page"""

    return render_template("melnea.html")


@app.route('/spawning_crwa')
def spawning_crwa():
    """Available spawning area in Charles River page"""

    return render_template("spawning_crwa.html")


@app.route('/ne_watershed')
def ne_watershed():
    """Patagonia project of New England Watersheds page"""

    return render_template("ne_watershed.html")


@app.route('/klamath')
def klamath():
    """Klamath River Mussels page"""

    return render_template("klamath.html")


@app.route('/tir_salmon')
def tir_salmon():
    """Thermal Infered Imaging page"""

    return render_template("TIR_salmon.html")


@app.route('/birds')
def birds():
    """Tell me about the birds project page"""

    return render_template("birds.html")


@app.route('/srf')
def srf():
    """Salmonid Restoration Federation (SRF) page"""

    return render_template("srf.html")


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

    # import sys
    # if sys.argv[-1] == "jstest":
    #     JS_TESTING_MODE = True

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
