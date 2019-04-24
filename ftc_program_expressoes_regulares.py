#-----------------------------------------------------------------------------------------------------
#  UNIVERSIDADE DO ESTADO DO AMAZONAS
#  FUNDAMENTOS TEORICOS DA COMPUTAÇAO UEA 2019.1 - PROJETO 01
#  Prof. Dr. Elloa Barreto Guedes da Costa
#  Aluno(a): Erik Atilio Silva Rey       Matricula: 1715310059       Curso: Sistemas de Informaçao
#-----------------------------------------------------------------------------------------------------

import sys
import re

# ------------------------------------FUNÇOES-------------------------------------------

# Funçao de validaçao de CPF
def validar_cpf(cpf: str) -> bool:
    # Obte'm apenas os numeros do CPF, ignorando pontuações.
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Validaçao do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validaçao do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True

# Funçao para imprimir validaçao e fechar programa.
def fechar():
    print("CABECALHO INVALIDO")
    sys.exit()  # Fecha o programa.

# Funçao auxiliar de validaçao do cabeçalho.
def verificaçao(var: bool):
    if(var == True):
        fechar()

# --------------------------------------CABEÇALHO---------------------------------------

arquivo = open(input(""), "r")  # Abre o arquivo.
cabecalho_validacoes = 0  # Recebe o numero de validações do cabeçalho.

# NOME
# Expressao regular para validar nome.
nome_cab = re.compile(r"^Nome:\s[^0-9\s\+\*\.\|\(\)\$\{\}][a-zA-Z\s]{1,50}\S$")
# Termo is None que retorna True ou False caso valido seja  none(nao encontrou a ER)  ou nao(encontrou a ER).
#  Funcao readline() chama a linha 1, depois linha 2 conforme e' chamada sucessivamente.
valido = nome_cab.match(arquivo.readline()) is None
# Verifica o valor de valido para ver se fecha ou nao o programa.
verificaçao(valido)

# CPF
# Expressao regular para validar cpf.
cpf_cab = re.compile(r"^CPF:\s\d{3}\.\d{3}\.\d{3}\-\d{2}$")
valido = cpf_cab.search(arquivo.readline())
if valido:
    # Validaçao do CPF
    cpf_verificar = re.search(
        r"\d{3}\.\d{3}\.\d{3}\-\d{2}$", valido.string).group()
    cpf_verificado = validar_cpf(cpf_verificar)
    if(cpf_verificado == False):
        fechar()
else:
    fechar()

# MATRICULA
# Expressao regular para validar matricula.
matricula_cab = re.compile(r"^Matricula:\s\d{10}$")
valido = matricula_cab.match(arquivo.readline()) is None
verificaçao(valido)

# SEPARADOR
# Expressao regular para validar o separador.
separador_cab = re.compile(r"^[\-]{20}$")
valido = separador_cab.match(arquivo.readline()) is None
verificaçao(valido)

print("CABECALHO VALIDO")

# ---------------------------------LISTA DE DISCIPLINAS---------------------------------

diciplinas = arquivo.readlines()  # lista de disciplinas.
tam = len(diciplinas)  # Tamnho da lista de diciplinas.

if(tam != 0):
    linhas_invalidas = []  # Lista com o indice das linhas invalidas.
    somatorio = 0  # Recebe o somatorio de notas*creditos.
    credito = 0  # Recebe o credito atual.
    nota = 0  # Recebe a nota atual.
    somatorio_credito = 0  # Recebe o somatorio de todos os creditos.

    for i in range(0, tam):
        # Expressoes regulares para os elementos de validaçao da linha atual.
        semestre_letivo_ = r"^\d{4}/(1\-1|2\-2)"
        cod_disciplina_ = r"\sEST(ECP|BSI|LIC|BAS)\d{3}"
        nome_disciplina_ = r"\s(\"[a-zA-Z\s]+\d{1}\"|\"[a-zA-Z\s]+\S\")"
        nome_turma_ = r"\s(ECP|BSI|LIC|ENG)(\d{2}|TFP)\_T\d{2}"
        creditos_ = r"\s[0-9]{1}\,[0-9]{2}"
        notas_ = r"\s([0-9]{1}\.[0-9]{2}|10\.00)"
        status_ = r"\s(APROVADO$|REPROVADO$)"

        #  Verifica se os elementos da linha atual são válidos.
        linha_formato = re.compile(
            semestre_letivo_+cod_disciplina_+nome_disciplina_+nome_turma_+creditos_+notas_+status_)
        valido = linha_formato.search(diciplinas[i]) is None
        if valido != False:
            # Adiciona na lista o numero da linha invalida.
            linhas_invalidas.append(i+1)
            continue

        # Expressao regular da nota para validar com status.
        validar_nota = re.compile(r"[0-9]{1}\.[0-9]{2}|10\.00")
        # Expressao regular do status para validar.
        validar_status = re.compile(r"APROVADO$|REPROVADO$")

        # Converte a nota para float.
        nota = float(validar_nota.search(diciplinas[i]).group())
        # Converte status para string.
        status = str(validar_status.search(diciplinas[i]).group())

        #  Verifica se o status possui acordância com a nota.
        if(((nota < 6.00) and (status == 'APROVADO')) or (nota >= 6.00) and (status == 'REPROVADO')):
            linhas_invalidas.append(i+1)
            continue

        # Expressao regular para credito.
        credito_cre = re.compile(r"[0-9]{1}\,[0-9]{2}")
        # Recebe o credito da linha atual.
        credito = credito_cre.search(diciplinas[i]).group()
        # Converte credito para float.
        credito = float(re.sub(",", ".", credito))

        #  Calculo de somatorio sem divisao por total de creditos e soma os creditos.
        somatorio += nota*credito
        somatorio_credito += credito

    #  Imprime o numero das linhas invalidas encontradas se houver.
    if(len(linhas_invalidas) != 0):
        print("LINHAS INVALIDAS:")
        for i in linhas_invalidas:
            print("LINHA %02d" % i)

    #  Calcula o CRE das disciplinas validas.
    if(somatorio_credito != 0.00):
        somatorio = (somatorio/somatorio_credito)
    else:
        somatorio = somatorio/1
    print("CRE: {:.2f}".format(somatorio))

else:
    print("CRE: 0.00")

arquivo.close()  # Fecha o arquivo.