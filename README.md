# RL-test
Reinforcement Learning Test

To run this project follow follwing steps.

**build docker container**
```
sudo docker build --tag  rltest .
```

**run docker container**
```
sudo docker run -d -p 5000:5000 rltest
```
**open this link** http://127.0.0.1:5000/run_step/step/ replace step with -1 or 1. 

It will return a json response with state (current location) and a reward

To run example.py use this command.

```
 sudo docker run rltest python3 example.py
```
output: [-0.32591976] 0.674080237694725
