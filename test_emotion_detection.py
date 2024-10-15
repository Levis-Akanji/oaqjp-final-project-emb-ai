import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_statements(self):
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

        for statement, expected_emotion in test_cases.items():
            with self.subTest(statement=statement):
                response = emotion_detector(statement)
                self.assertEqual(response['dominant_emotion'], expected_emotion)

if __name__ == '__main__':
    unittest.main()
