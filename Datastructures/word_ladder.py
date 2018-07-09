
"""
Created on Sat Jul  7 18:14:45 2018

@author: jarvis

"""
#Solving the word-bucket problem as asked on interactivepython.org

from pythonds.graphs import Graph


def buildGraph(wordFile): 
    wfile = open(wordFile, 'r')
    d = {} 
    g = Graph()
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)-1):
            #create the bucket
            bucket = word[:i] + "_" + word[i+1:]
            #print(bucket)
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    #add edges between the words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g
