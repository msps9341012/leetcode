import collections
def findLadders(beginWord, endWord, wordList):

    wordList = set(wordList)
    res = []
    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        newlayer = collections.defaultdict(list)
        for w in layer: ###attention!
            if w == endWord: 
                res.extend(k for k in layer[w])
            else:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neww = w[:i]+c+w[i+1:]
                        if neww in wordList:
                            newlayer[neww]+=[j+[neww] for j in layer[w]]
        print(w,newlayer)

        wordList -= set(newlayer.keys())
        layer = newlayer
        #print(layer)

    return res

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

findLadders(beginWord, endWord, wordList)