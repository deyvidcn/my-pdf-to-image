import os
from pdf2image import convert_from_path

diretorio_pdf = './pdf'
diretorio_image = './image'

if not os.path.exists(diretorio_image):
    os.makedirs(diretorio_image)

for arquivo in os.listdir(diretorio_pdf):
    if arquivo.endswith('.pdf'):
        arquivo_pdf = os.path.join(diretorio_pdf, arquivo)
        arquivo_jpg = os.path.join(diretorio_image, os.path.splitext(arquivo)[0] + '.jpg')

        imagens = convert_from_path(arquivo_pdf)
        primeira_imagem = imagens[0]

        primeira_imagem.save(arquivo_jpg, 'JPEG')
