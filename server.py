import os

from flask import (Flask,
                   render_template)


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

    return render_template("landing_pg.html")


@app.route('/resume')
def resume():
    """Resume page"""

    return render_template("resume.html")


@app.route('/aboutme')
def aboutme():
    """About Me page"""

    return render_template("aboutme.html")


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


@app.route('/invites')
def invites():
    """Wedding Invitation work page"""

    return render_template("invites.html")


@app.route('/volunteer')
def volunteer():
    """volunteer work page"""

    return render_template("volunteer.html")


@app.route('/hobby')
def hobby():
    """hobby work page"""

    return render_template("hobby.html")


@app.route('/impact')
def impact():
    """Impact Hackathon work page"""

    return render_template("impact_hack.html")


@app.route('/coding')
def coding():
    """Different coding projects page"""

    return render_template("coding.html")


@app.route('/aws_demo')
def aws_demo():
    """AWS Deployment blog post"""

    return render_template("aws_demo.html")

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

    # app.run(host='0.0.0.0')

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
