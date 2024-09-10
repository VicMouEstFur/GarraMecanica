import cv2
import mediapipe as mp
import time

# Inicializando MediaPipe Hands e o vídeo
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Variável de tempo
tempo = 0.3  # Intervalo de 0.3 segundos (pode ser alterado)
last_time = 0

# Variável de coordenadas

coordenadasAntigo = [0,0,0]
coordenadasAtual = [0,0,0]


def iteracao(tempo):
    if isLeftHere():
        print("reset")
        if isRightHere()==True:
            print('reset coordenates')
    elif isRightHere():
        print("continue")
    else:
        print("detection failed")



def isRightHere():
    # Verifica se a mão direita está presente
    global result
    if result.multi_handedness:
        for hand_info in result.multi_handedness:
            if hand_info.classification[0].label == 'Right':  # Verifica se a mão detectada é a direita
                return True
    return False

def isLeftHere():
    # Verifica se a mão esquerda está presente
    global result
    if result.multi_handedness:
        for hand_info in result.multi_handedness:
            if hand_info.classification[0].label == 'Left':  # Verifica se a mão detectada é a esquerda
                return True
    return False

# Captura de vídeo (você pode alterar para qualquer vídeo ou usar '0' para webcam)
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
    
    # Inverter a imagem horizontalmente para corrigir o espelhamento
    img = cv2.flip(img, 1)
    
    # Convertendo a imagem para RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Detectando as mãos
    result = hands.process(img_rgb)

    # Desenhar as marcas das mãos na imagem
    if result.multi_hand_landmarks:
        for hand_lms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)

    # Pegando o tempo atual
    current_time = time.time()

    # Verificando se já passou o intervalo de tempo
    if current_time - last_time >= tempo:
        last_time = current_time
        iteracao(tempo)

    # Mostrar o vídeo
    cv2.imshow("Imagem", img)

    # Pressionar 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
