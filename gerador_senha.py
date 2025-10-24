"""
Programa para gerar senhas de pelo menos 10 digitos.
As senhas, necessariamente, conterão:
    1 letra minúsucla
    1 letra maiúscula
    1 número
    1 caractere especial

OBS: Melhorias futuras/próximas:
    -> Dividir por funções
    -> Exigir pelo menos duas letras maiúsculas, duas minúsculas, dois símbolos e dois números
    -> Otimizações gerais
"""

import random
import string

letras_mins = string.ascii_lowercase
letras_maius = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation
todos = letras_mins + letras_maius + numeros + simbolos

solicitacao_usuario = int(input("Digite o tamanho da senha: "))
i = 0
senha = ""
validacao_letras_mins = False
validacao_letras_maius = False
validacao_numeros = False
validacao_simbolos = False
tentativas = 0

while i <= solicitacao_usuario:
    if i == solicitacao_usuario:
        for caractere in senha:
            if caractere in letras_mins:
                validacao_letras_mins = True
            if caractere in letras_maius:
                validacao_letras_maius = True
            if caractere in numeros:
                validacao_numeros = True
            if caractere in simbolos:
                validacao_simbolos = True

        validacao_tamanho = len(senha) >= 10

        validacao_senha = (
            validacao_letras_mins
            and validacao_letras_maius
            and validacao_numeros
            and validacao_simbolos
            and validacao_tamanho
        )

        if validacao_senha:
            print("Senha validada!")
            break
        else:
            print("Senha invalida")
            tentativas += 1
            if tentativas == 20:
                break
            validacao_letras_mins = False
            validacao_letras_maius = False
            validacao_numeros = False
            validacao_simbolos = False
            senha = ""
            i = 0

    caracter_random = random.choice(todos)
    senha += caracter_random
    i += 1


print(senha)
print(f"Tentativas = {tentativas}")
