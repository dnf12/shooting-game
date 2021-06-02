#전투기가 운석과 충돌하거나 운석을 놓치면 게임 오버1

#게임 메시지 출력
def writeMessage(text):
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text,True, (255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()  #배경 음악 정지
    gameoverSound.play()  #게임 오버 사운드 재생
    sleep(2)
    pygame.mixer.music.paly(-1)  #배경 음악 재생
    runGame()

#전투기가 운석과 충돌했을 때 메시지 출력
def crach():
    global gamePad
    writeMessage('전투기 파괴!')

#게임 오버 메시지 보이기
def gameOver():
    global gamePad
    writeMessage('게임 오버!')


    
