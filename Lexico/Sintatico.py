from lexico import tabela_tokens

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

dicionario = {}

arquivo = open("bnf2.txt", "r")

flag = 0

aux = ""

for line in arquivo:
    for word in line.split():
        if word == "&":
            flag = 1
        elif word != "|" and flag == 0:
            dicionario[word] = Node(word)
            aux = word
        elif flag == 1:
            dicionario[aux].add_child(word)
    flag = 0

#for key in dicionario:
    #print(key)
    #print(dicionario[key].children)

aux = 0
aux2 = 1
flag = 0

excecoes = ["<id>", "<real_num>", "<integer_num>", "<tipo_var>", "<rotina>", "<tipo_funcao>" , "<comando>" , "<condicao>" , "<expressao>" 
            , "<relacao>" , "<expressao_num>" , "<operando>" , "<operador>" , "<termo>" , "<expressao_fila>" , "<conteudo>", "<opFila>"]

def validId(id):
    if id[0].isnumeric():
        return False
    return True

def validNumb(numb):
    global aux
    for i in numb:
        if i.isnumeric() == False and i!="+" and i!="-" and i!=".":
            return False
    return True

def navegacaoexhaust(key):
    global aux,aux2
    for i in dicionario[key].children:
        if i[0] != "<" and i !="|":
            if i != tabela_tokens[aux].name:
                if "|" in dicionario[key].children:
                    break
                else:
                    return
            else:
                navegacao(i)
        else:    
            navegacaoexhaust(i)


def navegacao(key):
    global aux, aux2, flag
    for i in dicionario[key].children:
        if i[0] != "<" and i !="|":
            if i != tabela_tokens[aux].name:
                if "|" in dicionario[key].children:
                    break
                else:
                    if flag == 1:
                        return
                    else:
                        print("ERROR" + aux)
                        exit()
            else:
                aux = aux + 1
                if flag == 1:
                    flag = 0
        elif i !="|":
            if i in excecoes:
                if i =="<id>":
                    if validId(tabela_tokens[aux].name) and tabela_tokens[aux].tipo == "Id":
                        aux = aux + 1
                        if flag == 1:
                            flag = 0
                    else:
                        if flag == 1:
                            return
                        else:
                            print("ERROR"  + aux)
                            exit()
                elif i =="<real_num>" or i =="<integer_num>":
                    if validNumb(tabela_tokens[aux].name) and (tabela_tokens[aux].tipo == "Real" or tabela_tokens[aux].tipo == "Number"):
                        aux = aux + 1
                        if flag == 1:
                            flag = 0
                    else:
                        if flag == 1:
                            return
                        else:
                            print("ERROR"  + aux)
                            exit() 
                else:
                    flag = 1
                    while( i + str(aux2) in dicionario and flag == 1):
                        navegacao(i + str(aux2))
                        aux2 = aux2 + 1
            else:    
                navegacao(i)



for key in dicionario:
    navegacao(key)
