from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods = ['GET','POST'])

def classify_image():
    image_data = request.form['image_data']

    responce = jsonify(util.classify_image(image_data))

    responce.headers.add('Access-Control-Allow-origin','*')

    return responce

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)


def util():
    return None