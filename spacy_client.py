class NamedEntityRecognitionClient:
    def __init__(self, model):
        self.model = model

    def getEntities(self, sentence):
        return {}