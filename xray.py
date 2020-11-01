import os
from flask import Flask, render_template, request
import keras
import cv2
import pyimgur

app = Flask(__name__)
<<<<<<< HEAD
UPLOAD_FOLDER = "../Ideathon/static"
CATEGORIES = ["COVID POSITIVE", "COVID NEGATIVE"]
CLIENT_ID = "cdb00d6daa103d1"
dashes = "----"
=======
UPLOAD_FOLDER = "../Static"
CATEGORIES = ["Covid Positive", "Covid Negative"]
>>>>>>> 701dfda1dbccda05232fd6a39a87b576f3b24b6e


def prepare(filepath):
    IMG_SIZE = 244
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    p = new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    return p


@app.route("/", methods=["GET", "POST"])
def upload_predict():
<<<<<<< HEAD
    model = keras.models.load_model(
        "../Ideathon/Model/King.h5")
=======
    model = keras.models.load_model("../Model/King.h5")
>>>>>>> 701dfda1dbccda05232fd6a39a87b576f3b24b6e
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(
                UPLOAD_FOLDER,
                image_file.filename,
            )
            image_file.save(image_location)
            p = model.predict([prepare(image_location)])
            return render_template("index.html", prediction=dashes+CATEGORIES[int(p[0, 0])]+dashes)
    return render_template("index.html", prediction="-------RESULTS-------")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
