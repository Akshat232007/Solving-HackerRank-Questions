if __name__ == '__main__':
    s = input()
    
    alpanumeric = False
    alphabetic = False
    Digits = False
    lowercase = False
    uppercase = False
    
    for i in range(len(s)):
        alpanumeric = alpanumeric or s[i].isalnum()
        alphabetic = alphabetic or s[i].isalpha()
        Digits = Digits or s[i].isdigit()    
        lowercase = lowercase or s[i].islower()
        uppercase = uppercase or s[i].isupper()
        
        
    print(f"{alpanumeric}\n{alphabetic}\n{Digits}\n{lowercase}\n{uppercase}")