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

class Adversary_Type(Enum):
    Bruiser = "Bruiser"
    Horde = "Horde"
    Leader = "Leader"
    Minion = "Minion"
    Ranged = "Ranged"
    Skulk = "Skulk"
    Solo = "Solo"
    Standard = "Standard"
    Support = "Support"


def adversaryTypeToJsonPath(type):
    path = "Data/DH/"
    match(type):
        case Adversary_Type.Bruiser:
            path += "bruiser.json"
        case Adversary_Type.Horde:
            path += "horde.json"
        case Adversary_Type.Leader:
            path += "leader.json"
        case Adversary_Type.Minion:
            path += "minion.json"
        case Adversary_Type.Ranged:
            path += "ranged.json"
        case Adversary_Type.Skulk:
            path += "skulk.json"
        case Adversary_Type.Solo:
            path += "solo.json"
        case Adversary_Type.Standard:
            path += "standard.json"
        case Adversary_Type.Support:
            path += "support.json"
    return path