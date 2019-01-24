class Solution(object):
    def findWords(self, words):
        
        topRow = ['q','w','e','r','t','y','u','i','o','p']
        midRow = ['a','s','d','f','g','h','j','k','l']
        lowRow = ['z','x','c','v','b','n','m']

        output = []

        for i in range (len(words)):
            word = list(words[i].lower())
            inTopRow = True
            ii = 0
            while inTopRow and ii<len(word):
                if word[ii] not in topRow:
                    inTopRow = False
                ii += 1
            if inTopRow:
                output.append(words[i])

            inMidRow = True
            j = 0
            while inMidRow and j<len(word):
                if word[j] not in midRow:
                    inMidRow = False
                j += 1
            if inMidRow:
                output.append(words[i])

            inLowRow = True
            jj = 0
            while inLowRow and jj<len(word):
                if word[jj] not in lowRow:
                    inLowRow = False
                jj += 1
            if inLowRow:
                output.append(words[i])
                
        return output
