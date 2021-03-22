import pygame as pg
import os

import data.persist_literals as pl
from data.states.statemachine.GameState import GameState


class MapSelection(GameState):
    def __init__(self, unlocked_levels=None):
        super().__init__()
        if unlocked_levels is None:
            unlocked_levels = {1}
        self.unlocked_levels = unlocked_levels
        self._maps = []
        self._parse_maps()

    def startup(self, persistent):
        if pl.new_unlocked_levels in persistent:
            self.unlock_levels(persistent[pl.new_unlocked_levels])
        self.text = "Map Selection. Press {} for gameplay or M-menu.".format(self.unlocked_levels)
        super().startup(persistent)

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)

    def unlock_levels(self, new_levels):
        self.unlocked_levels = self.unlocked_levels | new_levels

    def _parse_maps(self, filenames=None, extension='.txt'):
        """
        Parses resource/maps

        :param filenames: a list of files to parse. Example Usage: filenames=["lvl1", "lvl2"]
        :param extension: the extension of the files in resources/maps
        """
        path = os.path.relpath('resources/maps')
        if filenames is None:
            filenames = os.listdir(path)
        else:
            filenames = [(f + extension) for f in filenames]
        for filename in filenames:
            m = {'name': filename[:-len(extension)], 'free': []}
            with open('/'.join([path, filename])) as f:
                for line in f:
                    line = line.replace('\n', '')
                    m['free'].append([True if c is '_' else False for c in line])
            self._maps.append(m)
        self._maps.sort(key=lambda map_dict: map_dict['name'])
