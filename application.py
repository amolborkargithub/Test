from flask import Flask
from osgeo import gdal
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Updated World!"

if __name__ == '__main__':
    app.run()
