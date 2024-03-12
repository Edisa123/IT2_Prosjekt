class Settinger:
    """en klasse for å lagre alle innstillinger for Alien Invasion"""

    def __init__(self):
        """laste ned spillets innstillinger"""
        # skjerm settinger
        self.skjerm_bredde = 1200
        self.skjerm_hoyde = 800
        self.bg_farge = (0, 0, 0)
        
        # skip hastighet
        self.skip_fart = 3

        # skudd innstillinger
        self.skudd_fart = 2.0
        self.skudd_bredde = 10
        self.skudd_hoyde = 40
        self.skudd_farge = (200, 200, 0)
        self.skudd_lov = 10