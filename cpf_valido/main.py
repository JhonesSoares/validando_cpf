
def iterador_digitos(digitos, contador):
    res = 0
    for digito in digitos:
        res += (int(digito) * contador)
        contador -= 1
    return int(res)    

def calculo_digito(iter):
    iter = (iter * 10) % 11
    digito = 0 if iter > 9 else iter
    return str(digito) 


def primeiro_digito(cpf):
    nove_digitos = cpf[:9]
    contador_regressivo = 10
    res = iterador_digitos(nove_digitos, contador_regressivo)

    return calculo_digito(res)

def segundo_digito(cpf):
    dez_digitos = cpf[:9] + primeiro_digito(cpf)
    contador_regressivo = 11
    res = iterador_digitos(dez_digitos, contador_regressivo)

    return calculo_digito(res)


def validando_cpf_usuario(cpf):
    calculo_cpf = str(f'{cpf[:9]}{primeiro_digito(cpf)}{segundo_digito(cpf)}')

    if cpf == calculo_cpf:
        return 'CPF válido!'
    return 'CPF inválido!'


CPF_USUARIO = '37316703059'
print(validando_cpf_usuario(CPF_USUARIO))