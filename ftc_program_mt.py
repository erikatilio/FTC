# -----------------------------------------------------------------------------------------------------
#  UNIVERSIDADE DO ESTADO DO AMAZONAS
#  FUNDAMENTOS TEORICOS DA COMPUTAÇAO UEA 2019.1 - PROJETO 03
#  Prof. Dr. Elloa Barreto Guedes da Costa
#  Aluno(a): Erik Atilio Silva Rey       Matricula: 1715310059       Curso: Sistemas de Informaçao
# -----------------------------------------------------------------------------------------------------
import ast

#  ESTRUTURA DA MAQUINA DE TURING
class maquina_turing():
    def __init__(self, expressao):
        self.delta = []
        # Converte as tuplas em lista para o delta.
        for i in expressao['delta']:
            self.delta.append(list(i))
        self.fita = []
        self.branco = 'b'
        self.posicao_cabecote = 0
        self.estado_inicial = expressao['inicial']
        self.estado_atual = self.estado_inicial
        self.estado_aceitacao = expressao['aceita']

    #  LER ITEM NA POSICAO ATUAL DO CABECOTE
    def ler_item_na_fita(self):
        return self.fita[self.posicao_cabecote]

    #  IMPRIME A FITA
    def imprimir_fita(self):
        for i in self.fita:
            # Remove os brancos da fita na impressao.
            if(i == 'b'):
                print("", end="")
            else:
                print(i, end="")

    #  LIMPA A FITA
    def limpar_fita(self):
        del self.fita[:]
        self.posicao_cabecote = 0
        self.troca_estado_atual(self.estado_inicial)

    #  TROCA O ESTADO ATUAL DA FITA
    def troca_estado_atual(self, estado):
        self.estado_atual = estado

    #  ESCREVE NA FITA O ITEM NA POSICAO DO CABECOTE
    def escreve_item_na_fita(self, item):
        self.fita[self.posicao_cabecote] = item

    #  MOVE CABECOTE NA FITA
    def move_cabecote(self, movimento):
        if(movimento == 'D'):
            self.posicao_cabecote += 1
            # Caso o movimento seja alem do limite da lista para a direita.
            if(self.posicao_cabecote > len(self.fita)-1):
                self.fita.append(self.branco)
        elif(movimento == 'E'):
            self.posicao_cabecote -= 1
            # Caso o movimento seja alem do limite da lista para a esquerda.
            if(self.posicao_cabecote < 0):
                self.fita.insert(0, self.branco)
                self.posicao_cabecote = 0
        elif(movimento == 'P'):
            self.posicao_cabecote = self.posicao_cabecote

    #  ESCREVER A PALAVRA NA FITA
    def escrever_palavra_na_fita(self, palavra):
        for i in palavra:
            self.fita.append(i)
        self.fita.append(self.branco) #  Adiciona o branco ao final da fita.

    #  ANALISA A PALAVRA
    def analisar_palavra(self, palavra):
        self.escrever_palavra_na_fita(palavra)
        contador = 0  # Contador para verificar se foi percorreu todo o delta.
        while(True):
            # Caso o estado atual seja de aceitacao.
            if(self.estado_atual == self.estado_aceitacao):
                self.imprimir_fita()
                print(" ACEITA")
                break
            # Caso o contador tenha percorrido todo o delta.
            if(contador == len(self.delta)):
                self.imprimir_fita()
                print(" REJEITA")
                break
            for aux in self.delta:
                contador += 1
                # Verifica se tem transicao no delta.
                if((self.estado_atual == aux[0])and(self.ler_item_na_fita() == aux[2])):
                    self.troca_estado_atual(aux[1])
                    self.escreve_item_na_fita(aux[3])
                    self.move_cabecote(aux[4])
                    contador = 0
                    break
        # Limpa a fita para que nao haja lixo.
        self.limpar_fita()

# -----------------------------------------------------------------------------------------------------

# Recebe o dicionario com a definicao da maquina de turing.
expressao = ast.literal_eval(input())
mt = maquina_turing(expressao)
# Recebe a quantidade de inputs.
vezes = int(input())
# Loop para receber os inputs dada a quantidade.
while(vezes != 0):
    palavra = input()
    mt.analisar_palavra(palavra)
    vezes -= 1