def tokenize(word):
    tokens = {}
    word = word.lower()
    words = word.split(' ')
    
    i = 0
    while(i < len(words)):
        if(words[i] not in tokens):
            tokens[words[i]] = 1
        else:
            tokens[words[i]] += 1
        i+= 1

            
            

    print(tokens)


word = "How are you how!"
tokenize(word)
