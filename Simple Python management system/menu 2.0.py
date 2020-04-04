#18/06/2018
import pickle
a=0
b=1
c=0
d=1
e=0
f=1
dicProduto={}
dicCliente={}
dicEstoque={}
dicCusto={}
dicFornecedor={}
dicFuncionario={}
dicVenda={}
valorTotal=0
custoTotal=0
dicTotal={}
from datetime import date
hj=date.today()
anoAtual=hj.year
valorap=0

def validacaoDia(dia):
    while dia.isdigit()!=True:
        dia=input("Inválido! Digite um número:")
def validacaoDeMes(mes):
    while mes.isdigit()!=True:
        mes=input("Inválido! Digite o mês novamente (número):")
    mes=int(mes)
def validacaoIdade(idade):
    while idade.isdigit()!=True:
        idade=input("Inválido! Digite idade novamente:")
    idade=int(idade)
def validacaoDecpf(cpf):
    valido = True
    numeros = [0,1,2,3,4,5,6,7,8,9]
    numerosStr = ["0","1","2","3","4","5","6","7","8","9"]
    cpf1 = []
    cpf2 = []
    

    if valido == True:
        for x in cpf:
            if x not in numerosStr:
                valido = False

    if valido == True:
        if len(cpf) != 11:
            valido = False

    if valido == True:
        for x in range(len(cpf)):
            cpf1.append(int(cpf[x]))
            cpf2.append(int(cpf[x]))


        soma1 = cpf1[0] * 10 + cpf1[1] * 9 + cpf1[2] * 8 + cpf1[3] * 7 + cpf1[4] * 6 + cpf1[5] * 5 + cpf1[6] * 4 + cpf1[7] * 3 + cpf1[8] * 2
        resto1 = (soma1*10)%11

        if resto1 == 10:
            cpf2[9] = 0
        if resto1 != 10:
            cpf2[9] = resto1
            
        soma2 = cpf1[0] * 11 + cpf1[1] * 10 + cpf1[2] * 9 + cpf1[3] * 8 + cpf1[4] * 7 + cpf1[5] * 6 + cpf1[6] * 5 + cpf1[7] * 4 + cpf1[8] * 3 + cpf2[9] * 2
        resto2 = (soma2*10)%11

        if resto2 == 10:
            cpf2[10] = 0
        if resto2 != 10:
            cpf2[10] = resto2


        if cpf1 == cpf2:
            valido = True
        if cpf1 != cpf2:
            valido = False

  

    if valido == True:
        print(cpf)
    while valido==False:
        cpf = input("CPF inválido! Digite novamente:")
        valido = True
        numeros = [0,1,2,3,4,5,6,7,8,9]
        numerosStr = ["0","1","2","3","4","5","6","7","8","9"]
        cpf1 = []
        cpf2 = []
        if valido == True:
            for x in cpf:
                if x not in numerosStr:
                    valido = False

        if valido == True:
            if len(cpf) != 11:
                valido = False

        if valido == True:
            for x in range(len(cpf)):
                cpf1.append(int(cpf[x]))
                cpf2.append(int(cpf[x]))


            soma1 = cpf1[0] * 10 + cpf1[1] * 9 + cpf1[2] * 8 + cpf1[3] * 7 + cpf1[4] * 6 + cpf1[5] * 5 + cpf1[6] * 4 + cpf1[7] * 3 + cpf1[8] * 2
            resto1 = (soma1*10)%11

            if resto1 == 10:
                cpf2[9] = 0
            if resto1 != 10:
                cpf2[9] = resto1
                
            soma2 = cpf1[0] * 11 + cpf1[1] * 10 + cpf1[2] * 9 + cpf1[3] * 8 + cpf1[4] * 7 + cpf1[5] * 6 + cpf1[6] * 5 + cpf1[7] * 4 + cpf1[8] * 3 + cpf2[9] * 2
            resto2 = (soma2*10)%11

            if resto2 == 10:
                cpf2[10] = 0
            if resto2 != 10:
                cpf2[10] = resto2


            if cpf1 == cpf2:
                valido = True
            if cpf1 != cpf2:
                valido = False
        if valido==True:
            cpf=cpf 
def validacaoDeTel(telefone):
    while telefone.isdigit()!=True:
        telefone=input("Telefone errado! Digite o certo:")
def validacaoDeCel(celular):
    while celular.isdigit()!=True:
        celular=input("Celular errado! Digite o certo:")
def validacaoDeNome(nome):
    while nome.isalpha()!=True:
        nome=input("Inválido! Digite somente letras:")
def validacaoIdentidade(identidade):
    while identidade.isdigit()!=True:
        identidade=input("Inválido! Digite novamente a identidade:")
    identidade=int(identidade)
def validarCnpj(cnpj):
    valido =False
    while not valido:
        valido = True
        numeros = [0,1,2,3,4,5,6,7,8,9]
        numerosStr = ["0","1","2","3","4","5","6","7","8","9"]
        cnpjInt1 = []
        cnpjInt2 = []
        cnpj = input('Escreva aqui seu CNPJ:')

        if valido == True:
            for x in cnpj:
                if x not in numerosStr:
                    valido = False

        if valido == True:
            if len(cnpj) != 14:
                valido = False  

        if valido == True:
            for x in range(len(cnpj)):
                cnpjInt1.append(int(cnpj[x]))
                cnpjInt2.append(int(cnpj[x]))

            soma1 = cnpjInt1[0] * 5 + cnpjInt1[1] * 4 + cnpjInt1[2] * 3 + cnpjInt1[3] * 2 + cnpjInt1[4] * 9 + cnpjInt1[5] * 8 + cnpjInt1[6] * 7 + cnpjInt1[7] * 6 + cnpjInt1[8] * 5 + cnpjInt1[9] * 4 + cnpjInt1[10] * 3 + cnpjInt1[11] * 2
            resto1 = soma1 % 11

            if resto1 < 2:
                cnpjInt2[12] = 0
            if resto1 >= 2:
                cnpjInt2[12] = 11 - resto1

            soma2 = cnpjInt1[0] * 6 + cnpjInt1[1] * 5 + cnpjInt1[2] * 4 + cnpjInt1[3] * 3 + cnpjInt1[4] * 2 + cnpjInt1[5] * 9 + cnpjInt1[6] * 8 + cnpjInt1[7] * 7 + cnpjInt1[8] * 6 + cnpjInt1[9] * 5 + cnpjInt1[10] * 4 + cnpjInt1[11] * 3 + cnpjInt2[12] * 2
            resto2 = soma2 % 11

            if resto2 < 2:
                cnpjInt2[13] = 0
            if resto2 >= 2:
                cnpjInt2[13] = 11 - resto2

            if cnpjInt1 == cnpjInt2:
                valido = True
            if cnpjInt1 != cnpjInt2:
                valido = False

        else:
            a = 0





while a<b:
    print("1-Cadastramento")
    print("2-Venda")
    print("3-Pesquisar")
    print("4-Salvar arquivos")#
    print("5-Relatório")
    print("6-Sair")

    informe=input("Digite a opção desejada:")
    informe.upper()
    if informe=='1' or informe=="CADASTRAMENTO":
        print("1-Produto")
        print("2-Cliente")
        print("3-Funcionário")
        print("4-Fornecedor")
        print("5-Custos")
        informe2=input("Digite a opção desejada:").upper()

        if informe2=='1' or informe2=="PRODUTO" or informe2=="PRODUTOS":
                    
            nomeDoProduto=input("Nome do produto:")
            codigoDoProduto=input("Código do produto:")
            referenciaDoProduto=input("Referência do produto:")
            referenciaOriginal=input("Referência original:")

            valorDoProduto=input("Valor do produto:")
            while valorDoProduto.isdigit()!=True:
              valorDoProduto=input("Inválido! Digite novamente o valor do produto:")
            valorDoProduto=float(valorDoProduto)


            quantidadeDoProduto=input("Quantidade do produto:")
            while quantidadeDoProduto.isdigit()!=True:
                quantidadeDoProduto=input("Inválido! Digite novamente a quantidade do produto:")
            quantidadeDoProduto=float(quantidadeDoProduto)

            marcaDoProduto=input("Marca do produto:")
            grupoDoProduto=input("Grupo do produto:")
            subgrupoDoProduto=input("Subgrupo do produto:")
            descricaoDoProduto=input("Descrição do produto:")
            aplicacaoDoProduto=input("Aplicação do produto:")
            fornecedorDoProduto=input("Fornecedor do produto:")
            localdeProduto=input("Local do produto:")


            dicProduto ["%s"%nomeDoProduto]=nomeDoProduto
            dicProduto ["%s"%codigoDoProduto]=codigoDoProduto
            dicProduto ["%s"%referenciaDoProduto]=referenciaDoProduto
            dicProduto ["%s"%referenciaOriginal]=referenciaOriginal
            dicProduto ["%0.2f"%valorDoProduto]=valorDoProduto
            dicProduto ["%0.2f"%quantidadeDoProduto]=quantidadeDoProduto
            dicProduto ["%s"%marcaDoProduto]=marcaDoProduto
            dicProduto ["%s"%grupoDoProduto]=grupoDoProduto
            dicProduto ["%s"%subgrupoDoProduto]=subgrupoDoProduto
            dicProduto ["%s"%descricaoDoProduto]=descricaoDoProduto
            dicProduto ["%s"%aplicacaoDoProduto]=aplicacaoDoProduto
            dicProduto ["%s"%fornecedorDoProduto]=fornecedorDoProduto
            dicProduto ["%s"%localdeProduto]=localdeProduto
            b+=1
        if informe2=='2' or informe2=="CLIENTE" or informe2=="CLIENTES":
                    
            nome=input("Nome:")
            validacaoDeNome(nome)
            apelido=input("Apelido:")
            idade=input("Idade:")
            while idade.isdigit()!=True:
                idade=input("Inválido! Digite idade novamente:")
            idade=int(idade)

            print("Data de Nascimento!")
            dia=input("Dia:")
            validacaoDia(dia)
            mes=input("Mês:")
            validacaoDeMes(mes)
            ano=input("Ano:")
            while ano.isdigit()!=True:
                ano=input("Inválido! Digite o ano novamente:")
            ano=int(ano)
            anoAtualEidade=anoAtual-idade# Minha idade menos o ano atual para que eu confira se os anos estão certos
            if anoAtualEidade==ano:
                anoAtualEidade==ano#Só para transcorrer
            while anoAtualEidade!=ano:
                ano=input("Inválido! Digite o ano certo:")
                ano=int(ano)
            ano = str(ano)
            while ano.isdigit()!=True:
                    ano=input("Inválido! Digite o ano novamente:")
            ano=int(ano)

            cpf=input("CPF:")
            validacaoDecpf(cpf)
            identidade=input("Identidade:")
            validacaoIdentidade(identidade)
            estado=input("Estado:")
            uf=input("UF:")
            cidade=input("Cidade:")
            endereco=input("Endereço:")
            numero=input("Número:")
            bairro=input("Bairro:")
            complemento=input("Complemento:")
            telefone=input("Telefone:")
            validacaoDeTel(telefone)
            celular=input("Celular:")
            validacaoDeCel(celular)
            email=input("Email:")

                    
            dicCliente ["%s"%nome]=nome
            dicCliente ["%s"%apelido]=apelido
            dicCliente ["%d"%idade]=idade
            dicCliente ["%s"%dia]=dia
            dicCliente ["%s"%mes]=mes
            dicCliente ["%d"%ano]=ano
            dicCliente ["%s"%identidade]=identidade
            dicCliente ["%s"%estado]=estado
            dicCliente ["%s"%uf]=uf
            dicCliente ["%s"%cidade]=cidade
            dicCliente ["%s"%endereco]=endereco
            dicCliente ["%s"%numero]=numero
            dicCliente ["%s"%bairro]=bairro
            dicCliente ["%s"%complemento]=complemento
            dicCliente ["%s"%telefone]=telefone
            dicCliente ["%s"%celular]=celular
            dicCliente ["%s"%email]=email
            b+=1
            
        if informe2=='3' or informe2=="FUNCIONARIO" or informe2=="FUNCIONÁRIO" or informe2=="FUNCIONARIOS" or informe2=="FUNCIONÁRIOS" or informe2=="VENDENDOR" or informe2=="VENDEDORES":
                    
                    nome=input("Nome:")
                    validacaoDeNome(nome)
                    apelido=input("Apelido:")
                    idade=input("Idade:")
                    while idade.isdigit()!=True:
                        idade=input("Inválido! Digite idade novamente:")
                    idade=int(idade)

                    print("Data de Nascimento!")
                    dia=input("Dia:")
                    validacaoDia(dia)
                    mes=input("Mês:")
                    validacaoDeMes(mes)
                    ano=input("Ano:")
                    while ano.isdigit()!=True:
                        ano=input("Inválido! Digite o ano novamente:")
                    ano=int(ano)
                    anoAtualEidade=anoAtual-idade# Minha idade menos o ano atual para que eu confira se os anos estão certos
                    if anoAtualEidade==ano:
                        anoAtualEidade==ano#Só para transcorrer
                    while anoAtualEidade!=ano:
                        ano=input("Inválido! Digite o ano certo:")
                        ano=int(ano)
                    ano = str(ano)
                    while ano.isdigit()!=True:
                        ano=input("Inválido! Digite o ano novamente:")
                    ano=int(ano)

                    cpf=input("CPF:")
                    validacaoDecpf(cpf)
                    identidade=input("Identidade:")
                    validacaoIdentidade(identidade)
                    estado=input("Estado:")
                    uf=input("UF:")
                    cidade=input("Cidade:")
                    endereco=input("Endereço:")
                    numero=input("Número:")
                    bairro=input("Bairro:")
                    complemento=input("Complemento:")
                    telefone=input("Telefone:")
                    validacaoDeTel(telefone)
                    celular=input("Celular:")
                    validacaoDeCel(celular)
                    email=input("Email:")


                    dicFuncionario ["%s"%nome]=nome
                    dicFuncionario ["%s"%apelido]=apelido
                    dicFuncionario ["%d"%idade]=idade
                    dicFuncionario ["%s"%dia]=dia
                    dicFuncionario ["%s"%mes]=mes
                    dicFuncionario ["%d"%ano]=ano
                    dicFuncionario ["%s"%identidade]=identidade
                    dicFuncionario ["%s"%estado]=estado
                    dicFuncionario ["%s"%uf]=uf
                    dicFuncionario ["%s"%cidade]=cidade
                    dicFuncionario ["%s"%endereco]=endereco
                    dicFuncionario ["%s"%numero]=numero
                    dicFuncionario ["%s"%bairro]=bairro
                    dicFuncionario ["%s"%complemento]=complemento
                    dicFuncionario ["%s"%telefone]=telefone
                    dicFuncionario ["%s"%celular]=celular
                    dicFuncionario ["%s"%email]=email
                    b+=1
        if informe2=='4' or informe2=="FORNECEDOR" or informe2=="FORNECEDORES":
                    
                    denominaçaoS=input("Denominação Social:")
                    estado=input("Estado:")
                    uf=input("UF:")
                    cidade=input("Cidade:")
                    endereco=input("Rua/Av:")
                    bairro=input("Bairro:")
                    numero=input("Número:")
                    telefone=input("Telefone:")
                    validacaoDeTel(telefone)
                    celular=input("Celular:")
                    validacaoDeCel(celular)
                    cep=input("CEP:")
                    cnpj=input("CNPJ:")
                    validarCnpj(cnpj)
                    email=input("Email:")   


                    dicFornecedor ["%s"%denominaçaoS]=denominaçaoS
                    dicFornecedor ["%s"%estado]=estado
                    dicFornecedor ["%s"%uf]=uf
                    dicFornecedor ["%s"%cidade]=cidade
                    dicFornecedor ["%s"%endereco]=endereco
                    dicFornecedor ["%s"%numero]=numero
                    dicFornecedor ["%s"%telefone]=telefone
                    dicFornecedor ["%s"%celular]=celular
                    dicFornecedor ["%s"%cep]=cep
                    dicFornecedor ["%s"%cnpj]=cnpj
                    dicFornecedor ["%s"%email]=email
                    b+=1
        if informe2=='5' or informe2=="CUSTO" or informe2=="CUSTOS":
                    
                    hoj=date.today()
                    hoj=str(hoj)
                    nomeDoCusto = input("Nome do Custo:")
                    quantidadeP=input("Quantidade:")
                    while quantidadeP.isdigit()!=True:
                        quantidadeP=input("Inválido! Digite a quantidade:")
                    quantidadeP=float(quantidadeP)
                    valorDoPro = input("Valor do Custo:")
                    while valorDoPro.isdigit()!=True:
                        valorDoPro=input("Inválido! Digite novamente o valor do custo:")
                    valorDoPro=float(valorDoPro)
                    valorp=quantidadeP*valorDoPro
                    descricaoDoCusto= input("Descrição do Custo:")
                    observacaoDoCusto= input("Observação sobre o Custo:")
                    dicCusto ["%s"%nomeDoCusto ]=nomeDoCusto 
                    dicCusto ["%0.2f"%quantidadeP]=quantidadeP
                    dicCusto ["%d"%valorDoPro]=valorDoPro
                    dicCusto ["%s"%descricaoDoCusto]=descricaoDoCusto
                    dicCusto ["%s"%observacaoDoCusto]=observacaoDoCusto
                    dicCusto ["%0.2f"%valorp]=valorp
                    custoTotal= custoTotal + valorp
                    
                    b+=1
            
    if informe=='2' or informe=="VENDA" or informe=="VENDAS":
        while e<f:
            deseja1=input("Deseja fazer uma venda? (SIM/NÃO):")
            if deseja1=="S" or deseja1=="SIM":
               
                print("NOME")
                print("CÓDIGO")
                print("REFERÊNCIA")
                pesquisar7=input("Digite a alternativa que deseja pesquisar para adicionar:").upper()
                
                if pesquisar7=="NOME" or pesquisar7=="CODIGO" or pesquisar7=="CÓDIGO" or pesquisar7=="REFERENCIA" or pesquisar7=="REFERÊNCIA" or pesquisar7=="REFERENCIA DO PRODUTO" or pesquisar7=="REFERÊNCIA DO PRODUTO" or pesquisar7=="REFERENCIA DO PRODUTO ORIGINAL" or pesquisar7=="REFERÊNCIA DO PRODUTO ORIGINAL" or pesquisar7=="VALOR" or pesquisar7=="CUSTO" or pesquisar7=="CUSTOS" or pesquisar7=="VALOR DE CUSTO" or pesquisar7=="VALOR DE CUSTOS" or pesquisar7=="QUANTIDADE" or pesquisar7=="QUANTIDADE DO PRODUTO" or pesquisar7=="MARCA" or pesquisar7=="GRUPO" or pesquisar7=="SUBGRUPO" or pesquisar7=="DESCRICAO" or pesquisar7=="DESCRIÇÃO" or pesquisar7=="DESCRIÇAO" or pesquisar7=="APLICAÇÃO" or pesquisar7=="APLICAÇAO" or pesquisar7=="APLICACAO" or pesquisar7=="FORNECEDOR" or pesquisar7=="LOCAL" or pesquisar7=="LOCAL DO PRODUTO":
                    print(dicProduto)
                    digiteO=input("Digite o que deseja:")
                    print("Nome:",dicProduto["%s"%nomeDoProduto])
                    print("Código:",dicProduto["%s"%codigoDoProduto])
                    print("Referência do produto:",dicProduto["%s"%referenciaDoProduto])
                    print("Referência do produto original:",dicProduto["%s"%referenciaOriginal])
                    print("Valor:",dicProduto["%0.2f"%valorDoProduto])
                    
                    print("Quantidade do produto:",dicProduto["%0.2f"%quantidadeDoProduto])
                    print("Marca:",dicProduto["%s"%marcaDoProduto])
                    print("Grupo:",dicProduto["%s"%grupoDoProduto])
                    print("Subgrupo:",dicProduto["%s"%subgrupoDoProduto])
                    print("Descrição:",dicProduto["%s"%descricaoDoProduto])
                    print("Aplicação:",dicProduto["%s"%aplicacaoDoProduto])
                    print("Fornecedor:",dicProduto["%s"%fornecedorDoProduto])
                    print("Local do produto:",dicProduto["%s"%localdeProduto])
                    
                    
                    nomeDoProdutoVenda=(dicProduto["%s"%nomeDoProduto])
                    codigoDoProdutoVenda=(dicProduto["%s"%codigoDoProduto])
                    referenciaDoProdutoVenda=(dicProduto["%s"%referenciaDoProduto])
                    referenciaDoProdutoVendaOriginal=(dicProduto["%s"%referenciaOriginal])
                    valorDoProdutoVenda=(dicProduto["%0.2f"%valorDoProduto])
                    valorDoProdutoVenda=float(valorDoProdutoVenda)
                    quantDp=float(input("Quantidade do produto:"))
                    quantDoProdutoVenda=(dicProduto["%0.2f"%quantidadeDoProduto])
                    valorDoProdutoCQuant=valorDoProdutoVenda*quantDp
                    quantDoProdutoVenda2=quantDoProdutoVenda-quantDp
                    quantDoProdutoVenda=quantDoProdutoVenda2
                    marcaDoProdutoVenda=(dicProduto["%s"%marcaDoProduto])
                    grupoDoProdutoVenda=(dicProduto["%s"%grupoDoProduto])
                    descricaoProdutoVenda=(dicProduto["%s"%descricaoDoProduto])
                    aplicacaoDoProdutoVenda=(dicProduto["%s"%aplicacaoDoProduto])
                    valorTotal=valorTotal+valorDoProdutoCQuant
                    valorap=valorap+valorDoProdutoCQuant
                    dicVenda ["%s"%nomeDoProdutoVenda]=nomeDoProdutoVenda
                    dicVenda ["%s"%codigoDoProdutoVenda]=codigoDoProdutoVenda
                    dicVenda ["%s"%referenciaDoProdutoVenda]=referenciaDoProdutoVenda
                    dicVenda ["%s"%referenciaDoProdutoVendaOriginal]=referenciaDoProdutoVendaOriginal
                    dicVenda ["%0.2f"%valorDoProdutoVenda]=valorDoProdutoVenda
                    dicVenda ["%0.2f"%quantDoProdutoVenda]=quantDoProdutoVenda
                    dicVenda ["%0.2f"%valorDoProdutoCQuant]=valorDoProdutoCQuant
                    dicVenda ["%s"%marcaDoProdutoVenda]=marcaDoProdutoVenda
                    dicVenda ["%s"%grupoDoProdutoVenda]=grupoDoProdutoVenda
                    dicVenda ["%s"%grupoDoProdutoVenda]=descricaoProdutoVenda
                    dicVenda ["%s"%aplicacaoDoProdutoVenda]=aplicacaoDoProdutoVenda

                    print("Nome do produto:",dicVenda["%s"%nomeDoProdutoVenda])
                    print("Código:",dicVenda["%s"%codigoDoProdutoVenda])
                    print("Referência:",dicVenda["%s"%referenciaDoProdutoVenda])
                    print("Referência Original:",dicVenda["%s"%referenciaDoProdutoVendaOriginal])
                    print("Valor:",dicVenda["%0.2f"%valorDoProdutoVenda])
                    print("Quantidade:",dicVenda["%0.2f"%quantDoProdutoVenda])
                    print("Valor total do produto:",dicVenda["%0.2f"%valorDoProdutoCQuant])
                    print("Marca:",dicVenda["%s"%marcaDoProdutoVenda])
                    print("Grupo:",dicVenda["%s"%grupoDoProdutoVenda])
                    print("Aplicação:",dicVenda["%s"%aplicacaoDoProdutoVenda])
                    f+=1
                    ad=input("Deseja dar desconto? (SIM/NÃO):").upper()
                    if ad=="S" or ad=="SIM":
                        deseja11=input("Vai dar desconto? (SIM/NÃO):").upper()
                        if deseja11=='SIM'or deseja11=='S':
                            desconto=int(input("DIGITE O VALOR DO DESCONTO:"))
                            valorDeDesconto=valorap*desconto/100
                            a_pagar=valorap-valorDeDesconto
                            print("O VALOR COM DESCONTO É:%0.2f"%a_pagar)
                            f+=1
                        if deseja11=="N" or deseja11=="NÃO":
                            print("O VALOR TOTAL É:%0.2f"%valorap)
                            
                            f+=1
                    if ad=="NÃO" or ad=="N" or ad=="NAO":
                        f+=1

            if deseja1=="N" or deseja1=="NÃO" or deseja1=="NAO":
                print("O valor a pagar é:%0.2f"%valorap)
                b+=1
                e=1+f
            

    if informe=='3' or informe=="PESQUISAR" or informe=="PESQUISA" or informe=="BUSCAR" or informe=="BUSCAR":
        print("1-Vendas")
        print("2-Produtos")
        print("3-Clientes")
        print("4-Funcionários")
        print("5-Fornecedores")
        print("6-Custos")
        informe3=input("Digite o que deseja:").upper()
        if informe3=='1' or informe3=="VENDA" or informe3=="VENDAS":
            pesquisar=input("Digite o que deseja:").upper()
            if pesquisar=="CODIGO" or pesquisar=="CÓDIGO" or pesquisar=="REFERENCIA" or pesquisar=="REFERÊNCIA" or pesquisar=="VALOR" or pesquisar=="REFERÊNCIA ORIGINAL" or pesquisar=="VALOR" or pesquisar=="QUANTIDADE" or pesquisar=="MARCA" or pesquisar=="GRUPO" or pesquisar=="APLICAÇÃO" or pesquisar=="APLICACAO" or pesquisar=="APLICACÃO" or pesquisar=="VALOR TOTAL":
                digite-input("Digite o que deseja:")
                print("Nome do produto:",dicVenda["%s"%nomeDoProdutoVenda])
                print("Código:",dicVenda["%s"%codigoDoProdutoVenda])
                print("Referência:",dicVenda["%s"%referenciaDoProdutoVenda])
                print("Referência Original:",dicVenda["%s"%referenciaDoProdutoVendaOriginal])
                print("Valor:",dicVenda["%0.2f"%valorDoProdutoVenda])
                print("Quantidade:",dicVenda["%0.2f"%quantDoProdutoVenda])
                print("Valor total do produto:",dicVenda["%0.2f"%valorDoProdutoCQuant])
                print("Marca:",dicVenda["%s"%marcaDoProdutoVenda])
                print("Grupo:",dicVenda["%s"%grupoDoProdutoVenda])
                print("Aplicação:",dicVenda["%s"%aplicacaoDoProdutoVenda])
                b+=1
        if informe3=='2' or informe3=="PRODUTOS" or informe3=="PRODUTO":
            print("NOME")
            print("CÓDIGO")
            print("REFERÊNCIA")
            pesquisar2=input("Digite o que procura:").upper()
            if pesquisar2=="NOME" or pesquisar2=="CODIGO" or pesquisar2=="CÓDIGO" or pesquisar2=="REFERENCIA" or pesquisar2=="REFERÊNCIA" or pesquisar2=="REFERENCIA DO PRODUTO" or pesquisar2=="REFERÊNCIA DO PRODUTO" or pesquisar2=="REFERENCIA DO PRODUTO ORIGINAL" or pesquisar2=="REFERÊNCIA DO PRODUTO ORIGINAL" or pesquisar2=="VALOR" or pesquisar2=="CUSTO" or pesquisar2=="CUSTOS" or pesquisar2=="VALOR DE CUSTO" or pesquisar2=="VALOR DE CUSTOS" or pesquisar2=="QUANTIDADE" or pesquisar2=="QUANTIDADE DO PRODUTO" or pesquisar2=="MARCA" or pesquisar2=="GRUPO" or pesquisar2=="SUBGRUPO" or pesquisar2=="DESCRICAO" or pesquisar2=="DESCRIÇÃO" or pesquisar2=="DESCRIÇAO" or pesquisar2=="APLICAÇÃO" or pesquisar2=="APLICAÇAO" or pesquisar2=="APLICACAO" or pesquisar2=="FORNECEDOR" or pesquisar2=="LOCAL" or pesquisar2=="LOCAL DO PRODUTO":
                digiteO=input("Digite o que deseja:")
                print("Nome:",dicProduto["%s"%nomeDoProduto])
                print("Código:",dicProduto["%s"%codigoDoProduto])
                print("Referência do produto:",dicProduto["%s"%referenciaDoProduto])
                print("Referência do produto original:",dicProduto["%s"%referenciaOriginal])
                print("Valor:",dicProduto["%0.2f"%valorDoProduto])
                
                print("Quantidade do produto:",dicProduto["%0.2f"%quantidadeDoProduto])
                print("Marca:",dicProduto["%s"%marcaDoProduto])
                print("Grupo:",dicProduto["%s"%grupoDoProduto])
                print("Subgrupo:",dicProduto["%s"%subgrupoDoProduto])
                print("Descrição:",dicProduto["%s"%descricaoDoProduto])
                print("Aplicação:",dicProduto["%s"%aplicacaoDoProduto])
                print("Fornecedor:",dicProduto["%s"%fornecedorDoProduto])
                print("Local do produto:",dicProduto["%s"%localdeProduto])
                b+=1
        if informe3=='3' or informe3=="CLIENTE" or informe3=="CLIENTES":
            print("NOME")
            print("APELIDO")
            print("EMAIL")
            pesquisar3=input("Digite o que procura:").upper()
            if pesquisar3=="NOME" or pesquisar3=="APELIDO" or  pesquisar3=="IDADE" or pesquisar3=="DATA" or pesquisar3==" DATA DE NASCIMENTO" or pesquisar3=="IDENTIDADE" or pesquisar3=="ESTADO" or pesquisar3=="CIDADE" or pesquisar3=="NUMERO" or pesquisar3=="NÚMERO" or pesquisar3=="ENDERECO" or pesquisar3=="ENDEREÇO" or pesquisar3=="COMPLEMENTO" or pesquisar3=="TELEFONE" or pesquisar3=="CELULAR" or pesquisar3=="UF":
                digite1=input("Digite o que você deseja:")
                print("Nome:",dicCliente["%s"%nome])
                print("Apelido:",dicCliente["%s"%apelido])
                print("idade:",dicCliente["%d"%idade])
                print("Data de nascimento:",dicCliente["%s"%dia],dicCliente["%s"%mes],dicCliente["%d"%ano])
                print("Identidade:",dicCliente["%s"%identidade])
                print("Estado:",dicCliente["%s"%estado])
                print("UF:",dicCliente["%s"%uf])
                print("Cidade:",dicCliente["%s"%cidade])
                print("Endereço:",dicCliente["%s"%endereco])
                print("Número:",dicCliente["%s"%numero])
                print("Bairro:",dicCliente["%s"%bairro])
                print("Complemento:",dicCliente["%s"%complemento])
                print("Telefone:",dicCliente["%s"%telefone])
                print("Celular:",dicCliente["%s"%celular])
                print("Email:",dicCliente["%s"%email])
                b+=1
        if informe3=='4' or informe3=="FUNCIONARIO" or informe3=="FUNCIONÁRIO" or informe3=="VENDENDOR" or informe3=="FUNCIONARIOS" or informe3=="FUNCIONÁRIOS":
            print("NOME")
            print("APELIDO")
            print("EMAIL")


            pesquisar4=input("DIGITE O QUE DESEJA PESQUISAR:").upper()
            if pesquisar2=="NOME" or pesquisar4=="DATA DE NASCIMENTO" or pesquisar4=="DATA" or pesquisar4=="NASCIMENTO" or pesquisar4=="IDENTIDADE" or pesquisar4=="CPF" or pesquisar4=="IDADE" or pesquisar4=="CIDADE" or pesquisar4=="ESTADO" or pesquisar4=="RUA" or pesquisar4=="AV" or pesquisar4=="ENDEREÇO" or pesquisar4=="ENDERECO"or pesquisar4=="NUMERO" or pesquisar4=="TELEFONE" or pesquisar4=="CELULAR":
                digite=input("DIGITE O NOME QUE DESEJA:")
                print("Nome:",dicFuncionario["%s"%nome])
                print("Apelido:",dicFuncionario["%s"%apelido])
                print("idade:",dicFuncionario["%d"%idade])
                print("Data de nascimento:",dicFuncionario["%s"%dia],dicFuncionario["%s"%mes],dicFuncionario["%d"%ano])
                print("Identidade:",dicFuncionario["%s"%identidade])
                print("Estado:",dicFuncionario["%s"%estado])
                print("UF:",dicFuncionario["%s"%uf])
                print("Cidade:",dicFuncionario["%s"%cidade])
                print("Endereço:",dicFuncionario["%s"%endereco])
                print("Número:",dicFuncionario["%s"%numero])
                print("Bairro:",dicFuncionario["%s"%bairro])
                print("Complemento:",dicFuncionario["%s"%complemento])
                print("Telefone:",dicFuncionario["%s"%telefone])
                print("Celular:",dicFuncionario["%s"%celular])
                print("Email:",dicFuncionario["%s"%email])
                b+=1
        if informe3=='5' or informe3=="FORNECEDOR" or informe3=="FORNECEDORES":
            print("DENOMINAÇÃO SOCIAL")
            print("CNPJ")
            pesquisar5=input("Digite o que deseja:").upper()
            if pesquisar5=="DENOMINACAO SOCIAL" or pesquisar5=="NOME" or pesquisar5=="DENOMINAÇAO SOCIAL" or pesquisar5=="DENOMINAÇÃO SOCIAL" or pesquisar5=="ESTADO" or pesquisar5=="UF" or pesquisar5=="CIDADE" or pesquisar5=="ENDERECO" or pesquisar5=="ENDEREÇO" or pesquisar5=="NUMERO" or pesquisar5=="NÚMERO" or pesquisar5=="TELEFONE" or pesquisar5=="CELULAR" or pesquisar5=="CEP" or pesquisar5=="CNPJ" or pesquisar5=="EMAIL":
                digite3=input("Digite o que quer:").upper()
                print("Denominação social:",dicFornecedor["%s"%denominaçaoS])
                print("Estado:",dicFornecedor["%s"%estado])
                print("UF:",dicFornecedor["%s"%uf])
                print("Cidade:",dicFornecedor["%s"%cidade])
                print("Endereço:",dicFornecedor["%s"%endereco])
                print("Número:",dicFornecedor["%s"%numero])
                print("Telefone:",dicFornecedor["%s"%telefone])
                print("Celular:",dicFornecedor["%s"%celular])
                print("CEP:",dicFornecedor["%s"%cep])
                print("CNPJ:",dicFornecedor["%s"%cnpj])
                print("Email:",dicFornecedor["%s"%email])
            b+=1
        if informe3=='6' or informe3=="CUSTO" or informe3=="CUSTOS":
            print("NOME")
            print("QUANTIDADE")
            print("NOME DO CUSTO")
            print("VALOR DO CUSTO")
            pesquisar6=input("Digite o que deseja:").upper()
            if pesquisar6=="NOME" or pesquisar6=="NOME DO CUSTO" or pesquisar6=="CUSTO" or  pesquisar6=="QUANTIDADE" or pesquisar6=="VALOR" or pesquisar6=="DATA" or pesquisar6=="DESCRIÇÃO" or pesquisar6=="OBSERVACAO" or pesquisar6=="OBSERVAÇÃO" or pesquisar6=="OBSERVAÇAO":
                digite4=input("Digite o que quer:").upper()
                print("Nome do custo:",dicCusto["%s"%nomeDoCusto])
                print("Quantidade:",dicCusto["%0.2f"%quantidadeP])
                print("Valor do custo:",dicCusto["%d"%valorDoPro])
                print("Descrição:",dicCusto["%s"%descricaoDoCusto])
                print("Observação:",dicCusto["%s"%observacaoDoCusto])
                b+=1        
    
   
    if informe=='4' or informe=="SALVAR" or informe=="SALVAR ARQUIVOS":

        arquivos=open("dicCliente.txt","w")
        for i in (dicCliente):
            arquivos.write("%s\n"%i)
        arquivos.close()
        arquivos2=open("dicProduto","w")
        for e in (dicProduto):
            arquivos2.write("%s\n"%e)
        arquivos2.close()
        arquivos3=open("dicCusto","w")
        for q in dicCusto:
            arquivos3.write("%s\n"%q)
        arquivos3.close()
        arquivos4=open("dicFornecedor","w")
        for p in dicFornecedor:
            arquivos4.write("%s\n"%p)
        arquivos4.close()
        arquivos5=open("dicFuncionario","w")
        for k in dicFuncionario:
            arquivos5.write("%s\n"%k)
        arquivos5.close()
        arquivos6=open("dicVenda","w")
        for z in dicVenda:
            arquivos6.write("%s\n"%z)
        arquivos6.close()
        b+=1
    if informe=='5' or informe=="RELATÓRIOS" or informe=="RELATORIOS" or informe=="RELATÓRIO" or informe=="RELATORIO":    
        print("Venda Total:%0.2f"%valorTotal)
        print("Custo Total:%0.2f"%custoTotal)
        valorTotalMcustoTotal=valorTotal-custoTotal
        print("Lucro:%0.2f"%valorTotalMcustoTotal)
        b+=1
    if informe=="6" or informe=="SAIR":
        a+=100000000
print("Obrigado e volte sempre!")
