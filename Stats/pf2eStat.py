

class Pf2eStat:

    def __init__(self, level, ac, hp, st, att_bon, att_dmg, caster = False, spl_bon = None, spl_dc = None):
        self.level = level
        self.ac = ac
        self.hp = hp
        #st is an array of 3 ints representing fort, ref and will in that order
        self.st = st
        self.att_bon = att_bon
        self.att_dmg = att_dmg
        if caster:
            self.spl_bon = spl_bon
            self.spl_dc = spl_dc
        pass