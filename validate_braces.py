#!/usr/bin/env python3
'''
    this scrip Validates a string code as all its braces are correctly closed
'''

class Code:
    def __init__ (self,mystring) :
       self.mystring=mystring
    
    def validate_braces (self) :
        cursor_stack=[] 
        starts_with = ['{','(','[']
        ends_with = ['}',')',']']
        
        for character in self.mystring:

            if character in starts_with :  
                cursor_stack.append(ends_with[starts_with.index(character)])
            
            elif character in ends_with:
                if len(cursor_stack) == 0:
                    return False
                else:
                    cursor_stack.pop()
        
        if len(cursor_stack) == 0 :
            return True
        
        else:
            return False

mycode  = Code('({f }){c }(arg )')
mycode1 = Code('({func }){code }((')
mycode2 = Code('({str }){code }[ ')

print(mycode.validate_braces())
print(mycode1.validate_braces())
print(mycode2.validate_braces())