import pygame as pg
from pygame.sprite import Sprite

class Skudd(Sprite):
    """en klasse til å styre skuddene som blit skutt av skipet"""

    def __init__(self, ai_spill):
        """skaper et skudd objekt på skipets nåværende posisjon"""
        super().__init__()
        self.skjerm = ai_spill.skjerm
        self.settings = ai_spill.settings
        self.farge = self.settings.skudd_farge

        # skaper et skudd rect på (0, 0) og setter korrekt posisjon
        self.rect = pg.Rect(0, 0, self.settings.skudd_bredde,
            self.settings.skudd_hoyde)
        self.rect.midtop = ai_spill.skip.rect.midtop

        # lagre skuddets posisjon som en float
        self.y = float(self.rect.y)

    def oppdatere(self):
        """beveger skuddet opp skjermen"""
        # oppdater skuddets posisjon
        self.y -= self.settings.skudd_fart
        # oppdater rect posisjonen
        self.rect.y = self.y

    def tegn_skudd(self):
        """tegn skuddet på skjermen"""
        pg.draw.rect(self.skjerm, self.farge, self.rect)