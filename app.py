from flask import Flask, request, jsonify, render_template
from game import Game

app = Flask(__name__)
game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    data = request.json
    if data.get('load_game'):
        game.load_game()
    else:
        player_name = data.get('player_name')
        game.start_new_game(player_name)
    return jsonify(game.get_game_state())

@app.route('/action', methods=['POST'])
def process_action():
    action = request.json.get('action')
    result = game.process_action(action)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
