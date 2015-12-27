from summary import Summary

# print Summary().getWeight(open('testDoc.txt').read())
print Summary(open('testDoc.txt').read()).getSummary()
