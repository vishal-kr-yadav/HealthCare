import unicodedata
import sys
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

from flask import Flask ,render_template ,request ,redirect ,url_for
app=Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return name

@app.route('/')
def first():
    return render_template('homepage.html')

@app.route('/second' ,methods = ['POST', 'GET'])
def second():
    if request.method=='POST' :

        #extracting cigratePerDay by using request.form and converting it into string because request.form returns unicode
        cigratePerDay= unicodedata.normalize('NFKD', request.form['cigratePerDay']).encode('ascii', 'ignore')
        weight= unicodedata.normalize('NFKD', request.form['weight']).encode('ascii', 'ignore')
        height= unicodedata.normalize('NFKD', request.form['height']).encode('ascii', 'ignore')
        waterIntakePerDay= unicodedata.normalize('NFKD', request.form['waterIntakePerDay']).encode('ascii', 'ignore')
        exerciseInHoursperDay= unicodedata.normalize('NFKD', request.form['exerciseInHoursperDay']).encode('ascii', 'ignore')

        #converting cigratePerDay it into int due to input format for logisticRegression
        initial=[int(cigratePerDay),int(weight),int(height),int(waterIntakePerDay),int(exerciseInHoursperDay)]
        final = []
        #preparing input data like [[10,65,6,5,1]]
        final.append(initial)
        url = "/home/vishal/Documents/healtCareDataSet.data"
        names = ['cigratePerDay', 'weight', 'height', 'waterIntakePerDay', 'exerciseInHoursperDay', 'healtConditions']
        dataset = pandas.read_csv(url, names=names)
        array = dataset.values
        X = array[:, 0:5]
        Y = array[:, 5]
        lr = LogisticRegression()
        lr.fit(X, Y)
        predictions = lr.predict(final)
        #passing the prediction result to another page
        return redirect(url_for('success',name=predictions))


if __name__=='__main__':
    app.run()


