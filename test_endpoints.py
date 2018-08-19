import unittest
import os
import json
from app import create_app

class QuestionsTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.questions = [
                                {
                                    'id': 1,
                                    'question': 'What is the test1?'},
                                {
                                    'id': 2,
                                    'question': 'How would would you test?'}
                            ]

    def test_api_can_get_all_questions(self):
        
        res = self.client().get('/api/v1.0/questions/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('What is the ...', str(res.data))


if __name__ == "__main__":
    unittest.main()