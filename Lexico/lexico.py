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
    or str == "output" or str == "length" or str == "concatena" or str == "inverte" or str == "var" or str == "boolean"
    or str == "procedure" or str == "true"
    or str == "false" or str == "goto" or str == "label" or str == "string" or str == "program" or str == "then"):
        return True
    return False

def isOperator(ch) -> bool:
    if(ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == "%" or ch== "#"):
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
    if line.strip() != '': #se a linha estiver vazia pula
        while (contadorcoluna<len(line)):
            #print (token)
            if line[contadorcoluna] == ' ' or line[contadorcoluna] == '\n' or isvalidIdentifier(line[contadorcoluna]) or ( isKeyWord(token) and (line[contadorcoluna] == ' ' or line[contadorcoluna] == '\n')):
                
                if isKeyWord(token): #checa se o token formado é uma keyword
                    tabela_tokens.append(Token(token, "Reserved Word", contadorlinha, contadorcoluna))
                    token = ""
                elif (token.isnumeric() or token[1:].isnumeric() )and line[contadorcoluna] != ".":#checa se o token formado é inteiro, tem tratamento para +1 ou -1
                    if token.isnumeric() or ((token[0] == "+" or token[0] == "-") and token[1:].isnumeric()):
                        tabela_tokens.append(Token(token, "Number", contadorlinha, contadorcoluna))
                        token = ""
                    else:
                        tabela_tokens.append(Token(token, "Id", contadorlinha, contadorcoluna))
                        token = ""
                elif (token.isnumeric() or token[1:].isnumeric()) and line[contadorcoluna] == ".":#checa se o token formado é float, tem tratamento para +1 ou -1
                    if token.isnumeric() or ((token[0] == "+" or token[0] == "-") and token[1:].isnumeric()):
                        aux = ""
                        while (not isvalidIdentifier(line[contadorcoluna]) or line[contadorcoluna] == "."): #adiciona os numeros depois do ponto para o token
                                aux = aux + line[contadorcoluna]
                                contadorcoluna += 1
                        tabela_tokens.append(Token(token + aux, "Real", contadorlinha, contadorcoluna))
                        contadorcoluna -= 1
                        token = ""
                    else:
                        tabela_tokens.append(Token(token, "Id", contadorlinha, contadorcoluna))
                        token = ""
                elif token != "":#se o token não for numero real, inteiro ou palavra reservada então ele é ID
                    tabela_tokens.append(Token(token, "Id", contadorlinha, contadorcoluna))
                    token = ""
                if isOperator(line[contadorcoluna]): #checa se o elemento lido atualmente é operador
                    if (line[contadorcoluna] == "+" or line[contadorcoluna] == "-") and line[contadorcoluna + 1].isnumeric():#caso seja um operador + ou - checa se o prox elemento é um numero
                            token = token + line[contadorcoluna]
                    elif (line[contadorcoluna] == "+" or line[contadorcoluna] == "-") and line[contadorcoluna + 1] == " ":#caso seja um operador + ou - checa se o prox elemento é um numero
                        aux = contadorcoluna
                        while (line[aux + 1] == " "): #eliminando os espaços que possam existir entre o + e um numero, ex: "+                1"
                            aux += 1
                            if (line[aux + 1].isnumeric()):
                                token = token + line[contadorcoluna]
                                contadorcoluna = aux
                                aux = ""
                                break
                        if aux!="":
                            tabela_tokens.append(Token(line[contadorcoluna], "Operator", contadorlinha, contadorcoluna))
                    else:
                        tabela_tokens.append(Token(line[contadorcoluna], "Operator", contadorlinha, contadorcoluna))
                        token = ""
                elif isRelationals(line[contadorcoluna]):#checa se o elemento lido atualmente é operador relacional
                    if (line[contadorcoluna] == '<' or line[contadorcoluna] == '>' or line[contadorcoluna] == '=') and line[contadorcoluna + 1] == "=":#caso seja um operador 
                                                                                                                                            #< , > ou = checa se o proximo elemento é um =
                        tabela_tokens.append(Token(line[contadorcoluna] + line[contadorcoluna + 1], "Relational", contadorlinha, contadorcoluna))
                        contadorcoluna += 1
                    elif line[contadorcoluna] == '=' and line[contadorcoluna + 1] != "=":
                        print("LEXICAL ERROR")
                        exit()
                    else:
                        tabela_tokens.append(Token(line[contadorcoluna], "Relational", contadorlinha, contadorcoluna))
                    token = ""
                elif isDelimeter(line[contadorcoluna]):#checa se o elemento lido atualmente é delimitador
                    if line[contadorcoluna] == ':' and line[contadorcoluna + 1] == "=": #caso seja um delimitador : checa se o proximo elemento é =
                        tabela_tokens.append(Token(line[contadorcoluna] + line[contadorcoluna + 1], "Relational", contadorlinha, contadorcoluna))
                        contadorcoluna += 1
                    else:
                        tabela_tokens.append(Token(line[contadorcoluna], "Delimiter", contadorlinha, contadorcoluna))
                    token = ""
            elif line[contadorcoluna].isalpha() or line[contadorcoluna].isnumeric() or line[contadorcoluna] == "_":#caso o elemento lido não seja operador, 
                                                                                                                   #relacional ou delimitador então adiciona esse elemento ao token
                token = token + line[contadorcoluna]
            elif line[contadorcoluna] !="\n":#caso o elemento lido não seja operador, relacional ou delimitador e não seja parte do alfabeto ou dos elementos numericos então da erro
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


