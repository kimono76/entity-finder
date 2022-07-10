class NamedEntityRecognitionClient:
    def __init__(self, model):
        self.model = model

    def getEntities(self, sentence):
        doc = self.model(sentence)
        entities =[
            {
                'ent':ent.text,
                'label':ent.label_
            } for ent in doc.ents
        ]
        return {'ents': entities , 'html':''}
        # return {'ents':[] , 'html':''}
