from flask import Flask, request, jsonify, render_template, session
from game import Game

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key
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
        player_name = data.get('player_name', 'Player')
        game.start_new_game(player_name)
    session['game_started'] = True
    return jsonify(game.get_game_state())

@app.route('/action', methods=['POST'])
def process_action():
    if not session.get('game_started'):
        return jsonify({"error": "Game not started. Please start a new game or load a saved game."}), 400
    
    action = request.json.get('action')
    result = game.process_action(action)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
