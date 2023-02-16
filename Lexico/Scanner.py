def isKeyWord(str = []) -> bool:
    if(str == "read" or str == "write" or str == "for" or str == "to"
    or str == "do" or str == "begin" or str == "end" or str == "repeat"
    or str == "until" or str == "while" or str == "if" or str == "else"
    or str == "function" or str == "integer" or str == "real" or str == "const"):
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
    if(ch == ";" or ch == "(" or ch == ")" or ch == ":" or ch == "," or ch == "." or ch == "'" or ch == "[" or ch == "]"): return True
    return False

def isvalidIdentifier(str = []) -> bool:
    if(isOperator(str[0]) == True or
    isDelimeter(str[0]) == True or isRelationals(str[0]) == True):
        return True
    return False

arquivo = open("prog.pas", "r")

token = ""

contadorlinha = 0
contadorcoluna = 0

tabela_tokens = {}



for line in arquivo:
    if line.strip() != '':
        for index in line:
            if index == ' ' or isvalidIdentifier(index):
                if isKeyWord(token):
                    tabela_tokens[token] = "Reserved Word"
                elif token.isnumeric():
                    tabela_tokens[token] = "Number"
                elif token != "":
                    tabela_tokens[token] = "Id"
                if isOperator(index):
                    tabela_tokens[index] = "Operator"
                elif isRelationals(index):
                    if (index == '<' or index == '>') and (line[contadorcoluna + 1] == "=" or line[contadorcoluna + 1] == ">"):
                        tabela_tokens[index + line[contadorcoluna + 1]] = "Relational"
                    else:
                        tabela_tokens[index] = "Relational"
                elif isDelimeter(index):
                    if index == ':' and line[contadorcoluna + 1] == "=":
                        tabela_tokens[index + line[contadorcoluna + 1]] = "Relational"
                    else:
                        tabela_tokens[index] = "Delimiter"
                token = ""
            elif index.isalpha() or index.isnumeric():
                token = token + index
            elif index !="\n":
                print("ERROR")
                exit()
            contadorcoluna += 1
        contadorlinha += 1
        contadorcoluna = 0

print(tabela_tokens)
