import random
import string


def caracteres_validos():
    letras_mins = string.ascii_lowercase
    letras_maius = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation
    # o método .join tende a ser mais performático. Em um programa pequeno como esse, não deve fazer muita diferença
    # no entanto, em programas que exigem mais performance, pode ser boa prática usar .join ao invés de concatenação (letras_mins + letras_maius ...)
    todos_caracteres_validos = "".join(([letras_mins, letras_maius, numeros, simbolos]))
    return todos_caracteres_validos


def gerar_senha_base():
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
    return senha_base


def tamanho_resto_senha(tamanho_solicitado):
    tamanho_restante = tamanho_solicitado - 6
    return tamanho_restante


def embaralhar_senha(senha):
    senha_final = senha
    random.shuffle(senha_final)
    senha_final = "".join(senha_final)
    return senha_final


def solicitar_tamanho_senha():
    solicitacao_usuario = int(input("Digite o tamanho da senha (mínimo 8): "))
    while solicitacao_usuario < 8:
        solicitacao_usuario = int(input("A senha deve conter no mínimo 8 dígitos: "))
    return solicitacao_usuario


def gerar_senha():
    tamanho_definido = solicitar_tamanho_senha()
    todos_caracteres_validos = caracteres_validos()
    senha_base = gerar_senha_base()
    tamanho_restante = tamanho_resto_senha(tamanho_definido)
    for n in range(tamanho_restante):
        senha_base.append(random.choice(todos_caracteres_validos))
    senha_final = embaralhar_senha(senha_base)
    return senha_final


print(gerar_senha())
