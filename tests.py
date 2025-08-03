from Stats.statConverter import convertAcToRange, convertLevelToTier, ConvertStatToRange
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
        
if __name__ == "__main__":
    unittest.main()