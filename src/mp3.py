import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def tocar_musica(pasta, nome_musica):
    caminho = os.path.join(pasta, nome_musica)

    if not os.path.exists(caminho):
        print("Arquivo não encontrado")
        return
    
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

    print(f"\nTocando agora: {nome_musica}")
    print(f"Comandos: [P] - Pausa , [R] - Retomar, [S] - Parar")

    while True:

        comando = input("> ")

        if comando == "P" or comando == "p":
            pygame.mixer.music.pause()
            print("Música pausada.")
        elif comando == "R" or comando == "r":
            pygame.mixer.music.unpause()
            print("Música despausada.")
        elif comando == "S" or comando == "s":
            pygame.mixer.music.stop()
            print("Música parou.")
            return
        else:
            print("Comando inválido")

def main():

    pygame.mixer.init()

    pasta = "musica"

    if not os.path.isdir(pasta):
        print(f"Pasta '{pasta}' não encontrada")
        return

    arquivos_mp3 = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith(".mp3")]

    if not arquivos_mp3:
        print("Nenhum arquivo .mp3 encontrado.")

    while True:
        print("x---x---x---MP3 PLAYER---x---x---x")
        print("Minhas músicas: ")

        for i, musica in enumerate (arquivos_mp3, start =1):
            print(f"{i}.{musica}")

        escolher_comando = input("\nEscolha qual música à ser tocada! (ou pressione 'Q' para sair.): ")
        if escolher_comando == "Q" or escolher_comando == "q":
            print("Até logo!")
            break
        if not escolher_comando.isdigit():
            print("Digite um número válido.")
            continue
        escolha = int(escolher_comando) - 1

        if 0 <= escolha < len(arquivos_mp3):
            tocar_musica(pasta, arquivos_mp3[escolha])
        else:
            print("Escolha inválida.")


if __name__ == "__main__":
    main()