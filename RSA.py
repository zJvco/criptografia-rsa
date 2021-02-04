import random


def cadastrar(arquivo, mensagem):
    try:
        b = open(arquivo, 'a')
    except:
        print('Error')
    else:
        b.write(f'{frase_cripto} \n')


def cadastrar_chave(arquivo, chave1, chave2):
    try:
        b = open(arquivo, 'a')
    except:
        print('Error')
    else:
        b.write(f'{chave1};{chave2}\n')


def ler_chave(arquivo):
    try:
        b = open(arquivo, 'rt')
    except:
        print('Error')
    else:
        contador = 0
        for linha in b:
            contador += 1
            dado = linha.split(';')
            dado[0] = dado[0].replace(';', '')
            dado[1] = dado[1].replace(';', '')
            print(f'{contador}º chave: {dado[0]} e {dado[1]}',end='')


def ler_arquivo(arquivo):
    try:
        b = open(arquivo, 'rt')
    except:
        print('Error')
    else:
        contador = 0
        mensagem_cripto = ''
        for linha in b:
            contador += 1
            mensagem_criptografada = linha.split()
            mensagem_cripto = ' '.join(mensagem_criptografada)
            print(f'{contador}º mensagem: {mensagem_cripto}')


def arq_existe(nome, arq2):
    try:
        b = open(nome, 'rt')  # ler arquivo
        c = open(arq2, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo_chave(nome):
    try:
        b = open(nome, 'wt+')
    except:
        print('Error')
    else:
        print('Arquivo criado com sucesso')


def criar_arquivo(nome):
    try:
        b = open(nome, 'wt+')
    except:
        print('Error')
    else:
        print('Arquivo criado com sucesso')


def criptografar(elemento):
    # transformar em um valor númerico para a conta baseado na lista
    posicao_j = 0
    for i in range(len(lista)):
        for item in lista[i]:
            if elemento in item == elemento:
                posicao_j = lista[i][0]
    pos_j = int(posicao_j)
    cripto = (pos_j ** e) % n
    print(cripto, end=' ')
    return str(cripto)


def descriptografar(chave1, chave2, mensagem):
    letra_final = 0
    valor_correspondente = (int(mensagem) ** int(chave1)) % int(chave2)
    for o in range(len(lista)):
        for iten in lista[o]:
            if str(valor_correspondente) == lista[o][0]:
                letra_final = lista[o][1]
    print(letra_final, end='')


primos = [19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
          137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
          251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359]
p = random.choice(primos)
q = random.choice(primos)
while p == q:
    q = random.choice(primos)
n = p * q
o_n = (p - 1) * (q - 1)  # total de valores que não possuem valor comum com n
e = 0
# escolher e{1 < e < o(n)
#           {nao pode ter valor comum com n,o(n)
for a in range(1, o_n):
    if a % n != 0 or a % o_n != 0:
        e = a
# fechadura (e, n)
lista = [['1', ''], ['2', 'b'], ['3', 'c'], ['4', 'd'], ['5', 'e'], ['6', 'f'], ['7', 'g'], ['8', 'h'], ['9', 'i'],
         ['10', 'j'], ['11', 'k'], ['12', 'l'], ['13', 'm'], ['14', 'n'], ['15', 'o'], ['16', 'p'], ['17', 'q'],
         ['18', 'r'], ['19', 's'], ['20', 't'], ['21', 'u'], ['22', 'v'], ['23', 'w'], ['24', 'x'], ['25', 'y'],
         ['26', 'z'], ['27', 'a'], ['28', '1'], ['29', '2'], ['30', '3'], ['31', '4'], ['32', '5'], ['33', '6'],
         ['34', '7'], ['35', '8'], ['36', '9'], ['37', 'ç'], ['38', 'á'], ['39', 'à'], ['40', 'é'], ['41', 'ó'],
         ['42', 'ò'], ['43', '@'], ['44', 'A'], ['45', 'B'], ['46', 'C'], ['47', 'D'], ['48', 'E'], ['49', 'F'],
         ['50', 'G'], ['51', 'H'], ['52', 'I'], ['53', 'J'], ['54', 'K'], ['55', 'L'], ['56', 'M'], ['57', 'N'],
         ['58', 'O'], ['59', 'P'], ['60', 'Q'], ['61', 'R'], ['62', 'S'], ['63', 'T'], ['64', 'U'], ['65', 'V'],
         ['66', 'W'], ['67', 'X'], ['68', 'Y'], ['69', 'Z'], ['70', ' '], ['71', '+'], ['72', '-'], ['73', '*'],
         ['74', '/'], ['75', '|'], ['76', '.'], ['77', ','], ['78', ';'], ['79', ':'], ['80', '>'], ['81', '<'],
         ['82', '^'], ['83', '~'], ['84', '='], ['85', '-'], ['86', '_'], ['87', '('], ['88', ')'], ['89', '!'],
         ['90', 'Ê'], ['91', 'ê'], ['92', '&'], ['93', '%'], ['94', '$'], ['95', '#'], ['96', '?'], ['97', '"'],
         ['98', "'"]]

# escolher d: d*e(mod o(n)) = 1
d = x = 0
x += e
lista_final = []
if (x * e) % o_n == 1:
    d = x
# chave (d,n)
# decriptografar
print('-' * 40)
print('''
[ 1 ] Para criptografar uma mensagem
[ 2 ] Ver mensagens criptografadas
[ 3 ] Para descriptografar uma mensagem
[ 4 ] Para mostrar as chaves
[ 5 ] Para sair do programa
''')
print('-' * 40)
escolha = int(input('O que você deseja realizar: '))
arq = 'mensagens.txt'
arq_chave = 'chave.txt'
if escolha == 1:
    frase = str(input('Frase que deseja criptografar: '))
    while len(frase) > 128:
        frase = str(input('Frase que deseja criptografar: '))
    if arq_existe(arq, arq_chave):
        pass
    else:
        print('Arquivo não encontrado')
        criar_arquivo(arq)
        criar_arquivo_chave(arq_chave)
    for palavra in frase:
        for letra in palavra:
            x = criptografar(letra)
            lista_final.append(x)
    frase_cripto = ' '.join(lista_final)
    cadastrar(arq, frase_cripto)
    cadastrar_chave(arq_chave, d, n)
    print()
    print(f'A chave da mensagem é {d} e {n}')
elif escolha == 2:
    ler_arquivo(arq)
elif escolha == 3:
    c1 = int(input('Primeira parte da chave: '))
    c2 = int(input('Segunda parte da chave: '))
    criptografada = str(input('Mensagem Criptografada que deseja descriptografar: '))
    while len(criptografada) > 768:
        criptografada = str(input('Mensagem Criptografada que deseja descriptografar: '))
    for parte in criptografada.split():
        descriptografar(c1, c2, parte)
elif escolha == 4:
    ler_chave(arq_chave)
elif escolha == 5:
    print('fechando programa...')
else:
    print('-' * 40)
    print('''
    [ 1 ] Para criptografar uma mensagem
    [ 2 ] Para descriptografar uma mensagem
    [ 3 ] Para sair do programa
    ''')
    print('-' * 40)
