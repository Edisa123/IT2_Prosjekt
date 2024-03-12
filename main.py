import sys

import pygame as pg

from settings import Settinger
from skip import Skip
from skudd import Skudd

class AlienInvasion:
    '''for a handtere spillobjekter og bevegelse'''

    def __init__(self):
        '''laste inn spill'''
        pg.init()

        # klokke/timer
        self.klokke = pg.time.Clock()
        self.settinger = Settinger()

        self.skjerm = pg.display.set_mode((0,0), pg.FULLSCREEN)
        self.settinger.skjerm_bredde = self.skjerm.get_width()
        self.settinger.skjerm_hoyde = self.skjerm.get_height()
        pg.display.set_caption('"Alien Invasion" Spill')

        # tilkalle skipsklassen
        self.skip = Skip(self)
        self.skudds = pg.sprite.Group()

        # bakgrunnsfarge
        self.bg_farge = (200, 200, 200)

    def kjor_spill(self):
        '''starter en loop av spillet'''
        while True:
            self.sjekk_event()
            self.skip.oppdatere()
            self.oppdater_skjerm()
            self.oppdater_skudds()
            # FPS for spillet
            self.klokke.tick(60)

    def oppdater_skjerm(self):
        # oppdatere skjermen
        self.skjerm.fill(self.settinger.bg_farge)
        for skudd in self.skudds.sprites():
            skudd.tegn_skudd()
        self.skip.blitme()

        pg.display.flip()
    
    def oppdater_skudds(self):
        "oppdaterer skuddets posisjon og fjerner skudd utenfor skjermen"
        self.skudds.oppdatere()
                
        # fjern skudd som er borte
        for skudd in self.skudds.copy():
            if skudd.rect.bottom <= 0:
                self.skudds.remove(skudd)
            print(len(self.skudds))
    
    def sjekk_event(self):
        '''responder til tastetrykk og mus'''
        # hvis brukeren lukker vinduet'''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            # tastetrykk ned
            elif event.type == pg.KEYDOWN:
                self.sjekk_tastNed(event)
            # tastetrykk opp
            elif event.type == pg.KEYUP:
                self.sjekk_tastOpp(event)
    
    def sjekk_tastNed(self, event):
        # taste trykkes ned
        if event.key == pg.K_RIGHT:
            # beveg skipet til hoyre
            self.skip.beveg_hoyre = True
        elif event.key == pg.K_LEFT:
            # beveg skipet til venstre
            self.skip.beveg_venstre = True
        elif event.key == pg.K_SPACE:
            self.skyt_skudd()

    def sjekk_tastOpp(self, event):
        # taste loftes opp
        if event.key == pg.K_RIGHT:
        # skipet stopper bevegelse til hoyre
            self.skip.beveg_hoyre = False
        elif event.key == pg.K_LEFT:
        # skipet stopper bevegelse til venstre
            self.skip.beveg_venstre = False

    def skyt_skudd(self):
        '''lag et nytt skudd og legg til skudd-lista'''
        if len(self.skudds) < self.settinger.skudd_lov:
            nytt_skudd = Skudd(self)
            self.skudds.add(nytt_skudd)

if __name__ == '__main__':
    ''' kjor spillet'''
    ai = AlienInvasion()
    ai.kjor_spill()