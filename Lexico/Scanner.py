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
    or str == "function" or str == "integer" or str == "real" or str == "const" 
    or str == "fila_of_integer" or str == "fila_of_real" or str == "input"
    or str == "output" or str == "lenght" or str == "concatena" or str == " inverte"):
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
    if(isOperator(str[0]) == True or
    isDelimeter(str[0]) == True or isRelationals(str[0]) == True):
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
            if line[contadorcoluna] == ' ' or isvalidIdentifier(line[contadorcoluna]):
                if isKeyWord(token):
                    tabela_tokens.append(Token(token, "Reserved Word", contadorlinha, contadorcoluna))
                elif line[contadorcoluna].isnumeric() and line[contadorcoluna + 1] != ".":
                    tabela_tokens.append(Token(token, "number", contadorlinha, contadorcoluna))
                #elif isReal(line[contadorcoluna]):
                elif line[contadorcoluna].isnumeric() and line[contadorcoluna + 1]  == ".":
                    tabela_tokens.append(Token(line[contadorcoluna]+ line[contadorcoluna + 1], "real", contadorlinha, contadorcoluna))
                    contadorcoluna += 1
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

for i in tabela_tokens:
    print(i.name + "    " + i.tipo + "    " + str(i.linha) + "    " + str(i.coluna))
