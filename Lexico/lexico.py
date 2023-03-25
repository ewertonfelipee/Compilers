class Token():
    def __init__(self, name, tipo, linha, coluna):
        self.name = name
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna

def isKeyWord(str = []) -> bool:
    if(str == "read" or str == "write" or str == "for" or str == "to"
    or str == "do" or str == "begin" or str == "end" or str == "repeat"
    or str == "until" or str == "while" or str == "if" or str == "else"
    or str == "function" or str == "integer" or str == "real"
    or str == "fila_of_integer" or str == "fila_of_real" or str == "input"
    or str == "output" or str == "lenght" or str == "concatena" or str == " inverte" or str == "var" or str == "boolean"
    or str == "procedure" or str == "true"
    or str == "false" or str == "goto" or str == "label" or str == "string" or str == "program" or str == "then"):
        return True
    return False

def isOperator(ch) -> bool:
    if(ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == "%"):
        return True
    return False

def isRelationals(ch) -> bool:
    if(ch == "=" or ch == ">" or ch == "<" or ch == ">=" or ch == "<=" or ch == "=="):
        return True
    return False

def isDelimeter(ch) -> bool:
    if(ch == ";" or ch == "(" or ch == ")" or ch == ":" or ch == "," or ch == "." or ch == "'" or ch == "[" or ch == "]"): return True
    return False

def isvalidIdentifier(str = []) -> bool:
    if(isOperator(str) == True or
    isDelimeter(str) == True or isRelationals(str) == True):
        return True
    return False

arquivo = open("prog.pas", "r")

token = ""

contadorlinha = 0
contadorcoluna = 0

tabela_tokens = []

for line in arquivo:
    if line.strip() != '':
        while (contadorcoluna<len(line)):
            #print (token)
            if line[contadorcoluna] == ' ' or line[contadorcoluna] == '\n' or isvalidIdentifier(line[contadorcoluna]) or ( isKeyWord(token) and (line[contadorcoluna] == ' ' or line[contadorcoluna] == '\n')):
                if isKeyWord(token):
                    tabela_tokens.append(Token(token, "Reserved Word", contadorlinha, contadorcoluna))
                elif token.isnumeric() and line[contadorcoluna] != ".":
                    tabela_tokens.append(Token(token, "Number", contadorlinha, contadorcoluna))
                elif token.isnumeric() and line[contadorcoluna] == ".":
                    aux = ""
                    while (not isvalidIdentifier(line[contadorcoluna]) or line[contadorcoluna] == "."):
                            aux = aux + line[contadorcoluna]
                            contadorcoluna += 1
                    tabela_tokens.append(Token(token + aux, "Real", contadorlinha, contadorcoluna))
                    contadorcoluna -= 1
                elif token != "":
                    tabela_tokens.append(Token(token, "Id", contadorlinha, contadorcoluna))
                if isOperator(line[contadorcoluna]):
                    tabela_tokens.append(Token(line[contadorcoluna], "Operator", contadorlinha, contadorcoluna))
                elif isRelationals(line[contadorcoluna]):
                    if (line[contadorcoluna] == '<' or line[contadorcoluna] == '>' or line[contadorcoluna] == '=') and line[contadorcoluna + 1] == "=":
                        tabela_tokens.append(Token(line[contadorcoluna] + line[contadorcoluna + 1], "Relational", contadorlinha, contadorcoluna))
                        contadorcoluna += 1
                    else:
                        tabela_tokens.append(Token(line[contadorcoluna], "Relational", contadorlinha, contadorcoluna))
                elif isDelimeter(line[contadorcoluna]):
                    if line[contadorcoluna] == ':' and line[contadorcoluna + 1] == "=":
                        tabela_tokens.append(Token(line[contadorcoluna] + line[contadorcoluna + 1], "Relational", contadorlinha, contadorcoluna))
                        contadorcoluna += 1
                    else:
                        tabela_tokens.append(Token(line[contadorcoluna], "Delimiter", contadorlinha, contadorcoluna))
                token = ""
            elif line[contadorcoluna].isalpha() or line[contadorcoluna].isnumeric() or line[contadorcoluna] == "_":
                token = token + line[contadorcoluna]
            elif line[contadorcoluna] !="\n":
                print("ERROR")
                exit()
            contadorcoluna += 1
        contadorlinha += 1
        contadorcoluna = 0

f = open("Token.txt", "w")

for i in tabela_tokens:
    f.write(i.name + "    " + i.tipo + "    " + str(i.linha) + "    " + str(i.coluna) + "\n")

f.close()
arquivo.close()


