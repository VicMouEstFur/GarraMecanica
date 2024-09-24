def atualizar_posicao_garra(nova_posicao, posicao_atual, taxa_atualizacao=0.1):
    """
    Atualiza a posição da garra de forma suave utilizando interpolação linear.
    """
    posicao_atualizada = [
        posicao_atual[i] + (nova_posicao[i] - posicao_atual[i]) * taxa_atualizacao
        for i in range(3)
    ]
    posicao_atualizada.append(nova_posicao[3])  # Atualiza o estado da mão (aberta/fechada)
    return posicao_atualizada