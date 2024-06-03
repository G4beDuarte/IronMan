import pygame, random, os
pygame.init()
tamanho = (800,600)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Iron Man do Marcão")
branco = (255,255,255)
preto = (0,0,0)
iron = pygame.image.load("assets/iron.png")
fundo = pygame.image.load("assets/fundo.png")
missel = pygame.image.load("assets/missile.png")
posicaoXPersona = 275
posicaoYPersona = 236
movimentoXPersona = 0
movimentoYPersona = 0
posicaoXmissel = 400
posicaoYmissel = -240
velocidadeMissel = 1
missileSound = pygame.mixer.Sound("assets/missile.wav")
pygame.mixer.Sound.play(missileSound)
fonte = pygame.font.SysFont("timesnewroman", 28)
pygame.mixer.music.load("assets/ironsound.mp3")
pygame.mixer.music.play(-1)
pontos = 0
larguraPersona = 250
alturaPersona = 127
larguraMissel = 50
alturaMissel = 250
dificuldade = 0
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXPersona = + 10
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXPersona = - 10
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXPersona = 0   
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYPersona = - 10
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYPersona = + 10
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYPersona = 0 
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYPersona = 0  

    posicaoXPersona = posicaoXPersona + movimentoXPersona
    if posicaoXPersona < 0:
        posicaoXPersona = 10
    elif posicaoXPersona > 550:
        posicaoXPersona = 540 

    posicaoYPersona = posicaoYPersona + movimentoYPersona
    if posicaoYPersona < 0:
        posicaoYPersona = 10
    elif posicaoYPersona > 473:
        posicaoYPersona = 463

    tela.fill(branco)
    tela.blit(fundo,(0,0))
    tela.blit( iron, (posicaoXPersona, posicaoYPersona))

    posicaoYmissel = posicaoYmissel  + velocidadeMissel
    if posicaoYmissel > 600:
        posicaoYmissel = -240
        pontos = pontos + 1
        velocidadeMissel = velocidadeMissel + 1
        posicaoXmissel = random.randint(0,800)
        pygame.mixer.Sound.play(missileSound)

    tela.blit(missel, (posicaoXmissel, posicaoYmissel))
    texto = fonte.render("Pontos: "+str(pontos),True,branco)
    tela.blit(texto, (10,10))
    
    pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona + alturaPersona))
    pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona + larguraPersona))
    pixelsMisselY = list(range(posicaoYmissel, posicaoYmissel + alturaMissel))
    pixelsMisselX = list(range(posicaoXmissel, posicaoXmissel + larguraMissel))

    os.system("clear")
    print(  )
    if len( list(set(pixelsMisselY).intersection(set(pixelsPersonaY)))) > dificuldade:
        if len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX)) )) > dificuldade:
            print("Morreu!")
        else:
            print("Ainda vivo, mas por pouco")
    else:
        print("Ainda vivo")



    pygame.display.update()
    clock.tick(60)
pygame.quit()