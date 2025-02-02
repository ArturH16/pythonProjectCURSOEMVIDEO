def notas(*nota,sit=False):
    """
    -> Função para analisar notas e situações de alunos
    :param nota: uma ou mais notas dos alunos ( aceita várias)
    :param sit: valor opcional, indicando se deve adicionar ou não a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dici = dict()
    dici['Total'] = len(nota)
    dici['Maior'] = max(nota)
    dici['Menor'] = min(nota)
    dici['Média'] = sum(nota) / len(nota)
    if sit:
        if dici['Média'] >= 7:
             dici['Situação'] = 'BOA'
        elif  6 < dici['Média'] <= 7:
            dici['Situação'] = 'RAZOÁVEL'
        else:
            dici['Situação'] = 'RUIM'
    return dici


note = notas(5.5,9.5,10,6.5,True)
print(note)
help(notas)




