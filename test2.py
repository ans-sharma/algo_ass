
import collections
def uniqueMorseRepresentations(words):
    result = []
    letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
               "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    for i in words:
        tempStr = ""                                                                                    
        for j in i:
            temp = ord(j)-97
            tempStr += letters[temp]
        result.append(tempStr)
    print(result)
    counter = collections.Counter(result)
    print(counter)
    c = 0
    for i, j in enumerate(counter):
        c += 1
    return c

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))
