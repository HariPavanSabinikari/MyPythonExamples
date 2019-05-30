def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    d = {}
    for i, word in enumerate(words):
        d[word]=i    
    #print(d)
    result=[]
    for i, word in enumerate(words):
        for char_i in range(len(words)):
            prefix, suffix = word[:char_i],word[char_i:]
            reversed_prefix=prefix[::-1]
            reversed_suffix=suffix[::-1]
            
            
            if(is_palindrome(suffix) and reversed_prefix in d):
                if i != d[reversed_prefix]:
                    result.append((i,d[reversed_prefix]))
                    
                    
            if(is_palindrome(prefix) and reversed_suffix in d):
                if i != d[reversed_suffix]:
                    result.append((d[reversed_suffix],i))
                
    print(result)

words=("code","edoc", "da","d")
palindrome_pairs(words)
#print(res)