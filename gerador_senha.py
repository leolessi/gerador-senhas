# commit inicial para mudar para a nova branch

import random
import string

letras_mins = string.ascii_lowercase
letras_maius = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation
todos = "".join(([letras_mins, letras_maius, numeros, simbolos]))

solicitacao_usuario = int(input("Digite o tamanho da senha (mínimo 8): "))


def gerar_senha(tamanho_senha):
    senha_base = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.digits),
        random.choice(string.punctuation),
        random.choice(string.punctuation),
    ]

    tamanho_restante = solicitacao_usuario - 6
    for n in range(tamanho_restante):
        senha_base.append(random.choice(todos))

    senha_final = senha_base
    random.shuffle(senha_final)
    senha_final = "".join(senha_final)
    return senha_final


print(gerar_senha(solicitacao_usuario))
