import pandas as pd
from flask import Flask, Response

app = Flask(__name__)

#Load the data
data = pd.read_csv('../input/test.csv', header=0)

@app.route('/reverse')
def data_reverse():

    reversed_data = pd.DataFrame(data, columns=['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
    reversed_data = reversed_data[reversed_data.columns[::-1]]
    print(reversed_data.to_string())

    return Response(reversed_data.to_string(), mimetype='text/plain')

@app.route('/split')
def data_split():
    
    splitted_data = pd.DataFrame(data, columns=['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
    splitted_data = splitted_data[splitted_data.columns[::2]]
    print(splitted_data.to_string())
    splitted_data.to_csv('../output/splitted_data.csv', index = False)

    return Response("File saved to 'output' folder!", mimetype='text/plain')

if __name__ == '__main__':
  app.run(debug=False)
