from Stats.statConverter import convertLevelToTier, ConvertStatToRange, GetAdversaryRanges
from Stats.dhStat import Adversary_Type
import unittest

class TestStatConverter(unittest.TestCase):
    def test_convertLevelToTier(self):
        self.assertEqual(convertLevelToTier(1), 1)
        self.assertEqual(convertLevelToTier(4), 2)
        self.assertEqual(convertLevelToTier(8), 2)
        self.assertEqual(convertLevelToTier(10), 3)
        self.assertEqual(convertLevelToTier(12), 3)
        self.assertEqual(convertLevelToTier(16), 4)
        self.assertEqual(convertLevelToTier(20), 4)


    def test_convertStatToRange_armor_class(self):
        # Assuming the armor_class.json has been set up correctly
        self.assertEqual(ConvertStatToRange(1, 3, "armor_class"), "below low")
        self.assertEqual(ConvertStatToRange(1, 13, "armor_class"), "low")
        self.assertEqual(ConvertStatToRange(2, 16, "armor_class"), "low to moderate")
        self.assertEqual(ConvertStatToRange(2, 17, "armor_class"), "moderate")
        self.assertEqual(ConvertStatToRange(8, 27, "armor_class"), "high")
        self.assertEqual(ConvertStatToRange(12, 35, "armor_class"), "high to extreme")
        self.assertEqual(ConvertStatToRange(16, 42, "armor_class"), "extreme")
        self.assertEqual(ConvertStatToRange(17, 400, "armor_class"), "above extreme")

    def test_ConvertStatToRange_HP(self):
        print("testing hp")
        # Assuming the hit_points.json has been set up correctly
        self.assertEqual(ConvertStatToRange(1, 3, "hit_points"), "below low")
        self.assertEqual(ConvertStatToRange(2, 23, "hit_points"), "low")
        self.assertEqual(ConvertStatToRange(4, 50, "hit_points"), "low to moderate")
        self.assertEqual(ConvertStatToRange(8, 135, "hit_points"), "moderate")
        self.assertEqual(ConvertStatToRange(12, 240, "hit_points"), "moderate to high")
        self.assertEqual(ConvertStatToRange(16, 370, "hit_points"), "high")
        self.assertEqual(ConvertStatToRange(17, 400, "hit_points"), "above high")

    def test_GetAdversaryRanges(self):
        # Assuming the adversary data is set up correctly
        self.assertEqual(GetAdversaryRanges(1, Adversary_Type.Bruiser), {
        "Difficulty" : "12-14",
        "Major Threshold": "7-9",
        "Severe Threshold" : "14-18",
        "HP" : "6-7",
        "Stress" : "3-4",
        "ATK" : "0-2",
        "Damage Average": "8-11",
        "Potential Dice Pools" : ["1d8+6",  "1d10+4", "1d12+2"]
    })
        self.assertEqual(GetAdversaryRanges(2, Adversary_Type.Horde), {
        "Difficulty" : "12-14",
        "Major Threshold": "10-15",
        "Severe Threshold" : "16-20",
        "HP" : "5-6",
        "Stress" : "2-3",
        "ATK" : "-1-1",
        "Damage Average": "9-13",
        "Potential Dice Pools" : ["2d8+6",  "2d10+2", "2d12+3"]
    })
        self.assertEqual(GetAdversaryRanges(3, Adversary_Type.Leader), {
        "Difficulty" : "17-19",
        "Major Threshold": "18-25",
        "Severe Threshold" : "36-42",
        "HP" : "8-10",
        "Stress" : "5-6",
        "ATK" : "5-7",
        "Damage Average": "15-18",
        "Potential Dice Pools" : ["3d8+8",  "3d10+1"]
    })
        self.assertEqual(GetAdversaryRanges(4, Adversary_Type.Minion), {
        "Difficulty" : "16-18",
        "Major Threshold": "-",
        "Severe Threshold" : "-",
        "HP" : "1",
        "Stress" : "1",
        "ATK" : "1-3",
        "Minion Passive": "9-12",
        "Potential Dice Pools" : "10-12"
    })
        
if __name__ == "__main__":
    unittest.main()