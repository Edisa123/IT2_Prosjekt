# side 244

import sys

import pygame as pg

from setting import Settinger

class AlienInvasion:
    '''for a handtere spillobjekter og bevegelse'''

    def __init___(self):
        '''laste inn spill'''
        pg.init()

        # klokke/timer
        self.klokke = pg.time.Clock()
        self.settinger = Settinger()

        self.skjerm = pg.display.set_mode((self.settinger.skjerm_bredde, self.settinger.skjerm_hoyde))
        pg.display.set_caption('"Alien Invasion" Spill')

        # tilkalle skipsklassen
        self.skip = Skip(self)

        # bakgrunnsfarge
        self.bakgrunn_farge = (200, 200, 200)

    def kjor_spill(self):
        '''starter en loop av spillet'''
        while True:
            self.sjekk_event()
            self.skip.oppdater()
            self.oppdater_skjerm()
            # FPS for spillet
            self.klokke.tick(60)

    def oppdater_skjerm(self):
        # oppdatere skjermen
        self.skjerm.fill(self.settinger.bakgrunn_farge)
        self.skip.blitme()

        pg.display.flip()
    
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

    def sjekk_tastOpp(self, event):
        # taste loftes opp
        if event.key == pg.K_RIGHT:
        # skipet stopper bevegelse til hoyre
            self.skip.beveg_hoyre = False
        elif event.key == pg.K_LEFT:
        # skipet stopper bevegelse til venstre
            self.skip.beveg_venstre = False



if __name__ == '__main__':
    ''' kjor spillet'''
    ai = AlienInvasion()
    ai.kjor_spill()




