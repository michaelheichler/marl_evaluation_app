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

frameworks = [
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
environments = [{'title': env} for env in gym.envs.registry.all()]
policies=[{'policy': 'PPO'}, {'policy': 'F2P'}, {'policy': 'SP'}]
algorithms=[{'algorithm': 'A2C'}, {'algorithm': 'PPO'}, {'algorithm': 'SAC'}, {'algorithm': 'F2P'}]

# Routes
@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'Hello World!'})

@app.route('/frameworks', methods=['GET'])
def all_frameworks():
    return jsonify({
        'status': 'success',
        'frameworks': frameworks,        
    })

@app.route('/environments', methods=['GET'])
def all_environments():
    return jsonify({
        'status': 'success',
        'environments': environments,        
    })

@app.route('/policies', methods=['GET'])
def all_policies():
    return jsonify({
        'status': 'success',
        'policies': policies,
    })

@app.route('/algorithms', methods=['GET'])
def all_algorithms():
    return jsonify({
        'status': 'success',
        'algorithms': algorithms,
    })

@app.route('/environments/select', methods=['POST'])
def initialize_environment():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        response_object['message'] = 'Environment Selected!'    
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()