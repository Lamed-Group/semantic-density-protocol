import unittest

from semantic_density.core import Observation, summarize


class ObservationTests(unittest.TestCase):
    def test_published_example(self):
        observation = Observation(
            nodes=18,
            reading_seconds=600,
            reflection_seconds=1800,
            dispersion=5,
        )
        self.assertEqual(observation.E, 3.0)
        self.assertAlmostEqual(observation.P_observed, 10.8)

    def test_invalid_reading_time(self):
        with self.assertRaises(ValueError):
            Observation(1, 0, 1, 1)

    def test_invalid_dispersion(self):
        with self.assertRaises(ValueError):
            Observation(1, 1, 1, 0)

    def test_summary_preserves_range(self):
        observations = [
            Observation(10, 10, 10, 2),
            Observation(20, 10, 10, 2),
            Observation(30, 10, 10, 2),
        ]
        result = summarize(observations)
        self.assertEqual(result.count, 3)
        self.assertEqual(result.minimum, 5.0)
        self.assertEqual(result.median, 10.0)
        self.assertEqual(result.maximum, 15.0)


if __name__ == "__main__":
    unittest.main()
