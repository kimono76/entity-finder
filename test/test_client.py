import unittest as ut
from client import NamedEntityRecognitionClient

class TestClient(ut.TestCase):
    def test_getEntities_emptyString_dictionary(self):
        model= NamedEntityRecognitionClient_Test_Double('eng')
        client = NamedEntityRecognitionClient()
        entities = client.getEntities("")
        self.assertIsInstance(entities, dict)

    # def test_getEntities_string_list(self):
    #     client = NamedEntityRecognitionClient()
    #     entities = client.getEntities("San Francisco is a city in California")
    #     self.assertIsInstance(entities, dict)

# dictionary of entities
#{
# ents: [{...}],
# html: "<span>..."
# }