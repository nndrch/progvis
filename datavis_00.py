
# caminho do arquivo de texto (csv)
P = u"/Users/gferreira0/Desktop/_cursos/progamação visual/_progvis/pop-rj.csv"

# acessa o arquivo em modo leitura ('r')
F = open(P, 'r')

# cria um dicionário vazio para armazenar os valores
D = {}

ordem = []

# percorre cada linha do arquivo...
for L in F.readlines():
    # separa os valores em variáveis
    age, amount, _ = L.split(',')
    # armazena os valores no dicionário
    D[age] = amount
    # armazena a ordem
    ordem.append(age)

# parametros do grafico
x, y = 40, 55
ht = 29
s = .0005
col = 158

size(800, 600)
colormode(HSB)

font('Verdana', 11)
c = 1.00 / (len(ordem)-1)

count = 0
for k in ordem:
    if k != 'Total':
        fill(c*count, 1, 1, .5)
        rect(x + col, y-14, int(D[k])*s, ht)
        fill(.6)
        text(k[:-7], x, y)
        text(int(D[k]), x + 13 + col + int(D[k])*s, y)
        y += ht + 5
        count += 1
