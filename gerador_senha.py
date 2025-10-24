# commit inicial para mudar para a nova branch

import random
import string

letras_mins = string.ascii_lowercase
letras_maius = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation
todos = "".join(([letras_mins, letras_maius, numeros, simbolos]))

solicitacao_usuario = int(input("Digite o tamanho da senha: "))

# definir essas atribuições como 'def zerar_variaveis()'
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
            print(f"Senha validada --> {senha}")
            break
        else:
            tentativas += 1
            if tentativas == 40:
                print(
                    f"Numero de tentativas chegou ao limite. Tente novamente com um tamanho maior (pelo menos 10)."
                )
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


# Caso necessário embaralhar a senha:
# senha_embaralhada = list(senha)
# random.shuffle(senha_embaralhada)
# senha_embaralhada = "".join(senha_embaralhada)
# print(f"Senha embaralhada: {senha_embaralhada}")

print(f"Tentativas = {tentativas}")
