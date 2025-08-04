from .dhStat import adversaryTypeToJsonPath 
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
    


def ConvertStatToRange(level, stat, json_name):
    hit_points_data = load_json_data(f"Data/PF/{json_name}.json")
    if(not hit_points_data):
        raise Exception(f"Json {json_name} not found") 
    ranges_for_level = hit_points_data[str(level)]
    range_keys = list(reversed(ranges_for_level.keys()))
    for i in range(len(ranges_for_level)):
        cur_min, cur_max = parseRange(ranges_for_level[range_keys[i]])
        #print(f"range for level: {level} is {cur_min},{cur_max}, stat - {stat}")
        if stat < cur_min:
            if i == 0:
                return f"below {range_keys[0]}"
            else:
                return f"{range_keys[i-1]} to {range_keys[i]}"
        elif stat >= cur_min and stat <= cur_max:
            return range_keys[i]
        elif stat > cur_max:
            if i == len(range_keys)-1:
                return f"above {range_keys[-1]}"


    
def GetAdversaryRanges(tier, type):
    adversary_data = load_json_data(adversaryTypeToJsonPath(type))
    return adversary_data[str(tier)]

    

def parseRange(range):
    if "-" not in range:
        return int(range), int(range)
    nums = range.split("-")
    return int(nums[1]), int(nums[0])

def load_json_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data