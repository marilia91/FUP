mat = []
#criar as matrizes depois

#imprimir direito
lista_tamanho = []
for j in range(0,10):
    tamanho = 0
    if tamanho < len(str(mat[i][j])):
        tamanho = len(str(mat[i][j]))
    lista_tamanho.append(tamanho)

for i in range(0,10):
    linha = '['
    for j in range(0,10):
        linha += f'{mat[i][j]:{lista_tamanhos[j]+1}}'
    linha += ']'
    print(linha)

"""tamanho = 0
for linha in mat:
    for elemento in linha:
        if tamanho < len(str(elemento)):
            tamanho = len(str(elemento))
for i in range(0,10):
    linha = '['
    for j in range(0,10):
        #construir a linha aqui
        linha += f"{mat[i][j]:{tamanho +1}}"
    linha += "]"
    print(linha)"""