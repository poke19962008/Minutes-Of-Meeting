from titles import TITLES
import re

from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tag import pos_tag

class HumanName:
    def __init__(self, document):
        self.document = document

        tokenizer = PunktSentenceTokenizer()
        self.sentences = tokenizer.tokenize(self.document)

        self.getTitleIndex()
        self.titleIndex = self.getTitleIndex()
        print self.titleIndex

    def genTitleRegex(self):
        reg = ""
        for TITLE in TITLES:
            reg = reg + TITLE + "|"
        return re.compile("(\s|\.)(" + reg[:-1] + ")(?=\s|\.)")

    def getTitleIndex(self):
        self.reTITLE = self.genTitleRegex()
        titleIndex = {}

        for sentence in self.sentences:
            # print sentence
            for title in self.reTITLE.finditer(sentence):
                # +1 is to remove (\s|\.) from the begining
                titleIndex [sentence[title.start()+1:title.end()] ] = { 'start': title.start(),
                                                                        'end': title.end(),
                                                                        'sentence': self.sentences.index(sentence)
                                                                    }
        return titleIndex

        def getNames(self):
            
