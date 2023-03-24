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
        if word == "&": # equivalente a ::= da bnf
            flag = 1
        elif word != "|" and flag == 0:
            dicionario[word] = Node(word) # a palavra é um nó
            aux = word
        elif flag == 1:
            dicionario[aux].add_child(word)
    flag = 0

#for key in dicionario:
    #print(key)
    #print(dicionario[key].children)


excecoes1 = ["<id>", "<real_num>", "<integer_num>"]

excecoes2 = [ "<tipo_var>","<rotina>"  , "<tipo_funcao>"  , "<comando>" , "<condicao>"  , "<expressao>"  
            , "<relacao>"  , "<expressao_num>"  , "<operando>"  , "<operador>"  , "<termo>"  , "<expressao_fila>"  , "<conteudo>" , "<opFila>" ]


class ExcecSpecial(object):
    def __init__(self):
        self.contador = 1
        self.flag = 0

def validId(id):
    if id[0].isnumeric():
        return False
    return True
    
def Error(key,i):
    global aux
    if key == "<comando>" and i ==":=":
        aux = aux - 1
        return
    print("ERROR " + tabela_tokens[aux].name)
    exit()

aux = 0
#aux2 = 1
flag = 0
flag2 = 0
flag3 = 0
contador = 0
backup = ""
backup2 = "start"

excecoesspecial = {}

for i in excecoes2:
    excecoesspecial[i] = ExcecSpecial()

excecoesspecial["start"] = ExcecSpecial()

def navegacao(key):
    global aux, flag ,flag2,flag3, backup, backup2, contador
    if "|" in dicionario[key].children:
        flag2 = 1
        backup = key
    for i in dicionario[key].children:
        #print("\n")
        #print(key + " " + i)
        #print(tabela_tokens[aux].name + " flag2: " + str(flag2))
        #print("*"+backup + "*")
        if i == "<empty>":
            flag2 = 1
            break
        if aux == len(tabela_tokens):
            if tabela_tokens[aux - 1].name != "end":                
                Error(key,i)
            print("aadadad")
            exit()
        if flag3 == 1 and backup != "":
            print("aa")
            if backup == key:
                flag3 = 0
                backup = ""
            break
        if (i[0] != "<" or i == "<") and i != "|":
            if i != tabela_tokens[aux].name:
                if flag == 1:
                    break
                if flag2 == 1:
                    if backup != key and backup != "":
                        flag3 = 1
                    flag2 = 0
                    break               
                Error(key,i)
                flag = 1
                break
            else:
                aux = aux + 1
                if flag == 1:
                    flag = 0
                if flag2 == 1:
                    flag2 = 0
        elif i !="|" and i!="<empty>":
            if i in excecoes1 or i in excecoes2:
                if i =="<id>":
                    if not validId(tabela_tokens[aux].name):
                        if flag == 1:
                            break
                        if flag2 == 1:
                            if backup != key and backup != "":
                                flag3 = 1
                            flag2 = 0
                            break                     
                        Error(key,i)
                    if tabela_tokens[aux].tipo == "Id":
                        aux = aux + 1
                        if flag == 1:
                            flag = 0
                        if flag2 == 1:
                            flag2 = 0
                    else:
                        if flag == 1:
                            break
                        if flag2 == 1:
                            if backup != key and backup != "":
                                flag3 = 1
                            flag2 = 0
                            break
                        else:
                            Error(key,i)
                elif i =="<integer_num>":
                    if tabela_tokens[aux].name == "+" or tabela_tokens[aux].name == "+":
                        aux = aux + 1
                    if tabela_tokens[aux].tipo == "Number":
                        aux = aux + 1
                        if flag == 1:
                            flag = 0
                        if flag2 == 1:
                            flag2 = 0
                    else:
                        if flag == 1:
                            break
                        if flag2 == 1:
                            if backup != key and backup != "":
                                flag3 = 1
                            flag2 = 0
                            break
                        else:
                            Error(key,i)
                elif i =="<real_num>":
                    if tabela_tokens[aux].name == "+" or tabela_tokens[aux].name == "+":
                        aux = aux + 1
                    if tabela_tokens[aux].name.strip(".").isnumeric() == False:
                        if flag == 1:
                            break
                        if flag2 == 1:
                            if backup != key and backup != "":
                                flag3 = 1
                            flag2 = 0
                            break
                        Error(key,i)
                    if tabela_tokens[aux].tipo == "Real":
                        aux = aux + 1
                        if flag == 1:
                            flag = 0
                        if flag2 == 1:
                            flag2 = 0
                    else:
                        if flag == 1:
                            break
                        if flag2 == 1:
                            if backup != key and backup != "":
                                flag3 = 1
                            flag2 = 0
                            break
                        else:
                            Error(key,i)                      
                else:
                    mark = flag2
                    flag2 = 0
                    backup3 = backup2
                    backup2 = i
                    if flag == 1:
                        contador = contador + 1
                    flag = 1
                    while((i + str(excecoesspecial[backup2].contador)) in dicionario) and flag == 1:
                        #print(dicionario[i + str(excecoesspecial[backup2].contador)].children)
                        #print(tabela_tokens[aux].name)
                        navegacao(i + str(excecoesspecial[backup2].contador))
                        excecoesspecial[backup2].contador = excecoesspecial[backup2].contador + 1
                    if mark == 0 and flag2 == 0 and (i + str(excecoesspecial[backup2].contador)) not in dicionario and flag == 0:
                        Error(key,i) 
                    if contador > 0:
                        contador = contador - 1
                    if contador == 0:
                        flag = 0
                    flag2 = mark
                    excecoesspecial[backup2].contador = 1
                    backup2 = backup3
            else:    
                navegacao(i)
                



for key in dicionario:
    navegacao(key)
