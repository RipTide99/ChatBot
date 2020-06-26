import spacy

class text_mining:

    def __init__(self, text):
        self.text = text

    def identify_name(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.text)

        for token in doc:
            if(token.pos_ == 'PROPN'):
                return(token.text)
        
        return('0')