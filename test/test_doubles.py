class NamedEntityRecognitionClient_Test_Double:
    """
    Test double for spaCy NLP model
    """

    def __init__(self, model):
        self.model = model
    
    def returns_doc_ents(self,entities):
        self.entities = entities

    def __call__(self, sentence):
        return DocTestDouble(sent, self.entities)
    
class DocTestDouble:
    """
    Test double for spaCy Doc
    """
    def __init__(self, sent, entities):
        self.entities = []