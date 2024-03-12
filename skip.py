import pygame as pg

class Skip:
    """en klasse til å styre skipet"""
    def __init__(self, ai_spill):
        """laste ned skipet og sette start posisjon på den"""
        self.skjerm = ai_spill.skjerm
        self.settinger = ai_spill.settinger
        self.skjerm_rect = ai_spill.skjerm.get_rect()

        # laste skipets bilde og få dens rect
        self.image = pg.image.load('images/ship.bmp') # KOMME TILBAKE TIL DET HER!!!
        self.rect = self.image.get_rect()

        # start hvert nye skip på bunden og midten av skjermen
        self.rect.midbottom = self.skjerm_rect.midbottom

        # beholde en float for skipets horisontale posisjon
        self.x = float(self.rect.x)

    def blitme(self):
        """tegn skipet på sitt nåværende område"""
        self.skjerm.blit(self.image, self.rect)
        # bevegelse flagg; start mad skip som ikke beveger seg
        self.beveg_hoyre = False
        self.beveg_venstre = False

    def oppdatere(self):
        """oppdaterer skipets posisjon basert på en bevegelses flagg"""
        # oppdaterer skipets x verdi, ikke rect-en
        if self.beveg_hoyre and self.rect.right < self.skjerm_rect.right: # prøv også med "hoyre"
            self.x += self.settinger.skip_fart
            # self.rect.x += 1
        if self.beveg_venstre and self.rect.left > 0: # LEFT BLIR BLÅ MEN IKKE RIGHT?
            self.x -= self.settinger.skip_fart
            #self.rect.x += -1