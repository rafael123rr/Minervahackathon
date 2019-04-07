from flask import Flask,request
from mongodb import api_wrapper

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route('/img/<path>/<name>')
def main(path, name):
    api_wrapper(name, path)
    return path


@app.route('/api/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
    return 'file uploaded successfully'
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(port=4996)
