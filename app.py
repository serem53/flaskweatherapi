from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weather',methods = ['POST','GET'])
def get_weatherdata():
    url =  'https://api.openweathermap.org/data/2.5/weather'
    params = {
          'q':'nairobi',
           'appid':request.form.get('appid'),
           'units': request.form.get('units')
    }

    response = requests.get(url,params=params)
    data = response.json()  

    return data

if __name__ == '__main__':
   app.run(host='0.0.0.0',port =8000)