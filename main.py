import pygame, random
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
fonte = pygame.font.SysFont("timenewroman", 16)
pygame.mixer.music.load("assets/ironsound.mp3")
pygame.mixer.music.play(-1)
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
    #pygame.draw.circle(tela,preto,(posicaoXPersona, posicaoYPersona), 40, 0 )
    tela.blit( iron, (posicaoXPersona, posicaoYPersona))

    posicaoYmissel = posicaoYmissel  + velocidadeMissel
    if posicaoYmissel > 600:
        posicaoYmissel = -240
        velocidadeMissel = velocidadeMissel + 1
        posicaoXmissel = random.randint(0,800)
        pygame.mixer.Sound.play(missileSound)

    tela.blit(missel, (posicaoXmissel, posicaoYmissel))

    #texto = fonte.render(str(posicaoXPersona)+"-"+str(posicaoXPersona),True,branco)
    #tela.blit(texto, (posicaoXPersona -20, posicaoYPersona-10))
    


    pygame.display.update()
    clock.tick(60)
pygame.quit()