import gym
from gym import spaces
from gym.utils import seeding
import numpy as np


class MoveToBeacon1D(gym.Env):

    """
    ### Description

    This environment is designed to move a pointer on x-axis from range -1 to 1.

    INPUT: 
    seed (int): set random seed

    Example:
    ```
        environment = MoveToBeacon1D()
        state,reward,_,_ = environment.step(-1)

        print(state,reward)
        [-0.32591976] 0.674080237694725

    ```

    ### Action Space

    | Num | Action                 |
    |-----|------------------------|
    | 0   | Push point to the left |
    | 1   | Push point to the right|

    **Note:** point is moved by distance of 0.025 based on the action.

    ### Observation space

    | Num | Observation           | Min  | Max |
    |-----|-----------------------|------|-----|
    | 0   | point position        | -1   | 1   |

    **Note:** If action tries to set state outside this range it is clipped in range -1 to 1.

    ## Starting State

    starting state is assigned by selecting a value from -1 to 1 uniformly.

    ## Reward
    Reward is 1- distance of point from 0.

    """

    metadata = {'render.modes': ['human']}

    def __init__(self, seed=42):
        super(MoveToBeacon1D, self).__init__()

        self._seed(seed)
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(
            low=-1,
            high=1,
            shape=(1,),
        )
        self.state = np.random.uniform(low=-1, high=1, size=(1))
        self.terminal = False
        self.current_step = 0
        self.reward_memory = []

    def step(self, action):
        """ Get new state and reward based on action """
        self.current_step += 1
        action = 2 * action - 1  # convert 0 to -1 and keep 1 as 1
        self.state = np.clip(action * 0.025 + self.state, -1, 1)
        reward = 1 - abs(self.state[0])  # reward is 1 - distance form 0
        self.reward_memory.append(reward)

        return self.state, reward, self.terminal, {}

    def reset(self):
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(
            low=-1,
            high=1,
            shape=(1,)
        )
        self.state = np.random.uniform(low=-1, high=1, size=(1))
        self.terminal = False
        self.current_step = 0
        return self.state

    def render(self, mode="human"):
        return self.state

    def _seed(self, seed=None):
        """ set random seed for recreating results """
        self.np_random, seed = seeding.np_random(seed)
        np.random.seed(seed)
