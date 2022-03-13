import unittest as ut
from spacy_client import NamedEntityRecognitionClient
from client_double import NamedEntityRecognitionClient_double

class TestClient(ut.TestCase):
    def test_getEntities_emptyString_emptySpacyDocEntities(self):
        model= NamedEntityRecognitionClient_double('eng')
        model.returns_doc_ents([])
        client = NamedEntityRecognitionClient(model)
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