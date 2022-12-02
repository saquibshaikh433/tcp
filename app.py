import pickle 
import pandas as pd 
import numpy as np 
import json
import os 
from flask import Flask, render_template, jsonify, app, url_for, request

app = Flask(__name__)

pkl_path = r"C:\Users\najmus.s\Desktop\Jupyter-notebook\end-2-end-deployment\tcp\saved_model"

model = pickle.load(open(pkl_path + '/' + "model1.pkl","rb" ))
channel_dict = pickle.load(open(pkl_path+"/"+"channel.pkl","rb"))
year_dict = pickle.load(open(pkl_path+"/"+"year.pkl", "rb"))
sc = pickle.load(open(pkl_path+"/"+"sc.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])

def predict():
    df = request.json["data"]
    new = sc.transform(np.array(list(df.values())).reshape(1,-1))
    out = model.predict(new)
    return jsonify(out[0])


@app.route("/prediction", methods=["POST"])
def prediction():
    df = [int(x) for x in request.form.values()]
    print(df)
    input = sc.transform(np.array(df).reshape(1,-1))
    output = model.predict(input)[0]
    return render_template("home.html", show_results="{}".format(int(output)))

if __name__=="__main__":
    app.run(debug=True)

