import unittest
import os
import json
from app import create_app

class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.question = {"question": "Define the various programming paridigms"}
        self.answer = {"answer": "Object oriented, Procedural and Structured paradigms."}
                                

    def test_api_can_get_all_questions(self):
        """Test endpoint that fetches all questions"""

        res = self.client().get('/api/v1.0/questions/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('What is the ...', str(res.data))
    
    def test_api_can_get_question_by_id(self):
        """Test endpoint that fetches a particular question"""

        res = self.client().get('/api/v1.0/questions/2')
        self.assertEqual(res.status_code, 200)
        self.assertIn('How would ...', str(res.data))


    def test_question_creation(self):
        """Test endpoint that posts a particular question"""

        res = self.client().post('/api/v1.0/questions/', json=self.question)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Define the various programming paridigms', str(res.data))

    def test_question_deletion(self):
        """Test endpoint that deletes a particular question"""

        res = self.client().delete('/api/v1.0/questions/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/api/v1.0/questions/1')
        self.assertEqual(result.status_code, 404)

    def test_api_can_get_all_answers_to_a_question(self):
        """Test endpoint that fetches answers posted to a particular question"""

        res = self.client().get('/api/v1.0/questions/2/answers/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('All editors are ...', str(res.data))
    
    def test_answer_creation(self):
        """Test endpoint that posts answer to a particular question"""
        
        res = self.client().post('/api/v1.0/questions/2/answers/', json=self.answer)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Object oriented, Procedural and Structured paradigms.', str(res.data))



if __name__ == "__main__":
    unittest.main()