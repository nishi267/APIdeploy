import pickle

from flask import Flask,request

from flasgger import Swagger
import pandas as pd

app = Flask(__name__)
Swagger(app)

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"


@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true

    responses:
        200:
            description: The output values

    """
    df_test = pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction = classifier.predict(df_test)

    return str(list(prediction))

if __name__=='__main__':
    app.run()