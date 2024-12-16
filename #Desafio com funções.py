#Desafio com funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. 
O usuario deverá fornecer as seguintes informações: Rendimento, altura e largura. 
O programa deve mostra na tela a mensagem "Você necessita de x latas de tinta"
'''

# caixas de entrada


# operação para gerar o resultado esperado

def capturar_dados():
    rendimento = float(input("Informe o rendimento da tinta (m² por lata): "))
    altura = float(input("Informe a altura da parede (em metros): "))
    largura = float(input("Informe a largura da parede (em metros): "))
    return rendimento, altura, largura

def calcular_area(altura, largura):
    return altura * largura

def calcular_latas(area, rendimento):
  import math
  return math.ceil(area / rendimento)

def main():
  rendimento, altura, largura = capturar_dados()
  area = calcular_area(altura, largura)
  latas = calcular_latas(area, rendimento)
  print(f"Você necessita de {latas} latas de tinta.")
  

#finalização
if __name__ == "__main__":
    main()