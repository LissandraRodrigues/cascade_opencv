# 22/05/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Programa que gera vetores das imagens geradas pelo geraPositivas.py

# Importações
import os

# Programa principal
def main():

    counter = 0

    # Número total de pastas positivas criadas pelo geraPositivas.
    positiveFolder = 159

    while counter != positiveFolder:

        # -num é o número total de positivas que rodará no seu treinamento.
        # Esse número total deve ser inferior ao total de imagens positivas geradas,
        # pois o treinamento consome um pouco mais do que o total estabelecido em -num.

        os.system("opencv_createsamples -info positivas{}/positivas{}.lst -num 8000 -w 28 -h 28 -vec vetor{}.vec".format(counter, counter, counter))

        counter += 1

main()


