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


@app.route('/<port_page>')
def show_work(port_page):
    """Renders different pages of portfolio"""

    return render_template(port_page + ".html")


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
