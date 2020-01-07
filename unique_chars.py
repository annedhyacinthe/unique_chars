""" Problem: look to see if there are any duplicates
input: string
output:boolean
Ecamples:
abc === true
aab === false
Aa === true
 === none
"""
def unique(string):
    if len(string) < 1:
        return None
    
    chars = {}
        for char in string:
            if char in dic:
                return false
            else:
                chars[char] = 1
        
        return True

 