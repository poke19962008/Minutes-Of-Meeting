from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize

from nameparser import HumanName

class Summary:
    def __init__(self, document):
        self.document = document

        self.sumLength = 10

        self.weights = {}
        self.invWeights = {}
        self.sumIndex = {}
        self.summary = {}

        tokenizer = PunktSentenceTokenizer()
        self.sentences = [sentence.lower() for sentence in tokenizer.tokenize(document)]

        HumanName(self.document)

    def getWeight(self):
        stopWords = open('summary/stopWords.txt').read().split('\n')

        words = [word.lower() for word in word_tokenize(self.document)]
        words = [word for word in words if word not in stopWords]
        fWords = FreqDist(words).items()

        tokenizer = RegexpTokenizer('\w+')
        for sentence in self.sentences:
            self.weights[sentence] = { 'keyWords': [] }
            weight = 0

            for word in fWords:
                if word[0] in sentence:
                    self.weights[sentence]['keyWords'].append({ word[0]: word[1] })
                    weight = weight + word[1]

            self.weights[sentence]['weight'] = weight
            self.invWeights[weight] = []
            self.invWeights[weight].append(sentence)

    def sequentialSort(self, summary):
        for key in summary.iterkeys():
            summary[key]['index'] = self.sentences.index(key)
            self.sumIndex[self.sentences.index(key)] = key
        return summary

    def getSummaryText(self):
        self.getSummary()

        for index in sorted(self.sumIndex.iterkeys()):
            print "+ " + self.sumIndex[index]

    def getSummary(self):
        self.getWeight()

        summary = {}
        prevKey = -1
        for key in sorted(self.invWeights.iterkeys(), reverse=True):
            if prevKey != -1 and prevKey != key:
                self.sumLength = self.sumLength - 1

            if self.sumLength == 0:
                break
            for sentence in self.invWeights[key]:
                summary[sentence] = self.weights[sentence]

            prevKey = key

        self.summary = self.sequentialSort(summary)
        return self.summary
