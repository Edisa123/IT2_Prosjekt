import pygame as pg

class Skip:
    """en klasse til å styre skipet"""
    def __init__(self, ai_spill):
        """laste ned skipet og sette start posisjon på den"""
        self.skjerm = ai_spill.skjerm
        self.skjerm_rect = ai_spill.skjerm.get_rect()

        # laste skipets bilde og få dens rect
        self.image = pg.image.load('images/ship.bmp')