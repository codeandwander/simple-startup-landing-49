import unittest
from unittest.mock import patch
from landing_page import LandingPage

class TestLandingPage(unittest.TestCase):
    def setUp(self):
        self.landing_page = LandingPage()

    def test_render_hero_section(self):
        """Test that the hero section is rendered correctly"""
        html = self.landing_page.render_hero_section()
        self.assertIn('<h1>Simple Startup</h1>', html)
        self.assertIn('<p>Your startup solution</p>', html)
        self.assertIn('<button>Get Started</button>', html)

    @patch('landing_page.requests.get')
    def test_get_company_info(self, mock_get):
        """Test that the company information is fetched correctly"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'name': 'Simple Startup',
            'tagline': 'Your startup solution'
        }
        name, tagline = self.landing_page.get_company_info()
        self.assertEqual(name, 'Simple Startup')
        self.assertEqual(tagline, 'Your startup solution')

    def test_integration_render_page(self):
        """Test the integration of rendering the full landing page"""
        html = self.landing_page.render_page()
        self.assertIn('<h1>Simple Startup</h1>', html)
        self.assertIn('<p>Your startup solution</p>', html)
        self.assertIn('<button>Get Started</button>', html)

if __name__ == '__main__':
    unittest.main()