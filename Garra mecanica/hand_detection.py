import mediapipe as mp
import cv2

# Inicializando MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def detectar_maos(img):
    """
    Função responsável pela detecção das mãos.
    """
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    return result, mp_draw, mp_hands

def getHandCoordinates(hand_landmarks, img_width, img_height):
    """
    Função que retorna as coordenadas da palma da mão.
    """
    wrist_landmark = hand_landmarks.landmark[0]
    x = int((wrist_landmark.x - 0.5) * img_width)
    y = int((wrist_landmark.y - 0.5) * img_height)
    z = calcular_profundidade(hand_landmarks.landmark, img_width, img_height)
    return [x, y, z]

def calcular_profundidade(landmarks, img_width, img_height, fator_sensibilidade_z=500):
    """
    Função para calcular a profundidade z com base na área do bounding box da mão.
    """
    min_x, min_y, max_x, max_y = img_width, img_height, 0, 0
    for lm in landmarks:
        x, y = lm.x * img_width, lm.y * img_height
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)
    
    largura = max_x - min_x
    altura = max_y - min_y
    area_mao = largura * altura
    z = fator_sensibilidade_z / area_mao if area_mao > 0 else 0
    return z

def verificar_mao_aberta(hand_landmarks):
    """
    Verifica se a mão está aberta ou fechada.
    """
    dedos = [4, 8, 12, 16, 20]
    dedos_abertos = 0
    for i in range(1, 5):
        ponta_dedo = hand_landmarks.landmark[dedos[i]]
        articulacao = hand_landmarks.landmark[dedos[i] - 2]
        if ponta_dedo.y < articulacao.y:
            dedos_abertos += 1

    ponta_polegar = hand_landmarks.landmark[4]
    base_polegar = hand_landmarks.landmark[2]
    if ponta_polegar.x > base_polegar.x:
        dedos_abertos += 1

    return dedos_abertos >= 3