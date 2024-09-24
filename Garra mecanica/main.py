import cv2
import time
from hand_detection import detectar_maos, verificar_mao_aberta, getHandCoordinates
from garra_control import atualizar_posicao_garra
from mqtt_client import enviar_dados_mqtt  # Importar a função de envio do MQTT

# Variável de tempo para intervalos de iteração
tempo = 2.0
last_time = 0

# Coordenada base e posição da garra
coordenadaBase = [0, 0, 0]
posicao_garra = [0, 0, 0, True]

# Captura de vídeo (você pode alterar para webcam)
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    # Inverter a imagem horizontalmente para corrigir o espelhamento
    img = cv2.flip(img, 1)

    # Pegando dimensões da imagem
    img_height, img_width, _ = img.shape

    # Detectando mãos
    result, mp_draw, hands = detectar_maos(img)

    # Desenhar as marcas das mãos na imagem
    if result.multi_hand_landmarks:
        for hand_lms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_lms, hands.HAND_CONNECTIONS)

    # Verificando o intervalo de tempo
    current_time = time.time()
    if current_time - last_time >= tempo:
        last_time = current_time

        # Verifique se o resultado da detecção de mãos não é None
        if result.multi_handedness:
            # Obter as coordenadas da mão direita e verificar se está aberta
            idx_mao_direita = next((i for i, handedness in enumerate(result.multi_handedness) if handedness.classification[0].label == 'Right'), None)

            if idx_mao_direita is not None:
                hand_lms = result.multi_hand_landmarks[idx_mao_direita]
                current_coordinates = getHandCoordinates(hand_lms, img_width, img_height)
                mao_aberta = verificar_mao_aberta(hand_lms)

                # Atualizar posição da garra
                relative_coordinates = [
                    current_coordinates[0] - coordenadaBase[0],
                    current_coordinates[1] - coordenadaBase[1],
                    current_coordinates[2] - coordenadaBase[2],
                    mao_aberta
                ]
                posicao_garra = atualizar_posicao_garra(relative_coordinates, posicao_garra)
                print(f'Posição alvo da garra: X={posicao_garra[0]:.2f}, Y={posicao_garra[1]:.2f}, Z={posicao_garra[2]:.2f}, Mão aberta: {posicao_garra[3]}')

                # Chamada contínua da função para enviar dados via MQTT
                enviar_dados_mqtt(posicao_garra)
        else:
            print("Nenhuma mão detectada.")

    # Mostrar o vídeo
    cv2.imshow("Imagem", img)

    # Pressionar 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
