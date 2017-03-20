"""Bird abundance by observation."""

from jinja2 import StrictUndefined

from flask import (Flask,
                   render_template,
                   request, session,
                   jsonify,
                   g)

from flask_debugtoolbar import DebugToolbarExtension

import secret_key

# from datetime import datetime

app = Flask(__name__)

JS_TESTING_MODE = False

# If you use an undefined variable in Jinja2, it raises an error.
app.jinja_env.undefined = StrictUndefined

app.secret_key = secret_key.flask_secret_key


@app.before_request
def add_tests():
    g.jasmine_tests = JS_TESTING_MODE


@app.route('/')
def index():
    """Homepage"""

    return render_template("landing_pg.html")


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


@app.route('/patagonia')
def patagonia():
    """Patagonia page"""

    return render_template("patagonia.html")


@app.route('/klamath_river')
def klamath_river():
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


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    import sys
    if sys.argv[-1] == "jstest":
        JS_TESTING_MODE = True

    app.run(host='0.0.0.0')
