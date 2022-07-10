from html import entities
import unittest as ut
from spacy_client import NamedEntityRecognitionClient
from spacy_client_double import NamedEntityRecognitionClient_double

class TestClient(ut.TestCase):
    def test_getEntities_emptyString_emptySpacyDocEntities(self):
        model= NamedEntityRecognitionClient_double('eng')
        model.returns_doc_ents([])
        client = NamedEntityRecognitionClient(model)
        # client = NamedEntityRecognitionClient_double(model)
        # entities = {} #client.getEntities("")
        entities = client.getEntities("")
        self.assertIsInstance(entities, dict)

    def test_getEntities_string_emptySpacyDocEntities(self):
        model= NamedEntityRecognitionClient_double('eng')
        model.returns_doc_ents([])
        client = NamedEntityRecognitionClient(model)
        entities = client.getEntities("Washinton DC is the capitol of USA")
        self.assertIsInstance(entities, dict)


    def test_getEntities__string_spacy_PersonLowerCase__serializes_Person(self):
        model= NamedEntityRecognitionClient_double('eng')
        doc_entities = [{'text':'Steve Jobs','label_':'PERSON'}]
        model.returns_doc_ents(doc_entities)
        client = NamedEntityRecognitionClient(model)
        result = client.getEntities(" some string ")
        expectedResult = {'ents':[{'ent':'Steve Jobs','label':'Person'}],'html':''}

        self.assertListEqual(result['ents'],expectedResult['ents'])

    # def test_getEntities_string_list(self):
    #     client = NamedEntityRecognitionClient()
    #     entities = client.getEntities("San Francisco is a city in California")
    #     self.assertIsInstance(entities, dict)

# dictionary of entities
#{
# ents: [{...}],
# html: "<span>..."
# }