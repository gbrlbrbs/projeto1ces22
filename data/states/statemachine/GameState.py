import pygame as pg
import data
import data.state_literals as sl


class GameState(object):
    """
    Parent class for individual game states to inherit from.
    """

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font(None, 24)

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        self.persist = persistent
        if hasattr(self, 'text'):
            self.title = self.font.render(self.text, True, pg.Color("gray50"))
            self.title_rect = self.title.get_rect(center=self.screen_rect.center)

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.

        :return: True if some event was catched, False otherwise.
        """
        state_name = sl.pascal2upper(self.__class__.__name__)
        if event.type == pg.QUIT:
            self.quit = True
            return True
        if event.type == pg.KEYUP:
            key_transitions = data.transitions.get(state_name, 'key')
            for k, (next_state, persist_update, callback, params) in key_transitions:
                if event.key == k:
                    self.next_state = next_state
                    self.persist.update(persist_update)
                    if callback is not None:
                        callback(*params)
                    self.done = True
                    return True
        if event.type == pg.MOUSEBUTTONUP:
            return True
        return False

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame.

        dt: time since last frame
        """
        pass

    def cleanup(self):
        """
        Method to clean things at the end of the state
        """
        pass

    def draw(self, surface):
        """
        Draw everything to the screen.
        """
        raise NotImplementedError
