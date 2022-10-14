from flask import Flask, jsonify, request
from flask_cors import CORS

# Configuration (Debug Mode on)
DEBUG = True

# Initiate the Flask App
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# List of Environment Variables
import gym
import pettingzoo
import ray

options = [
    {
        'title': 'Gym',
        'version': gym.__version__
    }, 
    {
        'title': 'PettingZoo', 
        'version': pettingzoo.__version__
    }, 
    {
        'title': 'Ray', 
        'version': ray.__version__
    }
]
options1=[{'policy': 'PPO'}, {'policy': 'F2P'}, {'policy': 'SP'}]
options2=[{'algorithm': 'A2C'}, {'algorithm': 'PPO'}, {'algorithm': 'SAC'}, {'algorithm': 'F2P'}]

# Routes
@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'Hello World!'})

@app.route('/environments', methods=['GET'])
def all_environments():
    return jsonify({
        'status': 'success',
        'environments': options,
        #'policy' : options1,
        #'algorithm' : options2
    })

@app.route('/environments/select', methods=['POST'])
def initialize_environment():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        env = gym.make(post_data)
        env.reset()
        response_object[message] = 'Environment Initialized'

    return env


if __name__ == '__main__':
    app.run()