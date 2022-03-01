import unittest as ut
from client import NamedEntityRecognitionClient

class TestClient(ut.TestCase):
    def test_getEntities_emptyString_dictionary(self):
        client = NamedEntityRecognitionClient()
        entities = client.getEntities("")
        self.assertIsInstance(entities, dict)

# dictionary of entities
#{
# ents: [{...}],
# html: "<span>..."
# }