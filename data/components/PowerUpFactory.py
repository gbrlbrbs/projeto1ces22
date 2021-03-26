import random
from data.components.PowerUp import PowerUp
from data.components.TimerThread import TimerThread


class PowerUpFactory:
    """
    Class to control the power-up creation
    """

    def __init__(self, interval, items, snake_positions):
        """
        Initializes the PowerUpFactory object

        :param interval: time (in seconds) to call create method]
        :param items: dict that contains the possible power-ups with different powers and probabilities
        :param snake_positions: follows snake's positions
        """
        self.interval = interval
        self.dict = items
        self.timer = TimerThread(self.interval, function=self.maybe_create_powerup,
                                 args=snake_positions)
        self.collectable_powerups = []

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def maybe_create_powerup(self, snake_positions):
        """
        Simplified creation method
        """
        k = random.random()
        if __debug__:
            print("factory running")
        if k > 0.5:
            print("entered")
            self.collectable_powerups.append(PowerUp())
            end = len(self.collectable_powerups) - 1
            self.collectable_powerups[end].randomize_position(snake_positions)

    def get_positions(self):
        """
        Method to get collectable power-up positions
        :return: list with power-up coordinates
        """
        return [p.position for p in self.collectable_powerups]
