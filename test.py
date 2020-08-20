from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
    """Stuff to do before every test."""

    self.client = app.test_client()
    app.config['TESTING'] = True

    def test_homepage(self):
    """Make sure information is in the session and HTML is displayed"""

    with self.client:
        response = self.client.get('/start')
        self.assertIn('board', session)
        self.assertIn(b'Score:', response.data)

    def test_invalid_word(self):
    """Test if word is on the board"""

    self.client.get('/')
    response = self.client.get('/check-word?word=impossible')
    self.assertEqual("result", 'not-on-board')

    def non_english_word(self):
    """Test if word is actual word"""

    self.client.get('/')
    response = self.client.get(
        '/check-word?word=fsjdakfkldsfjdslkfjdlksf')
    self.assertEqual("result", 'not-word')
