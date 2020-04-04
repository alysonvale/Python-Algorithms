# TESTE PASSAGEM
# CRIANDO O TABULEIRO DE DAMAS
def tabuleiro_de_damas():
    tabuleiro_de_damas = [[], [], [], [], [], [], [], []]
    for i in range(len(tabuleiro_de_damas)):  # CRIANDO COLUNA
        for e in range(len(tabuleiro_de_damas)):  # CRIANDO LINHAS
            if ((i == 0) or (i == 2)) and (e % 2 == 0):  # VERIFICA POSIÇÃO E SE TIVER COLOCA
                tabuleiro_de_damas[i].append("B")
            elif ((i == 1) and (e % 2 != 0)):
                tabuleiro_de_damas[i].append("B")


            elif (i == 5 or i == 7) and (e % 2 != 0):
                tabuleiro_de_damas[i].append("P")
            elif (i == 6) and (e % 2 == 0):
                tabuleiro_de_damas[i].append("P")
            else:
                tabuleiro_de_damas[i].append("-")
    return (tabuleiro_de_damas)


tabuleiro_de_damas()
tabuleiro = []
tabuleiro = tabuleiro_de_damas()

dicio = {}
dicio = {"A": 0,
         "a": 0,
         "B": 1,
         "b": 1,
         "C": 2,
         "c": 2,
         "D": 3,
         "d": 3,
         "E": 4,
         "e": 4,
         "F": 5,
         "f": 5,
         "G": 6,
         "g": 6,
         "H": 7,
         "h": 7}


def movimentoDo_B_P():
    atual_x_linha = (input("Digite o número da linha atual:"))
    while (atual_x_linha.isdigit() != True):
        atual_x_linha = input("Erro! Digite o número da linha atual:")
    atual_x_linha = int(atual_x_linha)
    atual_linha_x = atual_x_linha - 1
    atual_y_coluna = input("Digite a letra da coluna atual:")

    futura_x_linha = input("Digite o número da linha futura:")
    while (futura_x_linha.isdigit() != True):
        futura_x_linha = input("Erro! Digite o número da linha futura:")
    futura_x_linha = int(futura_x_linha)
    futura_linha_x = futura_x_linha - 1  # O VALOR DO NUMERO PROPOSTO É MAIOR, ENTÃO TIRO MENOS 1
    futura_y_coluna = input("Digite a letra da linha futura:")
    return (atual_linha_x, atual_y_coluna, futura_linha_x, futura_y_coluna)


def impressao_tabuleiro(tabuleiro):
    print()
    print('    A B C D E F G H')
    print("    ———————————————")

    for i in range(len(tabuleiro)):
        for e in range(len(tabuleiro[i])):
            if (e == 0):
                print(i + 1, end=' | ')
            print(tabuleiro[i][e], end=" ")
        print()


def jogando_damas():
    x_matar = 0
    y_matar = 0
    futuro_b_x = 0
    futuro_b_y = 0

    contador = 1
    pecas_comidas_primeiro_jogador = 0
    pecas_comidas_segundo_jogador = 0
    while ((pecas_comidas_primeiro_jogador != 12) or (
            pecas_comidas_segundo_jogador != 12)):  # Está condição é inicialmente por enquanto.

        impressao_tabuleiro(tabuleiro)
        print()
        print("PONTUAÇÃO")
        print("JOGADOR B: %d" % pecas_comidas_primeiro_jogador)
        print("JOGADOR P: %d" % pecas_comidas_segundo_jogador)
        # OS DOIS IFs SÃO PARA DIZER QUEM JOGARÁ PRIMEIRO
        if (contador % 2 != 0):
            print()
            print("Vez do B!")
            print()

            atual_x, atual_y, futuro_x, futuro_y = (movimentoDo_B_P())
            coluna_atual = (dicio["%s" % atual_y])
            #
            coluna_atual = int(coluna_atual)
            coluna_futura = (dicio["%s" % futuro_y])
            coluna_futura = int(coluna_futura)
            #
            futura_B_x = atual_x + 1  # PARA TESTAR SE PODE IR PARA A DIOGONAL POR EXEMPLO (3,1)
            futura_B_y = coluna_atual + 1  # PARA TESTAR A LINHA
            futura_B_y_2 = coluna_atual - 1
            #
            futura_fut_B_x = futura_B_x + 1
            futura_fut_B_y = futura_B_y + 1
            futura_fut_B_y_2 = futura_fut_B_y - 1

        if (contador % 2 == 0):
            print()
            print("Vez do P!")
            print()

            # PARA FAZER OS MOVIMENTOS DOS DOIS JOGADORES SÓ COM UMA FUNÇÃO
            atual_x, atual_y, futuro_x, futuro_y = (movimentoDo_B_P())
            coluna_atual = (dicio["%s" % atual_y])  # PUXA O VALOR DO DICIONARIO
            # TRANSFORMA OS VALORES
            coluna_atual = int(coluna_atual)
            coluna_futura = (dicio["%s" % futuro_y])
            coluna_futura = int(coluna_futura)
            #

        for i in ((tabuleiro)):  # ESSE FOR É PARA LER O TABULEIRO PARA FAZER AS JOGADAS ABAIXO

            if ((atual_x % 2 == 0) and (
                    coluna_atual % 2 == 0)):  # ESSE IF É PARA PRIMEIRA JOGADA DE B, MAS IRÁ VIRAR PARA P
                if ((futuro_x % 2 == 1) and (coluna_futura % 2 == 1)):  # FUTURA CASA QUE IRÁ

                    if ((tabuleiro[atual_x][coluna_atual]) == "B") and (
                            contador % 2 != 0):  # VEZ DEPENDE DO CONTADOR E SÓ UMA JOGADA

                        if ((tabuleiro[futuro_b_x][futuro_b_y]) != "P"):
                            if (tabuleiro[atual_x][coluna_atual]) != (tabuleiro[futuro_x][coluna_futura]) and (
                                    atual_x < futuro_x):
                                if (tabuleiro[futuro_x][coluna_futura] != "P"):
                                    tabuleiro[atual_x][coluna_atual] = "-"
                                    tabuleiro[futuro_x][coluna_futura] = "B"
                                    contador += 1
                                    if ((futuro_x) == 7):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                        (tabuleiro[futuro_x][coluna_futura]) = "b"
                                elif (tabuleiro[futuro_x][coluna_futura] == "P" or (
                                        futuro_x == atual_x)):  # SE O B JOGAR ERRADO
                                    atual_x, atual_y, futuro_x, futuro_y = (
                                        movimentoDo_B_P())  # PEDE AS INFORMAÇÕES PARA JOGAR NOVAMENTE


                    elif ((tabuleiro[atual_x][coluna_atual]) == "P") and (contador % 2 == 0):
                        if (tabuleiro[atual_x][coluna_atual]) != (tabuleiro[futuro_x][coluna_futura]) and (
                                atual_x > futuro_x):
                            if (tabuleiro[futuro_x][coluna_futura] != "B"):
                                tabuleiro[atual_x][coluna_atual] = "-"
                                tabuleiro[futuro_x][coluna_futura] = "P"
                                contador += 1
                                if ((futuro_x) == 0):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                    (tabuleiro[futuro_x][coluna_futura]) = "p"
                            elif (tabuleiro[futuro_x][coluna_futura] == "B") or (atual_x == futuro_x):
                                atual_x, atual_y, futuro_x, futuro_y = (movimentoDo_B_P())

                if ((futuro_x % 2 == 0) and (coluna_futura % 2 == 0)):  # PARA PULAR DUAS CASAS PARA MATAR

                    if coluna_futura - coluna_atual < 0:
                        x_matar = atual_x - 1
                        y_matar = coluna_atual - 1

                    else:
                        x_matar = atual_x - 1
                        y_matar = coluna_atual - 1

                    if (tabuleiro[atual_x][coluna_atual]) == "P" and (contador % 2 == 0):  # PARA MATAR

                        if ((tabuleiro[x_matar][y_matar]) == "B"):  # SABER SE É B
                            if (tabuleiro[atual_x][coluna_atual]) != (tabuleiro[futuro_x][coluna_futura]):
                                if (tabuleiro[futuro_x][coluna_futura] != "B"):
                                    tabuleiro[x_matar][y_matar] = "-"
                                    tabuleiro[futuro_x][coluna_futura] = "P"
                                    tabuleiro[atual_x][coluna_atual] = "-"
                                    pecas_comidas_segundo_jogador += 1
                                    contador += 1
                                    if ((futuro_x) == 0):  # JOGADA DE MATAR EM QUE A PEÇA VIRA RAINHA
                                        (tabuleiro[futuro_x][coluna_futura]) = "p"

                    if (tabuleiro[atual_x][coluna_atual]) == "B" and (contador % 2 != 0):
                        if coluna_futura - coluna_atual < 0:
                            x_matar = atual_x - 1
                            y_matar = coluna_atual - 1

                        if coluna_futura - coluna_atual > 0:  # PARA O JOGADOR B VOLTAR PARA MATAR
                            x_matar = atual_x + 1
                            y_matar = coluna_atual + 1
                        if ((tabuleiro[x_matar][y_matar]) == "P") and (
                                y_matar < 7):  # QUANDO EU TIVER EM UMA POSIÇÃO PAR E MINHA PEÇA PRECISAR COMER PARA TRÁS
                            if (tabuleiro[atual_x][coluna_atual]) != (tabuleiro[futuro_x][coluna_futura]):
                                if (tabuleiro[futuro_x][coluna_futura] != "P"):
                                    tabuleiro[atual_x][coluna_atual] = "-"
                                    tabuleiro[futuro_x][coluna_futura] = "B"
                                    tabuleiro[x_matar][y_matar] = "-"
                                    pecas_comidas_primeiro_jogador += 1
                                    contador += 1


            # ENTRADA DO P/B
            elif ((atual_x % 2 == 1) and (coluna_atual % 2 == 1)):  # QUANDO O JOGO COMAÇAR O P VAI SER IMPAR E O B PAR
                if ((futuro_x % 2 == 0) and (coluna_futura % 2 == 0)):  # UMA JOGADA POR VEZ

                    if (tabuleiro[atual_x][coluna_atual]) == "P" and (contador % 2 == 0):  # JOGADA DE P INICIAL
                        if (tabuleiro[atual_x][coluna_atual]) != (tabuleiro[futuro_x][coluna_futura]) and (
                                atual_x > futuro_x):
                            if (tabuleiro[futuro_x][coluna_futura] != "B"):
                                tabuleiro[atual_x][coluna_atual] = "-"
                                tabuleiro[futuro_x][coluna_futura] = "P"
                                contador += 1
                                if ((futuro_x) == 0):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                    (tabuleiro[futuro_x][coluna_futura]) = "p"
                            elif (tabuleiro[futuro_x][coluna_futura] == "B") or (
                                    atual_x == futuro_x):  # SE P JOGAR ERRADO
                                atual_x, atual_y, futuro_x, futuro_y = (movimentoDo_B_P())

                    elif (tabuleiro[atual_x][coluna_atual]) == "B" and (contador % 2 != 0):
                        if ((tabuleiro[atual_x][coluna_atual]) == "B") and (
                                contador % 2 != 0):  # VEZ DEPENDE DO CONTADOR
                            if (tabuleiro[atual_x][coluna_atual]) != (tabuleiro[futuro_x][coluna_futura]) and (
                                    atual_x < futuro_x):
                                if (tabuleiro[futuro_x][coluna_futura] != "P"):
                                    tabuleiro[atual_x][coluna_atual] = "-"
                                    tabuleiro[futuro_x][coluna_futura] = "B"
                                    contador += 1
                                    if ((futuro_x) == 7):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                        (tabuleiro[futuro_x][coluna_futura]) = "b"
                                elif (tabuleiro[futuro_x][coluna_futura] == "P") or (
                                        atual_x == futuro_x):  # SE O B JOGAR ERRADO
                                    atual_x, atual_y, futuro_x, futuro_y = (
                                        movimentoDo_B_P())  # PEDE AS INFORMAÇÕES PARA JOGAR NOVAMENTE

                elif ((futuro_x % 2 == 1) and (coluna_futura % 2 == 1)):  # PARA PULAR DUAS CASAS PARA MATAR

                    if coluna_futura - coluna_atual < 0:
                        x_matar = atual_x + 1
                        y_matar = coluna_atual - 1

                    else:
                        x_matar = atual_x + 1
                        y_matar = coluna_atual + 1

                    if (tabuleiro[atual_x][coluna_atual]) == "B" and (contador % 2 != 0):

                        if ((tabuleiro[x_matar][y_matar]) == "P") and (y_matar < 7):
                            if (tabuleiro[atual_x][coluna_atual]) != (tabuleiro[futuro_x][coluna_futura]):
                                if (tabuleiro[futuro_x][coluna_futura] != "P"):
                                    tabuleiro[atual_x][coluna_atual] = "-"
                                    tabuleiro[futuro_x][coluna_futura] = "B"
                                    tabuleiro[x_matar][y_matar] = "-"
                                    pecas_comidas_primeiro_jogador += 1
                                    contador += 1
                                    if ((futuro_x) == 7):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                        (tabuleiro[futuro_x][coluna_futura]) = "b"
                    if (tabuleiro[atual_x][coluna_atual]) == "P" and (
                            contador % 2 == 0):  # JOGADA PARA MATAR NA VOLTA DA PEÇA
                        if coluna_futura - coluna_atual < 0:
                            x_matar = atual_x + 1
                            y_matar = coluna_atual + 1

                        else:
                            x_matar = atual_x + 1
                            y_matar = coluna_atual + 1

                        if (tabuleiro[atual_x][coluna_atual]) == "P" and (contador % 2 == 0):  # PARA MATAR

                            if ((tabuleiro[x_matar][y_matar]) == "B"):  # SABER SE É B
                                if (tabuleiro[atual_x][coluna_atual]) != (tabuleiro[futuro_x][coluna_futura]):
                                    if (tabuleiro[futuro_x][coluna_futura] != "B"):
                                        tabuleiro[x_matar][y_matar] = "-"
                                        tabuleiro[futuro_x][coluna_futura] = "P"
                                        tabuleiro[atual_x][coluna_atual] = "-"
                                        pecas_comidas_segundo_jogador += 1
                                        contador += 1

    if (pecas_comidas_primeiro_jogador) < (pecas_comidas_segundo_jogador):
        print("O VENCEDOR É O JOGADOR B!")("PONTAÇÃO: %d" % pecas_comidas_primeiro_jogador)
        print("O P PERDEU!")("PONTUAÇÃO: %d" % pecas_comidas_segundo_jogador)

    elif (pecas_comidas_primeiro_jogador) < (pecas_comidas_segundo_jogador):
        print("O VENCEDOR É O JOGADOR P!")("PONTUAÇÃO: %d" % pecas_comidas_segundo_jogador)
        print("O B PERDEU!")("PONTUAÇÃO: %d" % pecas_comidas_primeiro_jogador)


jogando_damas()
"""

FAZER AS FUNÇÕES PARA OS MOVIMENTOS -> FEITO
MOSTRAR QUEM É O VENCEDOR
if (pecas_comidas_primeiro_jogador)<(pecas_comidas_segundo_jogador):
    print("O VENCEDOR É O JOGADOR B!")("PONTAÇÃO: %d"%pecas_comidas_primeiro_jogador)
    print("O P PERDEU!") ("PONTUAÇÃO: %d"%pecas_comidas_segundo_jogador)

elif (pecas_comidas_primeiro_jogador)<(pecas_comidas_segundo_jogador):
    print("O VENCEDOR É O JOGADOR P!") ("PONTUAÇÃO: %d"%pecas_comidas_segundo_jogador)
    print("O B PERDEU!") ("PONTUAÇÃO: %d"%pecas_comidas_primeiro_jogador)

MOVIMENTOS DAS DAMAS
#TRANSFORMAR A PEÇA EM DAMA
if (tabuleiro[futuro_x][coluna_futura]) = "-" and (tabuleiro[atual_x][coluna_atual]) == "B" and ((tabuleiro[futuro_x]) == 7 ):
    (tabuleiro[futuro_x][coluna_futura]) = "b"

if (tabuleiro[futuro_x][coluna_futura]) = "-" and (tabuleiro[atual_x][coluna_atual]) == "P" and ((tabuleiro[futuro_x]) == 8 ) :
    (tabuleiro[futuro_x][coluna_futura]) = "p" 
JOGADA DA DAMA

NÃO VOLTAR PARA TRÁS 
VOLTAR PARA TRÁS PARA MATAR 

"""
