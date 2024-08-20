import unittest
from app.yllm import Meditation, MeditationType, Instruction, Pause, yi_generate

class TestMeditationGenerator(unittest.TestCase):

    def test_yi_generate_output_types(self):
        """Test if the generated meditation has correct object types."""
        # Provide a sample user query
        user_query = "Create a 5 minute relaxation meditation."
        meditation = yi_generate(user_query)  # Pass user_query here

        self.assertIsInstance(meditation, Meditation)
        self.assertIsInstance(meditation.type, MeditationType)
        self.assertIsInstance(meditation.duration, int)

        for item in meditation.instructions:
            self.assertTrue(isinstance(item, Instruction) or isinstance(item, Pause))

    def test_yi_generate_total_duration(self):
        """Test if the total duration of instructions matches the expected duration."""
        expected_duration = 45
        # Provide a sample user query
        user_query = "Create a 45-second meditation for focus."
        meditation = yi_generate(user_query) # Pass user_query here

        total_duration = sum(item.duration for item in meditation.instructions)

        self.assertEqual(total_duration, expected_duration)


if __name__ == "__main__":
    unittest.main()