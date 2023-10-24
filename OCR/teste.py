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

# Diretório da pasta que contém as imagens
pasta_imagens = "IMAGE/"

# Listar arquivos na pasta de imagens
lista_arquivos = os.listdir(pasta_imagens)

# Loop através dos arquivos na pasta de imagens
for arquivo in lista_arquivos:
    # Verificar se o arquivo é uma imagem (por exemplo, termina com .png, .jpg, .jpeg, etc.)
    if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Caminho completo para a imagem
        caminho_img = os.path.join(pasta_imagens, arquivo)      
        # Imprima o texto extraído da imagem
        print(f'{arquivo}:')

# Caminho absoluto para a imagem
caminho_img = os.path.abspath("IMAGE/")

cupom_selecioando = input("Informe o cupom que deseja vizualizar EX: cumpom(1)")

# Concatenar o caminho completo com o nome do arquivo selecionado pelo usuário
caminho_img = os.path.join(pasta_imagens, cupom_selecioando)

# Verificar se o arquivo existe
if os.path.exists(caminho_img):
    # Ler a imagem usando o OpenCV
    imagem = cv2.imread(caminho_img)
    texto = pytesseract.image_to_string(imagem)
    print(texto)
else:
    print(f"Arquivo '{cupom_selecioando}' não encontrado na pasta de imagens.")
