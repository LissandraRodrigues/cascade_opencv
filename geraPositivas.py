# 22/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Programa que gera mais imagens positivas para o treinamento a partir de imagens positivas base.

# Importações
import glob
import os

# Retorna uma lista com os caminhos das imagens encontradas na pasta.
def imageList():

    # Caminho da pasta que contém as imagens positivas base.
    chosenFolder = 'images/'

    images = glob.glob(chosenFolder)

    return images

def main():

    imagePath = imageList()

    counter = 0

    # Para cada imagem base, cria, neste caso, 180 imagens positivas em uma pasta.
    # A quantidade de pastas geradas será igual a quantidade de imagens contidas em imagePath.
    for image in imagePath:

        # -num é a quantidade de imagens positivas que serão geradas a partir da imagem base, neste caso.

        os.system("opencv_createsamples -img {} -bg negativas/bg.txt -info positivas{}/positivas{}.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -w 48 -h 48 -num 180 -bgcolor 255 -bgthresh 8".format(image, counter, counter))

        counter += 1

main()