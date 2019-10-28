#!/home/ubuntu/simple-web-app/venv/bin/python3
import pandas as pd

from flask import Flask

app = Flask(__name__)
# CORS(app) #Prevents CORS errors


# Read the Pokemon dataset
pokemon_df = pd.read_csv('pokemon.csv')


@app.route('/app')
def index():
    html = """
    <h2>The Flask app works!</h2>
    Here is the Pokemon <a href='/app/pokemon'>app</a>.
    """
    return html


@app.route('/app/pokemon')
def pokemon_empty():
    return '<h2>Type the Pokemon name after the slash in the address bar.</h2>'


@app.route('/app/pokemon/<pokemon_name>', methods=['GET'])
def get_pokemon(pokemon_name):
    logical = pokemon_df.name.apply(lambda x: x.lower()) == pokemon_name.lower()
    return pokemon_df[logical].to_json()


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
