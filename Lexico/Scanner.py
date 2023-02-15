def isKeyWord(str = []) -> bool:
    if(str == "read" or str == "write" or str == "for" or str == "to"
    or str == "do" or str == "begin" or str == "end" or str == "repeat"
    or str == "until" or str == "while" or str == "if" or str == "else"
    or str == "function" or str == "integer" or str == "real"):
        return True
    return False

def isOperator(ch) -> bool:
    if(ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == "//"):
        return True
    return False

def isRelationals(ch) -> bool:
    if(ch == "=" or ch == ">" or ch == "<" or ch == ">=" or ch == "<=" or ch == "<>"):
        return True
    return False

def isDelimeter(ch) -> bool:
    if(ch == ";" or ch == "{" or ch == "}"): return True
    return False

def validIdentifier(str = []) -> bool:
    if(str[0] == '0' or str[0] == '1' or str[0] == '2' or str[0] == '3' or
    str[0] == '4' or str[0] == '5' or str[0] == '6' or str[0] == '7' or
    str[0] == '8' or str[0] == '9' or isOperator(str[0]) == True or
    isDelimeter(str[0]) == True or isRelationals(str[0]) == True):
        return False
    return True