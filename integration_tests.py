
import unittest
from operations import Base


class IntegrationTests(unittest.TestCase):
    def test_create(self):
        b = Base()
        self.assertEqual(b.create('', '<asd>Test</asd>'), 'Document has been added.')
        self.assertEqual(b.create('renewed', 'Woo.'), 'Document has been added.')

    def test_read(self):
        b = Base()
        self.assertEqual(b.read('second'), 'Second')
        self.assertEqual(b.read('asd'), 'Document has not been read.')

    def test_update(self):
        b = Base()
        self.assertEqual(b.update('re', '<asd>NewResult</asd>'), "Document doesn't exist.")

    def test_delete(self):
        b = Base()
        self.assertEqual(b.delete('renewed'), 'Document has been deleted.')
        self.assertEqual(b.delete('sad'), "Document doesn't exist.")