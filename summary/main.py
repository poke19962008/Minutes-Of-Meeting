from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer

class Summary:
    def getWeight(self, document):
        stopWords = open('summary/stopWords.txt').read().split('\n')

        tokenizer = RegexpTokenizer('\w+')
        words = [word.lower() for word in tokenizer.tokenize(document)]
        words = [word for word in words if word not in stopWords]
        fWords = FreqDist(words).items()

        tokenizer = PunktSentenceTokenizer()
        sentences = [sentence.lower() for sentence in tokenizer.tokenize(document)]

        result = {}
        tokenizer = RegexpTokenizer('\w+')
        for sentence in sentences:
            result[sentence] = { 'keyWords': [] }
            weight = 0

            for word in fWords:
                if word[0] in sentence:
                    result[sentence]['keyWords'].append({ word[0]: word[1] })
                    weight = weight + word[1]

            result[sentence]['weight'] = weight

        return result
