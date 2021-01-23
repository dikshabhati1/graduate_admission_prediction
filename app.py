
import pickle
from flask import Flask, render_template, request
from flask_cors import cross_origin

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            GRE_Score = int(request.form['GRE Score'])
            TOEFL_Score = int(request.form['TOEFL Score'])
            University_Rating = int(request.form['University Rating'])
            SOP = float(request.form['SOP'])
            LOR = float(request.form['LOR'])
            CGPA = float(request.form['CGPA'])
            Research = int(request.form['Research'])
            

            filename = 'graduate_admission.pkl'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([[GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=prediction[0])
        except Exception as e:
            print('The Exception message is: ', e)

            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app