import unittest
from app.yllm import Meditation, MeditationType, Instruction, Pause, yi_generate

class TestMeditationGenerator(unittest.TestCase):

    def test_yi_generate_output_types(self):
        """Test if the generated meditation has correct object types."""

        meditation = yi_generate() 
        
        self.assertIsInstance(meditation, Meditation)
        self.assertIsInstance(meditation.type, MeditationType)
        self.assertIsInstance(meditation.duration, int)

        for item in meditation.instructions:
            self.assertTrue(isinstance(item, Instruction) or isinstance(item, Pause))

    def test_yi_generate_total_duration(self):
        """Test if the total duration of instructions matches the expected duration."""
        expected_duration = 45 

        meditation = yi_generate() 
        
        total_duration = sum(item.duration for item in meditation.instructions) 

        self.assertEqual(total_duration, expected_duration)

if __name__ == '__main__':
    unittest.main()