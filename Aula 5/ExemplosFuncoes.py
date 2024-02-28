# Exemplos de Funções:
# Exemplo Simples
def saudacao(nome):
    return f"Olá, {nome}!"


#Função com Parâmetros Padrão:
def potencia(base, expoente=2):
    return base ** expoente


# Função com Retorno Múltiplo:
def opera_numeros(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

#Exemplo Escopo:
def exemplo_escopo():
    variavel_local = 10
    print(variavel_local)

exemplo_escopo()  # Saída: 10
print(variavel_local)  # Erro: variavel_local não está definida fora da função

#
def calcular_quadrado(numero):
    return numero ** 2

resultado = calcular_quadrado(5)
print(resultado)  # Saída: 25
