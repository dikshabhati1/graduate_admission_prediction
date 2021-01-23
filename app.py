from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('graduate_admission.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        GRE_Score = int(request.form['GRE_Score'])
        TOEFL_Score=int(request.form['TOEFL_Score'])
        University_Rating=int(request.form['University_Rating'])
        SOP=float(request.form['SOP'])
        LOR=float(request.form['LOR'])
        CGPA=float(request.form['CGPA'])
        Research=int(request.form['Research'])
       
        prediction=model.predict([[GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_text="Sorry you cannot take admission")
        else:
            return render_template('index.html',prediction_text="Your Chance of Admission is {} %".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run()