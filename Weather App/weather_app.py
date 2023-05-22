from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        weather_data = get_weather_data(location)
        return render_template('index.html', weather_data=weather_data)
    return render_template('index.html')

def get_weather_data(location):
    api_key = '48fc419797bd4227b8b143809232105'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == '__main__':
    app.run(debug=True)