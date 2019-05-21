# -----------------------------------------------------------------------------------------------------
#  UNIVERSIDADE DO ESTADO DO AMAZONAS
#  FUNDAMENTOS TEORICOS DA COMPUTAÇAO UEA 2019.1 - PROJETO 02
#  Prof. Dr. Elloa Barreto Guedes da Costa
#  Aluno(a): Erik Atilio Silva Rey       Matricula: 1715310059       Curso: Sistemas de Informaçao
# -----------------------------------------------------------------------------------------------------

#  ESTRUTURA DA PILHA
class Pilha():
    def __init__(self):
        self.lista = []

    #  VERIFICA SE A PILHA ESTA' VAZIA
    def vazia(self):
        if (len(self.lista) == 0):
            return True
        else:
            return False

    #  RETORNA O ULTIMO ELEMENTO DA PILHA
    def topo(self):
        return self.lista[len(self.lista)-1]

    #  EMPILHA ELEMENTO NO TOPO DA PILHA
    def empilhar(self, elemento):
        self.lista.append(elemento)

    #  DESEMPILHA ELEMENTO DO TOPO DA PILHA
    def desempilhar(self):
        return self.lista.pop()

#  FUNCAO PARA VERIFICAR IGUALDADE DE CASAMENTO
def igual(i):
    #  Verifica se 'i' e' um dos casamentos
    if((i == '()')or(i == '{}')or(i == '[]')):
        return True
    else:
        return False

#  FUNCAO PARA CASAR ABERTURA E FECHAMENTO DE EXPRESSAO
def casar(expressao):
    pilha = Pilha()
    for i in expressao:
        #  Verifica se 'i' e' um elemento de abrir, se sim, empilha 'i' na pilha.
        if((i == '(')or(i == '{')or(i == '[')):
            pilha.empilhar(i)

        #  Verifica se 'i' e' um elemento de fechar.
        elif((i == ')')or(i == '}')or(i == ']')):
            #  Verifica se a pilha esta' vazia, para no caso a expressao começar com um elemento de fechar.
            if(pilha.vazia() == True):
                return False

            #  Recebe o elemento do topo da pilha.
            topo_pilha = pilha.topo()
            #  Verifica o topo da pilha concatenado com o elemento 'i' casam, se sim desempilha.
            if(igual(topo_pilha+i) == True):
                pilha.desempilhar()

    #  Se nao houver mais elementos na pilha, 'True', senao, 'False'.
    if(pilha.vazia() == True):
        return True
    else:
        return False

#  Armazena as expressoes.
expressoes = []

#  RECEBE OS INPUTS
while True:
    expressao = input()
    #  Caso seja vazio para encerrar os inputs.
    if(expressao == ''):
        break
    else:
        #  Adiciona a lista de expressoes e verifica expressao.
        expressoes.append(expressao)
        print(casar(expressao))
#  Junta todos os elementos da lista expressoes.
resultado = ''.join(expressoes)
print(casar(resultado))
