cpf = '14986955433'
cpf_tratado = cpf[0:-2]                       # Remove os dois ultimos números do cpf


def checa(cpf):
    cpf_inv = cpf[::-1]                       # Inverte o cpf
    soma = 0
    for c, d in enumerate(cpf_inv, start=2):  # Percorre cada dígto do cpf enumerado começando por 2
        soma += c * int(d)                    # Multiplica o contador pelo digto do cpf e adicona a soma
    dig = 11 - (soma % 11)                    # Formula para obter o dígito de validação
    if dig > 9:
        return cpf + '0'
    else:
        return cpf + str(dig)


cpf_novo = checa(checa(cpf_tratado))

if cpf == cpf_novo:
    print('valido')
else:
    print('invalido')
