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

        # bakgrunnsfarge
        self.bakgrunn_farge = (200, 200, 200)

    def kjor_spill(self):
        '''starter en loop av spillet'''
        while True:
            '''hvis brukeren lukker vinduet'''
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                
                # oppdatere skjermen
                self.skjerm.fill(self.settinger.bakgrunn_farge)

                pg.display.flip()
                # FPS for spillet
                self.klokke.tick(60)


if __name__ == '__main__':
    ''' kjor spillet'''
    ai = AlienInvasion()
    ai.kjor_spill()




