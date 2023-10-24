import cv2
import os
import pytesseract

# Caminho completo para o diretório Tesseract-OCR
tesseract_dir = r'C:\Program Files\Tesseract-OCR'

# Caminho completo para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = os.path.join(tesseract_dir, 'tesseract.exe')

# Caminho completo para o diretório tessdata
tessdata_dir = os.path.join(tesseract_dir, 'tessdata')

# Especifique o TESSDATA_PREFIX
os.environ['TESSDATA_PREFIX'] = tessdata_dir

# Defina a largura e a altura desejadas da imagem
width = 640
height = 480

# Inicialize a webcam (0 é o índice da webcam, pode ser diferente em alguns sistemas)
cap = cv2.VideoCapture(0)
cap.set(3, width)  # Defina a largura do quadro
cap.set(4, height)  # Defina a altura do quadro

# Garanta que a pasta "IMAGE/" exista, se não, crie-a
if not os.path.exists("IMAGE/"):
    os.makedirs("IMAGE/")

# Loop para capturar uma foto da webcam
while True:
    # Capturar quadro da webcam
    ret, frame = cap.read()

    # Girar o quadro em 90 graus à direita
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Mostrar a imagem da webcam
    cv2.imshow('Webcam', frame)

    # Verificar se o usuário pressionou a tecla 's' para salvar a foto
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Determinar o nome do arquivo
        nome_arquivo = "captura_webcam.png"
        caminho_arquivo = os.path.join("IMAGE/", nome_arquivo)

        # Verificar se o arquivo já existe
        contador = 1
        while os.path.exists(caminho_arquivo):
            nome_arquivo = f"captura_webcam({contador}).png"
            caminho_arquivo = os.path.join("IMAGE/", nome_arquivo)
            contador += 1

        # Salvar a foto na pasta "IMAGE/"
        cv2.imwrite(caminho_arquivo, frame)
        print(f"Foto salva como {nome_arquivo}")
        break

    # Verifique se o usuário pressionou a tecla 'q' para sair do loop
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a webcam e feche a janela
cap.release()
cv2.destroyAllWindows()
