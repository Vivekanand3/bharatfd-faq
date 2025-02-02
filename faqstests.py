from django.test import TestCase
from .models import FAQ

class FAQTests(TestCase):
    def test_faq_translation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        self.assertEqual(faq.get_translated_question('hi'), faq.question)