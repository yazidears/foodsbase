import spacy
from spacy.lang.en.examples import sentences
from string import punctuation

nlp = spacy.load("en_core_web_sm")

def get_keywords(desc):
    keywords = []
    
    doc = nlp(desc.lower())
    
    tags = ['PROPN', 'NOUN', 'ADJ']
    
    for token in doc:
        if (token.text in nlp.Defaults.stop_words or token.text in punctuation) == False and token.pos_ in tags:
            keywords.append(token.text)
    return keywords

text = "Molten chocolate cake is a dessert that consists of a chocolate cake with a liquid chocolate core. It is named for that molten center, and it is also known as chocolate coulant, chocolate lava cake, or simply lava cake."

keywords = list(set(get_keywords(text)))