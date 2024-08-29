# Importando libs/bibliotecas
# pip install mediapipe opencv-python pyautogui
import cv2
import mediapipe as mp
import pyautogui
import math

# Iniciando processamento das mãos
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Definindo parâmetros de detecção de mão
hands = mp_hands.Hands(max_num_hands = 1, min_detection_confidence = 0.7)

# Iniciando a captura de vídeo
cap = cv2.VideoCapture(0)

# Informando o tamanho da minha tela
screen_width, screen_height = pyautogui.size()

# FUNÇAO para calcular a menor distância entre dois pontos
def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z -p2.z) ** 2)

# Loop para processar as mãos
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertendo a imagem para RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processando a imagem para detecção de mão
    result = hands.process(frame_rgb)

    # Obtendo as dimensões da captura (frame)
    frame_height, frame_width, _ = frame.shape

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Extrair as coordenadas do ponto 8 (dedo indicados) e do ponto 4 (polegar)
            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            # Calculando distância entre polegar e indicador 
            distance = calculate_distance(index_finger_tip, thumb_tip)

            # Mover curusor do mouse
            x = int(index_finger_tip.x * frame_width)
            y = int(thumb_tip.y * frame_height)

            # Invertendo o eixo X e ajustando o eixo Y
            screen_x = screen_width - (screen_width / frame_width * x)
            screen_y = screen_height / frame_height * y

            pyautogui.moveTo(screen_x, screen_y)

            # Se os pontos 8 e 4 estão proximos o suficiente, se sim, clicar
            if distance < 0.05:
                pyautogui.click()

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Mostrar tela sem espelhar
    cv2.imshow("Camera", frame)

# Soltando a tudo
cap.release()
cv2.destroyAllWindows()
