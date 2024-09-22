# GarraMecanica# Controle de Garra Mecânica usando Detecção de Mão com MediaPipe e MQTT

Este projeto implementa o controle de uma garra mecânica usando a detecção de mãos com a biblioteca MediaPipe. As coordenadas da mão direita (X, Y, Z) são mapeadas para o movimento da garra, e o estado da mão (aberta ou fechada) controla se a garra deve abrir ou fechar. O projeto também está preparado para enviar dados via MQTT para controlar a garra remotamente.

## Estrutura do Projeto

- **`main.py`**: O arquivo principal que executa o fluxo de detecção de mãos e controle da garra.
- **`hand_detection.py`**: Contém as funções relacionadas à detecção da mão e ao cálculo das coordenadas.
- **`garra_control.py`**: Lida com a lógica de atualização da posição da garra e a interpolação suave para movimento.
- **`mqtt_client.py`**: Contém a lógica para o envio de dados via MQTT (preparado para futuras implementações).
- **`requirements.txt`**: Lista de dependências necessárias para rodar o projeto.

## Requisitos

- Python 3.7 ou superior
- As bibliotecas necessárias podem ser instaladas usando o `pip` com o comando:

  ```bash
  pip install -r requirements.txt
