import numpy as np


class Agent:
    """
    Given an environment state, choose an action, and learn from the reward
    """

    def __init__(self, env):
        self.env = environment
        self.board = np.zeros(env.board)
        self.player_vals = 1
        self.enemy_cals = 2

    def _get_x_y_coord(self, position):
        """
        Given a tuple, return the x and y coordinates
        """
        return position[0], position[1]

    def _set_board(self, players, enemies):
        """
        Set our np matrix using agent and enemy positions
        """
        board = self.board.copy()
        player_position = player.get_position()
        player_x, player_y = self._get_x_y_coord(player_position)
        board[player_y][player_x] = 1

        for enemy in enemies:
            enemy_position = enemy.get_position()
            enemy_x, enemy_y = self._get_x_y_coord(enemy_position)
            board[enemy_x][enemy_y] = 2

        return board

    def agent_move(self, player_position, enemy_positions):