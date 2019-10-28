from flask import Flask

app = Flask(__name__)
# CORS(app) #Prevents CORS errors


@app.route('/app')
def index():
    return 'The Flask app works!'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
