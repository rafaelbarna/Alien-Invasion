import sys  # modulo para quando quisermos sair do game

import pygame   # funcionalidades do game

from settings import Settings

def run_game():

    #   Inicializa o jogo e cria um objeto na tela.
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(ai_settings.screen_width, ai_settings.screen_height)
    screen = pygame.display.set_mode((1200, 800))   # screen vai ser igual aos valores colocados entre chaves
    pygame.display.set_caption('ALIEN INVASION!')   # titulo do game que vai aparecer no browser

    bg_color = (230, 230, 230)  # cor definida por padrao antes do laco while. Cores RGB

#   Inicia o laco principal do jogo

    while True:
        #   Observa eventos de teclado e de mouse
        for event in pygame.event.get():    # utiliza pygames.event e salva em uma variavel event
            if event.type == pygame.QUIT:   # se o usuario clica no X da janela, o jogo vai fechar
                sys.exit()

        screen.fill(ai_settings.bg_color)  # preenche a tela com a cor escolhida em bg_color

        pygame.display.flip()


run_game()