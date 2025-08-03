from enum import Enum

class DhStat:

    def __init__(self, tier,dif, m_thresh, s_thresh, hp, strs, att, dmg_avg,minion_passive=None):
        self.tier = tier
        self.dif = dif
        self.m_thresh = m_thresh
        self.s_thresh = s_thresh
        self.hp = hp
        self.strs = strs
        self.att = att
        self.dmg_avg = dmg_avg
        self.minion_passive = minion_passive

        pass

Adversary_Type = Enum("Bruiser", "Horde", "Leader", "Minion", "Ranged", "Skulk", "Solo", "Standard", "Support")
