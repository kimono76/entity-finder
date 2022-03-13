class NamedEntityRecognitionClient_double:
    """
    test_doubles for spaCy NLP model

    for using mock class implementations you could also use the following:
    
    pytest_mock 
    pip install pytest-mock
    https://medium.com/@bfortuner/python-unit-testing-with-pytest-and-mock-197499c4623c
    https://www.freblogg.com/pytest-functions-mocking-1

    monkey patch
    https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior/
    https://stackoverflow.com/questions/5626193/what-is-monkey-patching


    """

    def __init__(self, model):
        self.model = model
    
    def returns_doc_ents(self,entities):
        self.entities = entities 

    def __call__(self, sentence):
        return DocTest(sentence, self.entities)
    
class DocTest:
    """
    class DocTestDouble Test double for spaCy Doc
    """
    def __init__(self, sent, entities):
        self.entities = [SpanTest(ent['text'], ent['label_']) for ent in entities]

    def patch_methods(self, attr, return_value):
        def patched(): return return_value
        setattr(self, attr, patched)
        return self

class SpanTest:
    """
    class SpanTestDouble for spacy span
    """
    def __init__(self, text, label):
        self.text = text
        self.label = label