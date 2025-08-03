from Stats.statConverter import convertAcToRange, convertLevelToTier
import unittest

class TestStatConverter(unittest.TestCase):
    def test_convertLevelToTier(self):
        self.assertEqual(convertLevelToTier(1), 1)
        self.assertEqual(convertLevelToTier(2), 2)
        self.assertEqual(convertLevelToTier(5), 3)
        self.assertEqual(convertLevelToTier(8), 4)
        self.assertEqual(convertLevelToTier(9), 4)

    def test_convertAcToRange(self):
        # Assuming the armor_class.json has been set up correctly
        self.assertEqual(convertAcToRange(1, 8), "low")
        self.assertEqual(convertAcToRange(6, 23), "moderate")
        self.assertEqual(convertAcToRange(8, 29), "high")
        self.assertEqual(convertAcToRange(10, 40), "extreme")
