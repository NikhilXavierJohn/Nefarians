from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
with open('as.txt','r') as mal:
    str=''
    for i in mal:
        str=str+i
        #sprint(str)
    #print(str)
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(str)
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    #print(freqTable)
    sentences = sent_tokenize(str)
    #print(sentences)
    #5print(sentences)
    sentenceValue = dict()

    for sentence in sentences:
        #print(sentence)
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                #print(wordValue[1])
                if sentence in sentenceValue:
                    #print(sentence)
                    sentenceValue[sentence] += 1
                    #print(sentenceValue)
                else:
                    sentenceValue[sentence] = 1
    #print(sentenceValue)
    sumValues = 0
    #print(sentenceValue)
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    average = int(sumValues/ len(sentenceValue))
    summary = ''
    for sentence in sentences:
            if sentence in sentenceValue and sentenceValue[sentence] > (1.5*average):
                summary +=  " " + sentence
    print(summary)

