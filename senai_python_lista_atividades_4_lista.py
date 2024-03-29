# -*- coding: utf-8 -*-
"""SENAI-Python-Lista-Atividades-4-LISTA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ioWiasIik5MBO31HZ4B0B1C5Eg_y8HpM

# 1. Ler uma lista de 5 Numeros inteiros e mostre cada numero juntamente com a sua posicao na lista
"""

lista = [1 , 2 , 3 , 4 , 5]
i = 0

while i < len(lista):
  print(f"{i} : {lista[i]}")
  i += 1

"""# 2. Ler uma lista de 10 numeros reais e mostre-os na ordem inversa que foram lidos"""

lista = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
print(lista)
print()

lista[::-1]

"""# 3. Ler uma lista com 5 idades e exibir a maior e a menor"""

lista = [9 , 2 , 7 , 4 , 6]

lista.sort()
print(lista)

"""# 4. Inicializa uma lista de 10 numeros inteiros. Armazene os umeros pares em uma lista PAR e os numeros impares em uma lista IMPAR. Imprima as listas PAR e IMPAR"""

lista = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

apenas_pares = [x for x in lista if x % 2 == 0]
apenas_impares = [x for x in lista if x % 2 != 0]

print(f'{apenas_pares} sao pares')
print(f'{apenas_impares} sao impares')

"""#5. Escreva um programa que troque o primeiro com o último elemento de uma lista qualquer."""

frutas = ['Banana' , 'Manga' , 'Melancia' , 'Uva']

frutas[0] , frutas[-1] = frutas[-1] , frutas[0]

print(frutas)

"""## 6. Qual a saída/resultado da seguinte compreensão de lista?

## [[1 + j*3 + i for i in range(3)] for j in range(3)]

## Você consegue entender e explicar o resultado?
"""

[[1 + j * 3 + i
  #Aqui o contador "j" esta somando o 1 para nao iniciar em 0, e multiplicando com 3
  #e somando com o contador "i".
  for i in range(3)]
  #Para que i no range de 3, repete 3 vezes.
  for j in range(3)]
  #Para que j no range de 3, repete 3 vezes.

"""## 7. Considere que você recebe um dicionário contendo informações sobre produtos em uma loja. Cada chave do dicionário é o nome de um produto e cada valor é uma tupla contendo o preço e a quantidade em estoque desse produto.

produtos = {

'camiseta': (25.00, 10),

'calça': (45.00, 5),

'sapato': (60.00, 3),

'boné': (15.00, 8)

}
## Você deve criar um programa em Python que solicite ao usuário que insira um preço máximo. Em seguida, o programa deve imprimir os produtos cujo preço seja menor ou igual ao preço máximo inserido pelo usuário.
"""

produtos = {
  'camiseta': (25.00, 10),
  'calça': (45.00, 5),
  'sapato': (60.00, 3),
  'boné': (15.00, 8)
}

precomaximo = float(input("Insira o valor maximo: "))

for produto, (preco, quantidade) in produtos.items():
    if preco <= precomaximo:
        print(f'{produto}: R${preco} (Quantidade no estoque: {quantidade} unidades)')

"""## 8. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informadas em ordem crescente ou decrescente."""

media = 0

ginasta = {
 'nota' : [2.0 , 5.0 , 7.0 , 0.0 , 10.0 , 7.0 , 9.0],
 'nome' : 'Laura'
}

ginasta['nota'].sort()

print(ginasta['nota'])

ginasta['nota'].pop(0)
ginasta['nota'].pop(-1)

print(ginasta['nota'])

media = sum(ginasta['nota']) / len(ginasta['nota'])

print(media)
print(ginasta)