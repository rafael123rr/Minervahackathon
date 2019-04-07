from flask import Flask
from mongodb import api_wrapper

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route('/img/<path>/<name>')
def main(path, name):
    api_wrapper(name, path)
    return True

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
