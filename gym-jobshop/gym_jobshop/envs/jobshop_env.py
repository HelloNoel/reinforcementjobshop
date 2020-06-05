# External module imports
import numpy as np
import gym
from gym import error, spaces, logger, utils
from gym.utils import seeding

# Custom module imports
from gym_jobshop.envs.src import main


class JobShopEnv(gym.Env):
    """
    Description:
        Units of time measurement are steps, periods and episodes.
        1 period = 960 steps
        1 episode = 8000 periods
        The reinforcement learning agent can take an action once every period by using the step() method

    Source:

    Observations:
        Type: Box(low=0, high=np.inf, shape=(6, 6), dtype=np.int_)
        The observation space contains information on the current state of some production metrics.
        It features the amount of orders in each stage of production, filtered by the product type of orders.
        The state is always one array of arrays, containing six arrays, one per product type (1-6). Each array has six
        elements, which contain the amount of orders for the six production steps
        (Order pool | Work center 1 | Work center 2 | Work center 3 | FGI | Shipped goods).
        Example:
        [[   0    0    0    0   11 1381]
         [   0    0    0    0    8 1392]
         [   1    0    0    0   11 1346]
         [   1    0    0    0   14 1306]
         [   1    0    0    0   11 1395]
         [   1    0    0    0   15 1279]]
         The example state above indicates that there are 11 orders of product type 1 inside the finished goods inventory
         and 1381 orders of product type 1 are shipped.
         Product type 3 has one order in Work Center 1 and 1279 orders of product type 6 are shipped.

    Actions:
        Type: Discrete(3)
        Num |   Action
        0   |   Keep capacity
        1   |   Increase capacity
        2   |   Increase capacity

    Reward:
        Reward is the final cost after each episode. It is always a negative number, e.g. -246601

    Starting state:
        All stages of production start with zero orders inside them, thus the starting state is an
        array with six arrays, each consisting of six elements that all have the value 0.

    Episode Termination:
        Episodes end after 8000 periods, there are no other termination conditions.
    """
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # self.seed()
        self.viewer = None
        self.state = self.reset()

        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(6, 6), dtype=np.int_)

    # def seed(self, seed=None):
    #     self.np_random, seed = gym.utils.seeding.np_random(seed)
    #     return [seed]

    def step(self, action):
        """
        Step one period (= 960 simulation steps) ahead.
        :param action: Integer number, must be either 0, 1 or 2. Used to adjust the processing times of
        bottleneck machines. More info at main.py -> adjust_processing_times()
        :return: observation (array of arrays, contains production metrics),
        reward (floating-point number, indicates the cost that accumulated during the period),
        done (boolean value, tells whether to terminate the episode),
        info (diagnostic information for debugging)
        """
        # Verify if action is valid
        assert self.action_space.contains(action), "%r (%s) invalid action" % (action, type(action))
        # Adjust processing times of bottleneck machines (capacity) depending on action
        main.adjust_processing_times(action)
        # Step one period ( = 960 steps) ahead
        for i in range(960):
            main.step_one_step_ahead()
        # Retrieve new state from the environment
        self.state = main.get_current_environment_state()
        observation = np.array(self.state)
        # Obtain cost that accumulated during this period
        reward = main.get_results_from_this_period()

        done = False  # must be True or False. Not used since episodes always run for the full duration
        info = None  # Not used

        return observation, reward, done, info

    def reset(self):
        main.reset()
        self.state = main.get_current_environment_state()

        return np.array(self.state)

    def render(self, mode='human', close=False):
        """
        Render is not supported in this environment.
        :param mode: NOT SUPPORTED
        :param close: NOT SUPPORTED
        :return:
        """
        raise Exception("render() is not supported in this environment.")
