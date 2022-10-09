class NamedEntityRecognitionClient:
    def __init__(self, model):
        self.model = model

    def getEntities(self, sentence):
        doc = self.model(sentence)
        
        for entity in doc.ents:
            print('label from SPACY ')
            print(entity.label_)
        
        entities =[
            {
                'ent':ent.text,
                'label': self.map_label(ent.label_)
            } for ent in doc.ents
        ]
        return {'ents': entities , 'html':''}

    @staticmethod
    def map_label(label):
        label_map = {
            'PERSON':'Person',
            'NORP':'Group',
            'LOC':'Location',
            'GPE':'Location',
            'LANGUAGE':'Language',
            'ORDINAL':'Order'
        }
        return label_map.get(label)