from flask import Flask, jsonify
from MoveToBeacon1D import MoveToBeacon1D

app = Flask(__name__)

environnmet = MoveToBeacon1D()


@app.route('/run_step/<step>/')
def run_step(step):
    step = (int(step)+1)/2  # convert -1 to 0 and keep 1 as 1
    state, reward, _, _ = environnmet.step(step)
    result = {"state": state[0], "reward": reward}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
