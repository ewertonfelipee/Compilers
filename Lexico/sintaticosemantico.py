from lexicofinal import tabela_tokens
import operator

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

class Variavel():
    def __init__(self, name, categoria, escopo, tipo, valor):
        self.name = name
        self.categoria = categoria
        self.escopo = escopo
        self.tipo = tipo
        self.valor = valor
        self.valorlista = []
        self.parametro = False
        self.ordem = []

dicionario = {}

arquivo = open("bnf2.txt", "r")

flag = 0

aux = ""

for line in arquivo:
    for word in line.split():
        if word == "&": # equivalente a ::= da bnf
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


excecoes1 = ["<id>", "<real_num>", "<integer_num>"]

excecoes2 = [ "<tipo_var>","<rotina>"  , "<tipo_funcao>"  , "<comando>"  , "<expressao>"  
            , "<relacao>"   , "<operando>"  , "<operador>"  , "<termo>"  , "<expressao_fila>"  , "<conteudo>" , "<opFila>" ]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class ExcecSpecial(object):
    def __init__(self):
        self.contador = 1 

def validId(id):
    if id[0] in numbers or id[0] == "+" or id[0] == "-":
        return False
    return True

def validInt(num):
    if num[0] == "+" or num[0] == "-":
        num = num[1:]
    for i in num:
        if i not in numbers:
            return False
    return True

def validFloat(num):
    if num[0] == "+" or num[0] == "-":
        num = num[1:]
    for i in num:
        if i !="." and i not in numbers:
            return False
    return True
    
    
def Error(key,i):
    global aux
    if key == "<comando>7" and i == ":=":
        aux = aux - 1
        return
    print("Sintatico ERROR " + tabela_tokens[aux - 1].name)
    exit()

aux = 0 
flag = 0 
flag2 = 0 
flag3 = 0 
flag4 = 0 
contador = 0 
backup = "" 
backup2 = "start" 

excecoesspecial = {}

for i in excecoes2:
    excecoesspecial[i] = ExcecSpecial()

excecoesspecial["start"] = ExcecSpecial() 

def navegacao(key):
    global aux, flag ,flag2,flag3, flag4,backup, backup2, contador
    if "|" in dicionario[key].children: 
        flag2 = 1
        backup = key
    for i in dicionario[key].children: 
        #print("\n")
        #print(key + " " + i)
        #print(tabela_tokens[aux].name + " flag: " + str(flag) + " flag2: " + str(flag2))
        #print("*"+backup + "*")
        if i == "<empty>":
            flag2 = 1
            break
        if aux == len(tabela_tokens):
            if tabela_tokens[aux - 1].name != "end" or key != "<corpo>":       
                Error(key,i)
            print("Sintatico Sucess")
            criartabela()
            exit()
        if flag4 == 1:
            #print("aaa")
            break
        if flag3 == 1 and backup != "":
            #print("aa")
            if backup == key:
                flag3 = 0
                backup = ""
            break
        if (i[0] != "<" or i == "<" or i == "<=") and i != "|": 
            if i != tabela_tokens[aux].name:
                if i =="end":
                    Error(key,i)
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
                    if validId(tabela_tokens[aux].name.strip()) == False:
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
                    if validInt(tabela_tokens[aux].name.strip()) == False:
                        if flag == 1:
                            break
                        if flag2 == 1:
                            if backup != key and backup != "":
                                flag3 = 1
                            flag2 = 0
                            break
                        Error(key,i)
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
                    if validFloat(tabela_tokens[aux].name.strip()) == False:
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
                    #mark = flag2
                    #flag2 = 0
                    aux2 = aux 
                    backup3 = backup2
                    backup2 = i
                    contador = contador + 1
                    flag = 1
                    while((i + str(excecoesspecial[backup2].contador)) in dicionario) and flag == 1:
                        flag4 = 0
                        #print(dicionario[i + str(excecoesspecial[backup2].contador)].children)
                        #print(tabela_tokens[aux].name)
                        navegacao(i + str(excecoesspecial[backup2].contador))
                        excecoesspecial[backup2].contador = excecoesspecial[backup2].contador + 1
                    if contador > 0:
                        contador = contador - 1
                    if contador == 0:
                        flag = 0
                    #mark ==0
                    if flag2 == 0 and (i + str(excecoesspecial[backup2].contador)) not in dicionario  and aux2 == aux:
                        if flag==0:
                            Error(key,i) 
                        else:
                            flag4 = 1
                    #flag2 = mark
                    excecoesspecial[backup2].contador = 1
                    backup2 = backup3
            else: 
                navegacao(i)
                
variaveis = []
variaveisnomes = []

i = 0
auxliar = 0

def checkId(id, escopos):
    aux = 0
    if id not in variaveisnomes:
        return -1, -1 
    else:
        contador = variaveisnomes.count(id)
    for j in variaveis:
        if j.name == id:
            contador = contador - 1
            if j.escopo != escopos[-1] and j.escopo != "global":
                #print(j.name + " " + j.escopo + " " + escopos[-1])
                if contador > 0:
                    aux = aux + 1
                    continue
                return -1 , -1 #erro
            if j.categoria == "procedure" or j.categoria == "function":
                return aux , 1 
            return aux , 0
        aux = aux + 1

def navegarvariaveis( escopos, aux):
    global i, auxliar
    while ( tabela_tokens[i].name != ":"):
        if tabela_tokens[i].name != ",":
            if tabela_tokens[i].name in variaveisnomes:
                for j in variaveis:
                    if j.name == tabela_tokens[i].name:
                        if j.escopo == escopos[-1] or j.escopo == "global":
                            print("ERROR SEMANTICO")
                            exit()
            variaveis.append(Variavel( tabela_tokens[i].name, "variavel", escopos[-1] , "null", "null")) 
            variaveisnomes.append(tabela_tokens[i].name)
            aux = aux + 1
        i = i + 1
    i = i + 1
    for j in range(1, aux):
        if (variaveis[auxliar-1].parametro == True):
            variaveis[auxliar-1].ordem.append(tabela_tokens[i].name)
        variaveis[-j].tipo = tabela_tokens[i].name
    i = i + 2
    aux = 1
    if tabela_tokens[i].tipo == "Id":
        navegarvariaveis( escopos, aux)

def criartabela():
    global i, auxliar
    escopos = []
    escopos.append("global")
    aux = 1
    contadorEnd = 0
    contadorEnd2 = 0
    while (i < len(tabela_tokens)):
        if tabela_tokens[i].name == "var":
            i = i + 1
            navegarvariaveis( escopos, aux)
            aux = 1
            i = i - 1
        elif tabela_tokens[i].name == "procedure":
            i = i + 1
            if tabela_tokens[i].name in variaveisnomes:
                print("ERROR SEMANTICO")
                exit()
            variaveis.append(Variavel( tabela_tokens[i].name, "procedure", escopos[-1] , "null", "null")) 
            variaveisnomes.append(tabela_tokens[i].name)
            escopos.append(tabela_tokens[i].name)
            contadorEnd = contadorEnd + 1
            i = i + 2
            if tabela_tokens[i].tipo == "Id":
                #ativar flag global que esta lendo variaveis de parametro
                auxliar = len(variaveis)
                variaveis[auxliar-1].parametro = True
                navegarvariaveis( escopos, aux)
                auxliar = 1
            else:
                i = i - 1
        elif tabela_tokens[i].name == "function":
            i = i + 1
            if tabela_tokens[i].name in variaveisnomes:
                print("ERROR SEMANTICO")
                exit()
            variaveis.append(Variavel( tabela_tokens[i].name, "function", escopos[-1] , "null", "null")) 
            variaveisnomes.append(tabela_tokens[i].name)
            escopos.append(tabela_tokens[i].name)
            contadorEnd = contadorEnd + 1
            i = i + 2
            if tabela_tokens[i].tipo == "Id":
                auxliar = len(variaveis)
                variaveis[auxliar-1].parametro = True
                functionaux = i
                while ( tabela_tokens[functionaux].name != ")"):
                    functionaux = functionaux + 1
                functionaux = functionaux + 2
                variaveis[-1].tipo = tabela_tokens[functionaux].name
                navegarvariaveis( escopos, aux)
                auxliar = 1
            else:
                variaveis[-1].tipo = tabela_tokens[i].name
        elif tabela_tokens[i].name == "begin":
            i = i + 1 #pode dar erro no semantico, begin;;;;
            contadorEnd2 = contadorEnd2 + 1
            while contadorEnd2 > 0:
                if tabela_tokens[i].tipo == "Id" and tabela_tokens[i + 1].name == ":=":
                    aux2, flag = checkId(tabela_tokens[i].name , escopos)
                    if aux2 >= 0 and flag == 0:
                        i = i + 2
                        if tabela_tokens[i].tipo == "Number":
                            #print("aaaaaaaaaaa " + variaveis[aux2].name)
                            if variaveis[aux2].tipo != "integer":
                                print("ERROR SEMANTICO")
                                exit()
                            variaveis[aux2].valor = tabela_tokens[i].name
                        elif tabela_tokens[i].tipo == "Real":
                            if variaveis[aux2].tipo != "real":
                                print("ERROR SEMANTICO")
                                exit()
                            variaveis[aux2].valor = tabela_tokens[i].name
                        elif tabela_tokens[i].tipo == "Operator" or tabela_tokens[i].tipo == "Reserved Word":
                            operacao = tabela_tokens[i].name
                            if (operacao == "input" or operacao == "length" or operacao == "inverte" or operacao == "concatena" or operacao == "output") and  (variaveis[aux2].tipo =="integer" or  variaveis[aux2].tipo =="real"):
                                print("ERROR SEMANTICO")
                                exit()
                            i = i + 2
                            if tabela_tokens[i].tipo == "Id":
                                aux3, flag2  = checkId(tabela_tokens[i].name , escopos)
                                if aux3 ==-1 and flag2 == -1:
                                    print("ERROR SEMANTICO")
                                    exit()
                                if variaveis[aux3].valor == "null":
                                    print("ERROR SEMANTICO")
                                    exit()
                                valor1 = [ variaveis[aux3].valor, variaveis[aux3].tipo.lower()]
                                if variaveis[aux3].tipo == "integer":
                                    valor1[0] = int(valor1[0])
                                else:
                                    valor1[0] = float(valor1[0])
                            else:
                                if tabela_tokens[i].tipo == "Number":
                                    valor1 = [ tabela_tokens[i].name , "integer"]
                                    valor1[0] = int(valor1[0])
                                else:
                                    valor1 = [ tabela_tokens[i].name , tabela_tokens[i].tipo.lower()]
                                    valor1[0] = float(valor1[0])
                            i = i + 2
                            ###
                            if tabela_tokens[i].tipo == "Id":
                                aux3, flag2 = checkId(tabela_tokens[i].name , escopos)
                                if aux3 ==-1 and flag2 == -1:
                                    print("ERROR SEMANTICO")
                                    exit()
                                if variaveis[aux3].valor == "null":
                                    print("ERROR SEMANTICO")
                                    exit()
                                valor2 = [ variaveis[aux3].valor, variaveis[aux3].tipo.lower()]
                                if variaveis[aux3].tipo == "integer":
                                    valor2[0] = int(valor2[0])
                                else:
                                    valor2[0] = float(valor2[0])
                            else:
                                if tabela_tokens[i].tipo == "Number":
                                    valor2 = [ tabela_tokens[i].name , "integer"]
                                    valor2[0] = int(valor2[0])
                                else:
                                    valor2 = [ tabela_tokens[i].name , tabela_tokens[i].tipo.lower()]
                                    valor2[0] = float(valor2[0])
                            if valor1[1] != valor2[1]:
                                print("ERROR SEMANTICO")
                                exit()
                            if variaveis[aux2].tipo != valor1[1]:
                                if (variaveis[aux2].tipo == "fila_of_integer" and valor1[1] == "integer") or (variaveis[aux2].tipo == "fila_of_real" and valor1[1] == "real"):
                                    print("")
                                else:
                                    print("ERROR SEMANTICO")
                                    exit()
                            if operacao == "+":
                                variaveis[aux2].valor = valor1[0] + valor2[0]                      
                            elif operacao == "-":
                                variaveis[aux2].valor = valor1[0] - valor2[0]
                            elif operacao == "*":
                                variaveis[aux2].valor = valor1[0] * valor2[0]
                            elif operacao == "/":
                                variaveis[aux2].valor = valor1[0] / valor2[0]
                            elif operacao == "%":
                                variaveis[aux2].valor = valor1[0] % valor2[0]
                            elif operacao == "concatena":
                                variaveis[aux2].valorlista = [valor1[0] , valor2[0]]
                            else:
                                variaveis[aux2].valor = "PLACEHOLDER"
                        elif tabela_tokens[i].tipo == "Id":
                            aux3, flag2 = checkId(tabela_tokens[i].name , escopos)
                            if aux3 ==-1 and flag2 == -1:
                                print("ERROR SEMANTICO")
                                exit()
                            if variaveis[aux3].valor == "null":
                                print("ERROR SEMANTICO")
                                exit()
                            variaveis[aux2].valor =  variaveis[aux3].valor
                    elif aux2 >= 0  and flag == 1:
                        print("ERROR SEMANTICO")
                        exit()
                    elif aux2 ==-1 and flag == -1:
                        print("ERROR SEMANTICO")
                        #print(tabela_tokens[i].name)
                        exit()
                elif (tabela_tokens[i].tipo == "Id" and (tabela_tokens[i + 1].name == ";" or tabela_tokens[i + 1].name == "(") and tabela_tokens[i - 1].name != "to"):
                    aux2, flag = checkId(tabela_tokens[i].name , escopos)
                    if aux2 >= 0  and flag == 1:
                        if variaveis[aux2].parametro == True and tabela_tokens[i + 1].name == ";":
                            print("ERROR SEMANTICO")
                            exit()
                        elif variaveis[aux2].parametro == True and tabela_tokens[i + 1].name == "(":
                            i = i + 2
                            #print(variaveis[aux2].ordem)
                            for k in variaveis[aux2].ordem:
                                if tabela_tokens[i].tipo == "Real":
                                    if k != "real":
                                        print("ERROR SEMANTICO")
                                        exit()
                                elif tabela_tokens[i].tipo == "Number":
                                    if k != "integer":
                                        print("ERROR SEMANTICO")
                                        exit()
                                elif tabela_tokens[i].tipo == "Id":
                                    aux3, flag2 = checkId(tabela_tokens[i].name , escopos)
                                    if aux3 ==-1 and flag2 == -1:
                                        print("ERROR SEMANTICO")
                                        exit()
                                    if variaveis[aux3].valor == "null":
                                        print("ERROR SEMANTICO")
                                        exit()
                                    if variaveis[aux3].tipo != k:
                                        print("ERROR SEMANTICO")
                                        exit()
                                if tabela_tokens[i].name == ";":
                                    print("ERROR SEMANTICO")
                                    exit()
                                i = i + 2
                            if tabela_tokens[i].name != ";":
                                print("ERROR SEMANTICO")
                                exit()
                                
                                
                    else:
                        print("ERROR SEMANTICO")
                        exit()
                i = i + 1   
                if tabela_tokens[i].name == "begin":
                    contadorEnd2 = contadorEnd2 + 1
                if tabela_tokens[i].name == "end":
                    contadorEnd2 = contadorEnd2 - 1             
            if tabela_tokens[i].name == "end" and contadorEnd != 0:
                contadorEnd = contadorEnd - 1
                escopos.pop()

        i = i + 1  

    print("SEMANTICO SUCESSO")

    symbols = open("Symbols-table.txt", "w")

    variaveisorted = sorted(variaveis,key = operator.attrgetter('escopo'))

    troca = "global"
    symbols.write("Nome - Categoria - Escopo - Tipo - Valor\n")
    symbols.write("-------------------------------------------------------------------------------------------------------------\n")
    for i in variaveisorted:
        if i.escopo != troca:
            symbols.write("-------------------------------------------------------------------------------------------------------------\n")
        if i.tipo == "fila_of_integer" or i.tipo == "fila_of_real":
            symbols.write(i.name + " " + i.categoria + " " + i.escopo + " " + i.tipo + " " + str(i.valorlista) + "\n")
        else:
            symbols.write(i.name + " " + i.categoria + " " + i.escopo + " " + i.tipo + " " + str(i.valor) + "\n")
        troca = i.escopo
    symbols.write("-------------------------------------------------------------------------------------------------------------\n")
    symbols.close()

#falta verificar parametros na chamada de funcoes, completar calculos para variaveis de fila?
#tratar opfila e inverte


for key in dicionario:
    navegacao(key)




