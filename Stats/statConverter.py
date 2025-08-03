from .dhStat import Adversary_Type
import json

TIER_RANGES = [1,2,5,8]

def convertLevelToTier(level):
    level *= 0.5
    if level >= TIER_RANGES[3]:
        return 4
    elif level >= TIER_RANGES[2]:
        return 3
    elif level >= TIER_RANGES[1]:
        return 2
    else:
        return 1
    

def convertAcToRange(level, ac):
    armor_class_data = load_json_data("Data/PF/armor_class.json")
    ranges_for_level = armor_class_data[str(level)]
    tier = convertLevelToTier(level)
    if ac >= int(ranges_for_level["extreme"]):
        return "extreme"
    elif ac >= int(ranges_for_level["high"]):
        return "high"
    elif ac >= int(ranges_for_level["moderate"]):
        return "moderate"
    else:
        return "low"
    



def load_json_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data