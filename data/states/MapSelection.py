import random

import pygame as pg
import os

import data.persist_literals as pl
from data.states.statemachine.GameState import GameState


class MapSelection(GameState):
    def __init__(self, unlocked_maps=None):
        super().__init__()
        self._maps = []
        self._parse_maps()
        if unlocked_maps is None:
            unlocked_maps = []
        self.unlocked_maps = unlocked_maps

    def startup(self, persistent):
        if pl.new_unlocked_maps in persistent:
            self._unlock_maps(persistent[pl.new_unlocked_maps])
        self.text = f"Map Selection. Press 1-{len(self.unlocked_maps)}" \
                    f"for gameplay or M-menu."
        if __debug__:
            print(self.unlocked_maps)
        super().startup(persistent)

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)

    def unlock_map(self, map_):
        self._unlock_maps([map_])

    def unlock_random_map(self):
        available_maps = self.get_locked_maps()
        if available_maps:
            selected = random.choice(available_maps)
            self.unlock_map(selected)

    def _unlock_maps(self, new_maps):
        for m in new_maps:
            if m not in self.unlocked_maps:
                self.unlocked_maps.append(m)

    def get_locked_maps(self):
        return [m['name'] for m in self._maps if m['name'] not in self.unlocked_maps]

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
                    m['free'].append([True if c == '_' else False for c in line])
            self._maps.append(m)
        self._maps.sort(key=lambda map_dict: map_dict['name'])

    def get_map_names(self):
        return [m['name'] for m in self._maps]
