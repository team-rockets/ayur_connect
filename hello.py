import flask


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/doc_auth')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('op.html')


if __name__ == '__main__':
    APP.debug=True
    APP.run()
s